#!/usr/bin/env python3
"""Build REAL graphics-alternative Modrinth modpacks. NOT a Luxium or Embeddium port."""
import argparse
import json
import sys
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

API="https://api.modrinth.com/v2"
ROOTS=("iris","lambdynamiclights","fabric-api","sodium")
AGENT="LuxiomGraphicsAlternative/0.2 (GitHub Actions; dependency resolver)"

class PackError(Exception):
    pass

def get(path, params=None):
    url=API+path
    if params:
        url+="?"+urllib.parse.urlencode(params)
    request=urllib.request.Request(url,headers={"Accept":"application/json","User-Agent":AGENT})
    try:
        with urllib.request.urlopen(request,timeout=45) as stream:
            return json.load(stream)
    except Exception as exc:
        raise PackError("Modrinth API request failed for "+path+": "+str(exc)) from exc

def latest(pid, mc):
    all_versions=get("/project/"+urllib.parse.quote(pid,safe="")+"/version",{
        "loaders":json.dumps(["fabric"]),
        "game_versions":json.dumps([mc]),
    })
    versions=[v for v in all_versions if v.get("version_type")=="release"]
    if not versions:
        raise PackError("No stable Fabric "+mc+" version of "+pid)
    return max(versions,key=lambda v:v.get("date_published",""))

class Resolver:
    def __init__(self,mc):
        self.mc=mc
        self.meta={}
        self.mods={}
        self.visiting=set()
    def project(self,slug):
        if slug not in self.meta:
            obj=get("/project/"+urllib.parse.quote(slug,safe=""))
            self.meta[slug]=obj
            self.meta[obj["id"]]=obj
        return self.meta[slug]
    def resolve(self,slug,pinned=None):
        obj=self.project(slug)
        pid=obj["id"]
        if pid in self.mods:
            if pinned and self.mods[pid]["version"]["id"]!=pinned:
                raise PackError("Conflicting pinned dependency for "+obj["title"])
            return
        if pid in self.visiting:
            raise PackError("Circular dependency for "+obj["title"])
        self.visiting.add(pid)
        try:
            version=get("/version/"+pinned) if pinned else latest(pid,self.mc)
            if version.get("project_id")!=pid or self.mc not in version.get("game_versions",[]) or "fabric" not in version.get("loaders",[]):
                raise PackError("Incompatible dependency "+obj["title"]+" "+str(version.get("version_number")))
            jar_files=[f for f in version.get("files",[]) if f.get("filename","").lower().endswith(".jar")]
            if not jar_files:
                raise PackError("No JAR for "+obj["title"])
            file=next((f for f in jar_files if f.get("primary")),jar_files[0])
            name=file["filename"]
            checksum=file.get("hashes",{}).get("sha512")
            host=urllib.parse.urlsplit(file.get("url",""))
            if Path(name).name!=name or "\\" in name or len(checksum or "")!=128 or host.scheme!="https" or host.hostname not in ("cdn.modrinth.com","cdn-raw.modrinth.com"):
                raise PackError("Untrusted file metadata for "+obj["title"])
            self.mods[pid]={"project":obj,"version":version,"file":file}
            for dep in version.get("dependencies",[]):
                if dep.get("dependency_type")!="required":
                    continue
                dp=dep.get("project_id")
                dv=dep.get("version_id")
                if not dp and dv:
                    dp=get("/version/"+dv)["project_id"]
                if not dp:
                    raise PackError("Unresolvable required dependency of "+obj["title"])
                self.resolve(dp,dv)
        except Exception:
            self.mods.pop(pid,None)
            raise
        finally:
            self.visiting.remove(pid)
    def collect(self):
        for slug in ROOTS:
            self.resolve(slug)
        for e in self.mods.values():
            for dep in e["version"].get("dependencies",[]):
                if dep.get("dependency_type")!="incompatible":
                    continue
                pid=dep.get("project_id")
                vid=dep.get("version_id")
                if pid in self.mods and (not vid or self.mods[pid]["version"]["id"]==vid):
                    raise PackError("Declared incompatibility in "+e["project"]["title"])
                if vid and any(x["version"]["id"]==vid for x in self.mods.values()):
                    raise PackError("Declared incompatible version in "+e["project"]["title"])
        return sorted(self.mods.values(),key=lambda e:e["project"]["title"])

def build(mc,output):
    mods=Resolver(mc).collect()
    if len(mods)<4:
        raise PackError("Not all four required graphics components could be resolved")
    files=[]
    used=set()
    for mod in mods:
        file=mod["file"]
        path="mods/"+file["filename"]
        if path in used:
            raise PackError("Duplicate filename "+path)
        used.add(path)
        files.append({
            "path":path,
            "hashes":{"sha512":file["hashes"]["sha512"]},
            "downloads":[file["url"]],
            "env":{"client":"required","server":"unsupported"},
            "fileSize":int(file.get("size",0)),
        })
    index={
        "formatVersion":1,
        "game":"minecraft",
        "versionId":mc+"-graphics-alternative-0.2",
        "name":"Graphics Alternative (NOT Luxium) "+mc,
        "summary":"Real Sodium, Iris, LambDynamicLights, Fabric API, and required dependencies; not a Luxium or Embeddium port.",
        "files":files,
        "dependencies":{"minecraft":mc,"fabric-loader":"0.19.5"},
    }
    notes=("NOT A LUXIUM OR EMBEDDIUM PORT. Import in a NEW, CLEAN Fabric instance.\n"
           "Requires Fabric Loader 0.19.5 or newer. Never install the prior UNIMPLEMENTED JARs.\n"
           "Iris supports shaders but a shader pack must be installed separately.\n"
           "Minecraft client startup has not been tested by this build pipeline.\n")
    output=Path(output)
    output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,"w",zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("modrinth.index.json",json.dumps(index,indent=2)+"\n")
        archive.writestr("README.txt",notes)
        archive.writestr("COMPONENTS.txt","\n".join(f'{x["project"]["title"]}: {x["version"]["version_number"]}' for x in mods)+"\n")
    print("Created",output)
    for x in mods:
        print(x["project"]["title"],x["version"]["version_number"])

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--minecraft",required=True,choices=("1.21.11","26.3"))
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    try:
        build(args.minecraft,args.output)
    except PackError as exc:
        print("ERROR:",exc,file=sys.stderr)
        sys.exit(1)
