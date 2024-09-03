from app import app

@app.route('/')
def home():
  return '¡Hola, Flask - VSCode to Main!'
