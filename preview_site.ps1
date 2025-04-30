# Script para garantir preview correto do website Quarto
cd (Split-Path -Parent $MyInvocation.MyCommand.Definition)
conda activate notas-leitura-env
quarto preview index.qmd
