import sys, io, os, json
from datetime import datetime
name, path = sys.argv[1], sys.argv[2]
d=json.load(io.open("out.json","r",encoding="utf-8"))
cat=d["categoria"]; ts=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
os.makedirs("docs/Consolidados", exist_ok=True)
blk=[f"=== Fuente: {name} — {path} — {ts} ===",
     f"**Resumen:** {d.get('resumen','')}",
     ("**Áreas críticas:**\n- "+"\n- ".join(d["areas_criticas"])) if d.get("areas_criticas") else "",
     ("**TODO:**\n- "+"\n- ".join(d["todos"])) if d.get("todos") else "",
     ("**Servicios afectados:** "+", ".join(d["servicios_afectados"])) if d.get("servicios_afectados") else "",
     ("**ADRs sugeridos:**\n- "+"\n- ".join(d["adrs_sugeridos"])) if d.get("adrs_sugeridos") else "",
     f"**KEEP:** {d.get('keep',True)} — {d.get('motivo_keep','')}",
     ("**Tags:** "+", ".join(d.get("tags",[]))) if d.get("tags") else ""]
io.open(f"docs/Consolidados/{cat}-Consolidado.md","a",encoding="utf-8").write("\n".join([b for b in blk if b])+"\n\n")
prev=io.open("CHANGELOG.md","r",encoding="utf-8").read() if os.path.exists("CHANGELOG.md") else ""
io.open("CHANGELOG.md","w",encoding="utf-8").write(prev+f"- Procesado: {name} — {path} → {cat} ({ts}) KEEP={d.get('keep',True)}\n")
