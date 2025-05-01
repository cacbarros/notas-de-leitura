@echo off
REM :: Caminho do ambiente conda e da pasta de trabalho
set "PASTA_PROJETO=C:\Users\cesar\notas-de-leitura"
set "AMBIENTE=notas-leitura-env"

REM :: Iniciar PowerShell padrão: ativa o ambiente, entra na pasta e roda quarto render
start powershell -NoExit -Command "conda activate %AMBIENTE%; cd '%PASTA_PROJETO%'; quarto render index.qmd"

REM :: Iniciar outra janela PowerShell com Jupyter Lab
start "" "%windir%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoExit -Command "conda activate %AMBIENTE%; cd '%PASTA_PROJETO%'; jupyter lab"
