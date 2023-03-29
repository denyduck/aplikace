from app.auth.importy import *



## REGISTRACE
@auth_bp.route("/registrace/", methods=['GET', 'POST'])
def registrace():
    # Pokud je uživatel již přihlášen, přesměrovat na hlavní stránku plus flash
    if current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    # Získání dat z formuláře
    form = RegForm()
    if form.validate_on_submit():
        # Kontrola, zda uživatel již existuje
        existing_user = Uzivatele.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash("Uživatel s tímto jménem již existuje. Zvolte prosím jiné jméno.", "danger")
            return redirect(url_for("auth.registrace"))
        # Přidat uzivatele do databaze a zasifrovat mu heslo
        new_user = Uzivatele(
            username=form.username.data,
            password=generate_password_hash(form.password.data)
        )
        # Přidání nového uživatele do session a uložení do databáze
        db.session.add(new_user)
        db.session.commit()
        # flash a přesměrování
        flash("Registrace proběhla úspěšně. Nyní se můžete přihlásit.", "success")
        return redirect(url_for("auth.login"))
    # získání hodnoty proměnné is_authenticated
    is_authenticated = current_user.is_authenticated
    # pokud není validní vráti registraci
    return render_template("registrace.html", form=form, is_authenticated=is_authenticated)
#---------------------------------------------------------------------------------------------------
##REGISTRACE
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # pokud je uživatel již přihlášen přesměrovat a vypsat flash o prihlaseni
    if current_user.is_authenticated:
        return redirect(url_for("main.homepage"))
    form = LogForm()
    if form.validate_on_submit():
        # Získání uživatele z databáze
        user = Uzivatele.query.filter_by(username=form.username.data).first()
        # Kontrola, zda uživatel existuje a zda se hesla shodují
        if user is None or not check_password_hash(user.password, form.password.data):
            flash("Nesprávné jméno nebo heslo.", "danger")
            return redirect(url_for("auth.login"))
        # Přihlášení uživatele
        login_user(user)
        flash("Přihlášení proběhlo úspěšně.", "success")
        return redirect(url_for("inside_bp.plocha"))
    return render_template("login.html", form=form)
#---------------------------------------------------------------------------------------------------------
##ODHLÁŠENÍ
@auth_bp.route('/homepage')
def odhlasit():
    logout_user()
    return render_template("homepage.html")

