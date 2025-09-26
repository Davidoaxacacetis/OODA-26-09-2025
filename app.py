from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    mensaje = "<h1>Esta es la pagina de inicio</h1>"
    mensaje += "<ul>"
    mensaje += "<h2> Acerca de http://127.0.0.1:5000/datos</h2>"
    mensaje += "<h2> Tema 1 http://127.0.0.1:5000/palmer</h2>"
    mensaje += "<h2> Tema 2 http://127.0.0.1:5000/dembele</h2>"
    mensaje += "</ul>"
    mensaje += "secreto http://127.0.0.1:5000/as" 
    return mensaje

@app.route("/datos")
def dato():
    mensaje = "<h1> Oaxaca Orona David Adrian </h1>"
    mensaje += "<h2> Grupo: 3 - D </h2"
    mensaje += "<h2> Matricla: 24308060610040</h2>"
    mensaje += "<h2> Especialidad: Programación</h2>"
    return mensaje

@app.route("/palmer")
def tema():
    mensaje = "<h1> Cole Palmer </h1>"
    mensaje += "<h4>Cole Jermaine Palmer (Mánchester, 6 de mayo de 2002) es un futbolista británico que juega como mediocentro ofensivo o extremo derecho en el Chelsea F. C. de la Premier League de Inglaterra. Es internacional con la selección inglesa desde 2023.</h4>"
    return mensaje

@app.route("/dembele")
def tema2():
    mensaje = "<h1> Ousmane Dembélé</h1>"
    mensaje += "<h3>Masour Ousmane Dembélé (pronunciación en francés: masuʁ usman dɛmbele; Vernon, Eure, 15 de mayo de 1997) es un futbolista francés que juega de delantero en el Paris Saint-Germain F. C. de la Ligue 1.</h3>"
    return mensaje

@app.route('/as')
def hola_ailin():
    return '<h1> Hola Ailin </h1>'

if __name__ =='__main__':
    app.run(debug=True)

