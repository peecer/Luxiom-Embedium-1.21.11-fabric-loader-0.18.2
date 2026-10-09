#!/usr/bin/env python3
"""Inspect REAL 1.21.11 Fabric release JAR metadata for loader 0.18.2."""
import urllib.request,urllib.parse,json,io,zipfile,hashlib,sys
ROOTS=("sodium","iris","lambdynamiclights","fabric-api")
API="https://api.modrinth.com/v2"
def get(path,query=None):
 u=API+path
 if query:u+="?"+urllib.parse.urlencode(query)
 r=urllib.request.Request(u,headers={"User-Agent":"Luxiom-Fabric-Compatibility-Check/1.0","Accept":"application/json"})
 with urllib.request.urlopen(r,timeout=50) as res:return json.load(res)
def inspect(v):
 f=next((x for x in v["files"] if x["filename"].endswith(".jar") and x.get("primary")),None)
 if f is None:f=next(x for x in v["files"] if x["filename"].endswith(".jar"))
 with urllib.request.urlopen(urllib.request.Request(f["url"],headers={"User-Agent":"Luxiom-Fabric-Compatibility-Check/1.0"}),timeout=90) as r:data=r.read()
 if hashlib.sha512(data).hexdigest()!=f["hashes"]["sha512"]:raise ValueError("SHA512 mismatch")
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  meta=json.loads(z.read("fabric.mod.json"))
  embedded=[]
  for e in meta.get("jars",[]):
   path=e.get("file")
   if not path or path not in z.namelist():continue
   with zipfile.ZipFile(io.BytesIO(z.read(path))) as inner:
    if "fabric.mod.json" in inner.namelist():
     imeta=json.loads(inner.read("fabric.mod.json"))
     embedded.append((imeta.get("id"),imeta.get("depends",{}).get("fabricloader","<not specified>")))
 return {"version":v["version_number"],"id":v["id"],"loader":meta.get("depends",{}).get("fabricloader","<not specified>"),"id_in_jar":meta.get("id"),"minecraft":meta.get("depends",{}).get("minecraft"),"deps":[(x.get("project_id"),x.get("version_id"),x.get("dependency_type")) for x in v.get("dependencies",[])],"nested":embedded[:25]}
for slug in ROOTS:
 print("###",slug,flush=True)
 try:
  versions=get("/project/"+slug+"/version",{"loaders":json.dumps(["fabric"]),"game_versions":json.dumps(["1.21.11"])})
  vs=sorted((v for v in versions if v.get("version_type")=="release"),key=lambda v:v.get("date_published",""))
  print("releases",len(vs),flush=True)
  for v in vs[:6]+(vs[-1:] if len(vs)>6 else []):
   try:print(json.dumps(inspect(v)),flush=True)
   except Exception as e:print("candidate error",v.get("version_number"),str(e),flush=True)
 except Exception as e:print("project error",slug,str(e),flush=True)
