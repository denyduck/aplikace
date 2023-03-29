from flask import render_template, flash, redirect, url_for, get_flashed_messages
from app.inside.forms import KlientiForm, PojisteniForm
from app import db
from app.models import Uzivatele,Klienti,Pojisteni, KlientiPojisteni
from flask_login import current_user



## Z FORMULARE Z WEBU VLOZI NOVEHO KLIENTA DO DATABAZE
def add_client():
    form = KlientiForm()
    if form.validate_on_submit():
        new_client = Klienti(
            uzivatel_id=current_user.id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            birth_year=form.birth_year.data,
            street=form.street.data,
            city=form.city.data,
            postal_code=form.postal_code.data
        )
        # Přidání nového klienta do databáze
        db.session.add(new_client)
        db.session.commit()
        # flash a přesměrování
        flash("Klient byl úspěšně vložen do databáze", "success")
        flash("Nyní můžete klientovi vytvořit pojištění", "info")
        return redirect(url_for("inside_bp.vlozit_klienta"))
    return render_template("vlozit_klienta.html", form=form, messages=get_flashed_messages(with_categories=True))
#-----------------------------------------------------------------------------------------------------------------
## Z FORMULARE Z WEBU VLOZI NOVE POJISTENI DO DATABAZE
def add_policy():
    form = PojisteniForm()
    if form.validate_on_submit():
        #vytvori nove pojisteni s id
        new_policy = Pojisteni(
            uzivatel_id=current_user.id,
            druh=form.druh.data,
            pojistovna=form.pojistovna.data,
            pojistna_castka=form.pojistna_castka.data
        )
        # Přidání nového klienta do databáze
        db.session.add(new_policy)
        db.session.commit()
        # flash a přesměrování
        flash("Pojištění bylo úspěšně přidáno do databáze", "success")
        return redirect(url_for("inside_bp.vlozit_pojisteni"))
    return render_template("vlozit_pojisteni.html", form=form, messages=get_flashed_messages(with_categories=True))
#------------------------------------------------------------------------------------------------------------------
# VRATI DATA POKUD NEJAKA UZIVATEL MA, JINAK ZOBRAZIT FLASH

def valid():
    uzivatel_id = current_user.id
    uzivatel = Uzivatele.query.get(uzivatel_id)
    if uzivatel.id == uzivatel_id:
        return uzivatel
    else:
        return render_template('homepage.html')

#--------------------------------------------------------------------------------------------------------
#VRATIT PRIHLASENEMU JEHO KLIENTY A POJISTENI POKUD JSOU K DISPOZICI
def views():
    uzivatel = valid()
    if uzivatel:
        klienti = Klienti.query.all()
        pojisteni = Pojisteni.query.all()
        return klienti, pojisteni
    else:
        #vratit dva objekty, a kazdy seznam pro html
        return [], []
#--------------------------------------------------------------------------------------
#VRATI POCET VŠECH VŠECH KLIENTU
def soucet_klientu():
    uzivatel = valid()
    if uzivatel:
        pocet = Klienti.query.count()
        return pocet
    else:
        return 0
#---------------------------------------------------------------------------------------
#VRATIT POCET VSECH POJISTEK
def soucet_pojisteni():
    uzivatel = valid()
    if uzivatel:
        pocet = Pojisteni.query.count()
        return pocet
    else:
        return 0
#----------------------------------------------------------------------------------
#VRATI VSECHYN POJISTKY BEZ KLIENTU
def pojistka_bez_klienta():
    uzivatel = valid()
    if uzivatel:
        id_vsechny_pojistky = Pojisteni.query.with_entities(Pojisteni.id).all()
        id_pojistky_klientu = KlientiPojisteni.query.with_entities(KlientiPojisteni.pojisteni_id).all()
        pocet = list(set(id_vsechny_pojistky) - set(id_pojistky_klientu))
        return len(pocet)
    else:
        return 0
#--------------------------------------------------------------------------------------
#VRATI VSECHNY POJISTKY KTERE MAJI KLIENTA
def pojistka_s_klientem():
    uzivatel = valid()
    if uzivatel:
        pocet = KlientiPojisteni.query.filter(KlientiPojisteni.pojisteni).count()
        return pocet
    else:
        return 0
#-------------------------------------------------------------------------------------
#VRATI VSECHNY KLIENTY MAJICI ALESPON JEDNO POJISTENI
def klient_s_pojistenim():
    uzivatel = valid()
    if uzivatel:
        pocty = KlientiPojisteni.query.distinct(KlientiPojisteni.klient_id).count()
        return pocty
    else:
        return 0
#-------------------------------------------------------------------------------------
#PRIDAT POJISTENI KLIENTOVI
def prirad_pojisteni_klientovi(klient_id, pojisteni_id):
    uzivatel = valid()
    if uzivatel:
        klient = Klienti.query.get(klient_id)
        pojisteni = Pojisteni.query.get(pojisteni_id)
        klient_pojisteni = KlientiPojisteni(klient=klient, pojisteni=pojisteni)
        # pridat do tabulky klient_pojisteni
        db.session.add(klient_pojisteni)
        db.session.commit()
