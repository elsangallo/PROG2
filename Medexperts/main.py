from flask import Flask
app = Flask("medexperts")
from jinja2 import Jinja2
app = Jinja2("medexperts")
@app.route('/startseite')
def startseite():
    return ...
@app.route('/falleingang'methods=['GET', 'POST'])
def falleingang():
    if request.method == 'POST':
        fallnr = request.form['fallnr']
        vornamen = request.form['vornamen']
        nachnamen = request.form['nachnamen']
        auftraggeber = request.form['auftraggeber']
        datum = request.form['datum']
        termin = request.form['termin']
        rueckgabe_string = "Fallnummer: " + fallnr /n + "Namen: " + vornamen + " " + nachnamen /n + "Auftraggeber: " + auftraggeber /n + "Eingangsdatum: " + datum /n + "Disziplin: " + disziplin /n + "Abschlusstermin: " + termin
        return rueckgabe_string
    return render_template("index.html")

@app.route('/abwesenheiten')
def abwesenheit():

@app.route('/kalender')
def kalender():

@app.route('/zuordnung')
def zuordnung():

if __name__ == "__main__":
    app.run(debug=True, port=5000)
