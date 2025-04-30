import bibtexparser
from bibtexparser.bwriter import BibTexWriter

# Ficheiro original
bib_path = "rc_calculo_analise_apa.bib"

# Carrega a base
with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

# Filtra apenas entradas do tipo 'book'
livros = [entry for entry in bib_database.entries if entry.get("ENTRYTYPE", "").lower() == "book"]

# Cria novo banco de dados
bib_books = bibtexparser.bibdatabase.BibDatabase()
bib_books.entries = livros

# Exporta para novo ficheiro
output = "rc_calculo_analise_books.bib"
with open(output, "w", encoding="utf-8") as f:
    writer = BibTexWriter()
    f.write(writer.write(bib_books))

print(f"{len(livros)} entradas @book salvas em {output}")
