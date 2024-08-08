#!/bin/bash

# Caminho para o seu ambiente virtual
VENV_DIR="venv"
echo "Dentro de $(pwd)"

# Verifica se o diretório do venv existe
if [ -d "$VENV_DIR" ]; then
    # Ativa o ambiente virtual
    source "$VENV_DIR/bin/activate"
    echo "Ambiente virtual ativado."
else
    echo "Diretório do ambiente virtual não encontrado: $VENV_DIR"
fi
