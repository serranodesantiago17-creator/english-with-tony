# Genera index.html a partir de la carpeta fuente/ (python3 build.py)
import pathlib
base = pathlib.Path(__file__).parent
src = base / "fuente"
parts = ["temas1.js", "temas2.js", "ampliacion.js", "temas3.js", "temas4.js"]
data = "\n".join((src / p).read_text(encoding="utf-8") for p in parts)
html = (src / "app.html").read_text(encoding="utf-8").replace("/*TEMAS*/", data)
(base / "index.html").write_text(html, encoding="utf-8")
print("index.html generado")
