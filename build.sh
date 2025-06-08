python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate

# Copiar el gif al folder public para que sea accesible
cp assets/code.gif public/code.gif

rm -f frontend.zip
