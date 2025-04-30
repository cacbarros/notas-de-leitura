import bibtexparser
from collections import Counter

# Caminho do arquivo .bib a verificar
bib_path = "rc_calculo_analise.bib"

# Campos obrigatórios para citação básica
campos_obrigatorios = ["author", "title", "year"]

with open(bib_path, encoding="utf-8") as bibfile:
    try:
        bib_database = bibtexparser.load(bibfile)
    except Exception as e:
        print(f"\n❌ Erro ao carregar o ficheiro .bib: {e}")
        exit(1)

entries = bib_database.entries
print(f"\n📚 Total de entradas carregadas: {len(entries)}\n")

ids = [entry.get("ID", "") for entry in entries]
duplicados = [item for item, count in Counter(ids).items() if count > 1 and item]

# Verifica duplicações de chave
if duplicados:
    print("❗ Entradas com ID duplicado:")
    for dup in duplicados:
        print(f"  - {dup}")
    print("")

# Verifica entrada a entrada
erros_criticos = 0

for i, entry in enumerate(entries, start=1):
    entrada_ok = True
    entry_id = entry.get("ID", "(sem ID)")
    entry_type = entry.get("ENTRYTYPE", None)

    print(f"[{i}] {entry_id}")

    if not entry_type:
        print("    ❌ ERRO CRÍTICO: tipo de entrada (ENTRYTYPE) ausente.")
        entrada_ok = False

    if not entry_id or entry_id.strip() == "":
        print("    ❌ ERRO CRÍTICO: identificador (ID) ausente.")
        entrada_ok = False

    for campo in campos_obrigatorios:
        if campo not in entry or entry[campo].strip() == "":
            print(f"    ⚠️  Campo obrigatório ausente ou vazio: {campo}")
            entrada_ok = False

    if not entrada_ok:
        erros_criticos += 1

    print("")

# Resumo
if erros_criticos == 0:
    print("✅ Todas as entradas estão estruturalmente corretas para uso com Quarto/Pandoc.")
else:
    print(f"⚠️ Foram encontrados {erros_criticos} erros críticos em {len(entries)} entradas.")
