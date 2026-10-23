from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)
app.secret_key = "1991"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Bestilling")
def bestilling():
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
    ram = [
        {"Navn": "8gb", "pris": 1500},
        {"Navn": "16gb", "pris": 2500},
        {"Navn": "24gb", "pris": 4000},
        {"Navn": "32gb", "pris": 7000},
        {"Navn": "64gb", "pris": 12000},
    ]
    return render_template("Bestilling.html", Farge=Farge, ram=ram, Cpu=Cpu, Gpu=Gpu)

@app.route("/Confirmation1", methods=["POST"])
def Conf1():
    Farge = request.form.get("Farge")
    Gpu = request.form.get("Gpu")
    Cpu = request.form.get("Cpu")
    ram = request.form.get("ram")
    if "0" in (Farge, Gpu, Cpu, ram) or not all([Farge, Gpu, Cpu, ram]):
        flash("Vennligst velg en av alle komponentene!")
        return redirect(url_for("bestilling"))
    print(Gpu)
    print(ram)
    return render_template("Conf1.html", ram=ram, Cpu=Cpu, Gpu=Gpu, Farge=Farge)



if __name__ == "__main__":
    app.run(debug=True)
    