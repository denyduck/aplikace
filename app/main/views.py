from flask import render_template
from app.main import main_bp



@main_bp.route("/")
def homepage():
    return render_template("homepage.html")

@main_bp.route("/kontakt")
def contact():
    return render_template("kontakt.html")

@main_bp.route("/o_projektu")
def about():
    return render_template("o_projektu.html")

@main_bp.route("/pojisteni")
def pojisteni():
    return render_template("pojisteni.html")

@main_bp.route("/odpovednosti")
def odpovednosti():
    return render_template("odpovednosti.html")

@main_bp.route("/vozidla")
def vozidla():
    return render_template("vozidla.html")

@main_bp.route("/zivota")
def zivota():
    return render_template("zivota.html")

@main_bp.route("/majetku")
def majetku():
    return render_template("majetku.html")
