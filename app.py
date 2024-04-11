from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    personas = [
        {"nombre": "Juan", "apellidos": "Pérez", "id": "1", "cumpleaños": "10/03/1984", "gastos": 15000},
        {"nombre": "María", "apellidos": "González", "id": "2", "cumpleaños": "02/07/1976", "gastos": 27500},
        {"nombre": "Pedro", "apellidos": "Rodríguez", "id": "3", "cumpleaños": "25/11/1995", "gastos": 19200}
    ]
    total = sum(persona["gastos"] for persona in personas)
    return render_template("index.html", personas=personas, total=total)