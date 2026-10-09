#!/usr/bin/env python3
"""Build a REAL shader/optimization modpack, not an actual Luxium port."""
import argparse
import hashlib
import io
import json
import sys
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

import build_compatible_pack as core

MC="1.21.11"
LOADER="0.18.2"
core.ROOTS=core.ROOTS + ("immediatelyfast","cull-leaves","modernfix-mvus")
core.PINS.update({
    "immediatelyfast":"4EwhsTu7",  # 1.14.3 Fabric 1.21.11
    "cull-leaves":"yrL6pwHZ",    # 4.1.1.1 Fabric 1.21.11
    "modernfix-mvus":"int4tWnO", # 5.25.2 Fabric 1.21.11
})

def shader_for(mc):
    candidates=core.get("/project/complementary-reimagined/version",{
        "loaders":json.dumps(["iris"]),
        "game_versions":json.dumps([mc]),
    })
    candidates=[v for v in candidates if v.get("version_type")=="release" and
                "iris" in v.get("loaders",[]) and mc in v.get("game_versions",[])]
    if not candidates:
        raise core.PackError("No Complementary Reimagined release explicitly supports "+mc+" and Iris")
    v=max(candidates,key=lambda x:x.get("date_published",""))
    files=[f for f in v.get("files",[]) if f.get("filename","").lower().endswith(".zip")]
    if not files:
        raise core.PackError("Selected shader version has no zip file")
    f=next((x for x in files if x.get("primary")),files[0])
    u=urllib.parse.urlsplit(f.get("url",""))
    if u.scheme!="https" or u.hostname not in ("cdn.modrinth.com","cdn-raw.modrinth.com"):
        raise core.PackError("Unexpected shader file host")
    if Path(f["filename"]).name!=f["filename"] or len(f.get("hashes",{}).get("sha512",""))!=128:
        raise core.PackError("Invalid shader file metadata")
    request=urllib.request.Request(f["url"],headers={"User-Agent":core.AGENT})
    with urllib.request.urlopen(request,timeout=90) as response:
        data=response.read()
    if hashlib.sha512(data).hexdigest()!=f["hashes"]["sha512"]:
        raise core.PackError("Shader ZIP SHA-512 mismatch")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if not any(name.startswith("shaders/") or "/shaders/" in name for name in archive.namelist()):
            raise core.PackError("Shader ZIP contains no shaders directory")
    print("Verified shader pack:",v["version_number"],f["filename"],flush=True)
    return v,f

def build(output):
    selected=core.Resolver(MC).collect()
    if len(selected)<7:
        raise core.PackError("Missing at least one graphics/performance component")
    core.validate_binary_files(selected,LOADER)
    shader_version,shader=shader_for(MC)
    files=[]
    used=set()
    for mod in selected:
        f=mod["file"]
        path="mods/"+f["filename"]
        if path in used:
            raise core.PackError("Duplicate output JAR path "+path)
        used.add(path)
        files.append({
            "path":path,
            "hashes":{"sha512":f["hashes"]["sha512"]},
            "downloads":[f["url"]],
            "env":{"client":"required","server":"unsupported"},
            "fileSize":int(f.get("size",0)),
        })
    shader_path="shaderpacks/"+shader["filename"]
    if shader_path in used:
        raise core.PackError("Duplicate shader pack output filename")
    files.append({
        "path":shader_path,
        "hashes":{"sha512":shader["hashes"]["sha512"]},
        "downloads":[shader["url"]],
        "env":{"client":"required","server":"unsupported"},
        "fileSize":int(shader.get("size",0)),
    })
    index={
        "formatVersion":1,
        "game":"minecraft",
        "versionId":"1.21.11-Fabric-0.18.2-Luxium-style-NOT-Luxium",
        "name":"Luxium-style Real Graphics — NOT Luxium — Fabric 0.18.2",
        "summary":"Iris, Sodium, dynamic lighting, optimized renderer and shaderpack; NOT original Luxium.",
        "files":files,
        "dependencies":{"minecraft":MC,"fabric-loader":LOADER},
    }
    notes=(
        "DO NOT INSTALL THE ORIGINAL FORGE 1.20.1 LUXIUM JAR HERE.\n"
        "NOT an actual Luxium/Embeddium port: no Luxium custom renderer, LSR, or TFR.\n"
        "All selected JARs are verified against Fabric Loader 0.18.2.\n"
        "Complementary shader pack is included by an authenticated Modrinth checksum reference.\n"
        "Import this .mrpack to a clean launcher instance and select the shader pack in Iris.\n"
        "Do NOT add the old UNIMPLEMENTED JARs or Compact BedWars HUD 1.3.\n"
        "No Minecraft client launch test has been performed.\n"
    )
    out=Path(output)
    out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("modrinth.index.json",json.dumps(index,indent=2)+"\n")
        archive.writestr("README.txt",notes)
        archive.writestr("COMPONENTS.txt","\n".join(
            f'{m["project"]["title"]}: {m["version"]["version_number"]}' for m in selected
        )+"\nShader pack: "+shader_version["version_number"]+"\n")
    print("Produced pack:",out)
    print("Fabric Loader:",LOADER)
    for mod in selected:
        print("COMPONENT:",mod["project"]["title"],mod["version"]["version_number"])
    print("SHADER:",shader_version["version_number"])

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    try:
        build(args.output)
    except Exception as exc:
        print("Build failed:",exc,file=sys.stderr)
        raise
