# -------------------------------------------
# Script de atualização do site Quarto
# Local: raiz do projeto notas-de-leitura
# -------------------------------------------

Write-Host ""
Write-Host "Iniciando atualização do site..."

# 1. Ativar ambiente Conda (se necessário)
# Ajuste o nome do ambiente abaixo se for diferente
conda activate notas-leitura-env

# 2. Verificar status do Git
Write-Host ""
Write-Host "Verificando alterações locais..."
git status

# 3. Adicionar alterações (exceto as ignoradas no .gitignore)
Write-Host ""
Write-Host "Adicionando alterações..."
git add .

# 4. Criar commit com data e hora atual
$data = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Atualização automática em $data"

# 5. Enviar alterações para o repositório remoto
Write-Host ""
Write-Host "Enviando para o GitHub..."
git push origin main

# 6. Publicar o site usando Quarto
Write-Host ""
Write-Host "Publicando o site com Quarto..."
quarto publish gh-pages

Write-Host ""
Write-Host "Atualização concluída com sucesso."
