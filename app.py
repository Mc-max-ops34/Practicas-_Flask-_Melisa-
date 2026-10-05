from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/alumnos')
def alumnos():
    lista_alumnos = ["Jose Luis", "Helen", "Rosalia", "Diana", "Angel"]
    return render_template('alumnos.html', alumnos=lista_alumnos)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        print(f"Nuevo mensaje de {nombre} ({email}): {mensaje}")
        
        return f"¡Gracias {nombre}! Hemos recibido tu mensaje."
        
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
