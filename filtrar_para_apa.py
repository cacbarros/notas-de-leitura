import bibtexparser
from bibtexparser.bwriter import BibTexWriter

bib_path = "rc_calculo_analise.bib"

with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

campos_por_tipo = {
    "book": {"author", "title", "year", "publisher"},
    "article": {"author", "title", "year", "journal", "volume", "pages"},
    "incollection": {"author", "title", "booktitle", "year", "publisher"},
    "misc": {"title", "year"},  # author ou editor obrigatório em prática
    "online": {"author", "title", "year", "url"},
}

def entrada_valida(entry):
    entry_type = entry.get("ENTRYTYPE", "").lower()
    required = campos_por_tipo.get(entry_type)
    if not required:
        return False
    for campo in required:
        if campo not in entry or not entry[campo].strip():
            return False
    if entry_type == "misc" and not (entry.get("author") or entry.get("editor")):
        return False
    return True

entradas_validas = [e for e in bib_database.entries if entrada_valida(e)]

bib_filtrado = bibtexparser.bibdatabase.BibDatabase()
bib_filtrado.entries = entradas_validas

with open("rc_calculo_analise_apa.bib", "w", encoding="utf-8") as f:
    writer = BibTexWriter()
    f.write(writer.write(bib_filtrado))

print(f"{len(entradas_validas)} entradas APA salvas em rc_calculo_analise_apa.bib")
