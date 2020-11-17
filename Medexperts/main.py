from flask import Flask
app = Flask("medexperts")
@app.route('/startseite')
def startseite():
    return ...
@app.route('/kalender')
def kalender():

@app.route('/falleingang'methods=['GET', 'POST'])
def falleingang():
    if request.method == 'Falleingang':
        termin = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
