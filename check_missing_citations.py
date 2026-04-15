import re
from pathlib import Path

# Percorsi da modificare secondo la tua struttura
tex_dir = Path("Tex")
bib_file = Path("Formal_Models.bib")

# 1. Trova tutte le chiavi citate nei .tex
citations = set()
for tex_file in tex_dir.glob("*.tex"):
    content = tex_file.read_text()
    matches = re.findall(r'\\cite(?:\[[^\]]*\])?{([^}]+)}', content)
    for m in matches:
        for key in m.split(","):
            citations.add(key.strip())

# 2. Trova tutte le chiavi presenti nel .bib
with open(bib_file) as f:
    bib_content = f.read()
bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_content))

# 3. Mostra le chiavi citate ma non trovate
missing = citations - bib_keys
if missing:
    print("❌ Citazioni mancanti nel .bib:")
    for key in sorted(missing):
        print(f"  - \\cite{{{key}}}")
else:
    print("✅ Tutte le citazioni hanno una voce nel .bib.")