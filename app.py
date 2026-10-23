from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "1991"

Farge = ["Svart", "Hvit", "Lilla", "Grønn", "Gul"]
Gpu = [
    {"Navn": "5090", "pris": 20000},
    {"Navn": "5070ti", "pris": 14000},
    {"Navn": "5070", "pris": 8000},
    {"Navn": "9070xt", "pris": 9000},
    {"Navn": "5060", "pris": 5000},
    {"Navn": "9060xt", "pris": 4500},
    {"Navn": "5060ti", "pris": 7500}
]
Cpu = [
    {"Navn": "7800x3d", "pris": 4000},
    {"Navn": "i5 7890k", "pris": 3000},
    {"Navn": "i9 13500", "pris": 6000},
    {"Navn": "7900x3d", "pris": 5000},
    {"Navn": "9800x3d", "pris": 7000},
    {"Navn": "i3 4500k", "pris": 1800},
    {"Navn": "R7 9000", "pris": 2700},]
Ram = [
    {"Navn": "8gb", "pris": 1500},
    {"Navn": "16gb", "pris": 2500},
    {"Navn": "24gb", "pris": 4000},
    {"Navn": "32gb", "pris": 7000},
    {"Navn": "64gb", "pris": 12000},
]
def getItem(items, key):
    """
    Looks up and returns the full dictionary object from a list by its 'Navn'.
    Returns None if the item is not found.
    """
    for item in items:
        if item.get("Navn") == key:
            return item
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Bestilling")
def bestilling():

    return render_template("Bestilling.html", Farge=Farge, Ram=Ram, Cpu=Cpu, Gpu=Gpu)

@app.route("/Confirmation1", methods=["POST"])
def Conf1():
    Farge = request.form.get("Farge")
    valgtGpu = getItem(Gpu, request.form.get("Gpu")) 
    valgtCpu = getItem(Cpu, request.form.get("Cpu"))
    valgtRam = getItem(Ram, request.form.get("Ram"))
    if "0" in (Farge, Gpu, Cpu, Ram) or not all([Farge, Gpu, Cpu, Ram]):
        flash("Vennligst velg en av alle komponentene!")
        return redirect(url_for("bestilling"))
    return render_template("Conf1.html", Ram=valgtRam, Cpu=valgtCpu, Gpu=valgtGpu, Farge=Farge)



if __name__ == "__main__":
    app.run(debug=True)
    