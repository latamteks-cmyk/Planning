import os, sys, io, json, requests
MODEL=os.getenv("OPENAI_MODEL","gpt-4o-mini")
tpl=io.open("prompts/PROCESAR_DOCUMENTO.md","r",encoding="utf-8").read()
txt=io.open(sys.argv[1],'r',encoding='utf-8',errors='ignore').read()
prompt=tpl.replace("{{CONTENIDO}}", txt[:400000])
r=requests.post("https://api.openai.com/v1/chat/completions",
 headers={"Authorization":f"Bearer {os.environ['OPENAI_API_KEY']}"},
 json={"model":MODEL,"temperature":0,"response_format":{"type":"json_object"},
       "messages":[{"role":"user","content":prompt}]}, timeout=120)
r.raise_for_status()
data=json.loads(r.json()["choices"][0]["message"]["content"])
assert data["categoria"] in ["01-Vision-Estrategia","02-Gobernanza","03-Arquitectura","04-Datos","05-Módulos","06-Legal-Compliance","07-UI-UX","08-DevOps","09-Requisitos","10-Backlog","11-Investigaciones","12-Glosario","13-ADR","99-Misceláneo"]
io.open("out.json","w",encoding="utf-8").write(json.dumps(data,ensure_ascii=False,indent=2))
