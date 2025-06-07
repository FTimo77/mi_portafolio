python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only

# Verifica si el archivo existe y descomprime correctamente
if [ -f frontend.zip ]; then
    unzip frontend.zip -d public
    rm -f frontend.zip
elif [ -f web.zip ]; then
    unzip web.zip -d public
    rm -f web.zip
else
    echo "No se encontró el archivo zip exportado por Reflex"
    exit 1
fi

deactivate