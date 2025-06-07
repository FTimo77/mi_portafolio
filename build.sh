python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only

if [ -f frontend.zip ]; then
    unzip -j frontend.zip -d public
    rm -f frontend.zip
elif [ -f web.zip ]; then
    unzip -j web.zip -d public
    rm -f web.zip
else
    echo "No se encontró el archivo zip exportado por Reflex"
    exit 1
fi

echo "Contenido del directorio actual:"
ls -l
echo "Contenido de public (si existe):"
ls -l public || echo "No existe la carpeta public"

deactivate