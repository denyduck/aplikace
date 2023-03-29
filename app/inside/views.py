from flask import render_template, flash, redirect, url_for, get_flashed_messages
from app.inside import inside_bp
from app.inside.forms import KlientiForm, PojisteniForm
from app import db
from app.models import Klienti, Pojisteni
from flask_login import current_user, login_required
from app.models import Uzivatele
from app.inside.utils import (
    add_client,
    add_policy,
    views,
    soucet_klientu,
    soucet_pojisteni,
    klient_s_pojistenim,
    pojistka_bez_klienta,
   # klienti_bez_pojisteni,
    pojistka_s_klientem
)


@inside_bp.route("/plocha")
def plocha():
    #klienti
    klienti_celkem = soucet_klientu()
  #  klient_bez_pojisteni = klienti_bez_pojisteni()
    klienti_s_pojistenim = klient_s_pojistenim()
    #pojistky
    pojistky_celkem = soucet_pojisteni()
    pojistky_bez_klienta = pojistka_bez_klienta()
    pojistky_s_klientama = pojistka_s_klientem()

    return render_template("plocha.html",
                           #klienti
                           klienti_celkem = klienti_celkem,
                          # klient_bez_pojisteni=klient_bez_pojisteni,
                           klienti_s_pojistenim=klienti_s_pojistenim,
                           #pojistky
                           pojistky_celkem = pojistky_celkem,
                           pojistky_bez_klienta = pojistky_bez_klienta,
                           pojistky_s_klientama = pojistky_s_klientama)
#------------------------------------------------------------------
@inside_bp.route("/vlozit_klienta", methods=["GET", "POST"])
def vlozit_klienta():
    return add_client()
#-------------------------------------------------------------------
@inside_bp.route("/vlozit_pojisteni", methods=["GET", "POST"])
def vlozit_pojisteni():
    return add_policy()
#------------------------------------------------------------------
@inside_bp.route("/zobrazit", methods=["GET", "POST"])
@login_required
def zobrazit():
    klienti, pojisteni = views()

    return render_template("zobrazit.html",
                           klienti=klienti,
                           pojisteni=pojisteni)
#------------------------------------------------------------------
@inside_bp.route("/seznam_klientu", methods=["GET", "POST"])
def seznam_klientu():
    klienti, pojisteni = views()
    return render_template("seznam_klientu.html",
                           klienti=klienti)
#------------------------------------------------------------------
@inside_bp.route("/seznam_pojisteni", methods=["GET", "POST"])
def seznam_pojisteni():
    klienti, pojisteni = views()
    return render_template("seznam_pojisteni.html",
                           pojisteni=pojisteni,
                           klienti=klienti)
#-------------------------------------------------------------------
