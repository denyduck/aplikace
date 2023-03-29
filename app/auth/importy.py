from flask import render_template, flash, url_for, redirect,session
from flask_login import current_user, login_user, logout_user, login_required
from app.auth import auth_bp
from app.auth.forms import RegForm, LogForm
from app.models import Uzivatele
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

