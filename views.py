"""
1. Fisierul views.py - cuprinde toate paginile mai putine cele de logare/delogare
2. Aveti mai jos un exemplu de pagina -  home 
3. Pagini ce trebuie implementate:
     - home
     - person_view: pagina pe care se vor afisa informatiile despre persoana ceruta 
        * aici sa tinem cont ca in functie de statutul cu care te loghezi poti vedea unele info sau pe toate
     - (lasam pe mai incolo) statistic_view: o pagina pe care vom afisa statistici despre persoane (exemplu - cate persoane sunt anul 1)
     - attendance (o pagina in care heads vor face prezenta la sedinta)
     - admin: de aici poti adauga/sterge/modifica info despre persoane

*trebuie sa tinem cont ce pagini au nevoie de @login.required si care nu au nevoie
"""

from flask import Blueprint, render_template
from flask import request
from models import database_members

views = Blueprint('views', __name__)


@views.route('/', methods = ['GET', 'POST'])
def home():

    # atentiune aici, cand logam un viewer si cand logam un admin

    return render_template("home.html") # aici se face conexiunea cu front-end-ul

@views.route('/single_view', methods = ['GET', 'POST'])
def single_view():

    # aici for fi functionalitatile paginii

    return render_template("single_view.html")


@views.route('/multiple_view', methods = ['GET', 'POST'])
def multiple_view():

    # atentiune aici, cand cream un cont de viewer si cand cream un cont de admin

    return render_template("multiple_view.html")


@views.route('/admin/add', methods = ['GET', 'POST'])
def admin_add():
    if request.method == 'POST':
        last_name = request.form.get('Nume')
        first_name= request.form.get('Prenume')
        CNP = request.form.get('CNP')
        series = request.form.get('Serie buletin')
        number= request.form.get('Numar buletin')
        adress=request.form.get('Adresa domiciuliu')
        email=request.form.get('Email')
        phonenumber=request.form.get('Telefon')
        college=request.form.get('Facultate')
        experience= request.form.get('Experienta in EA')
        department= request.form.get('Departament')
        subdepartment= request.form.get('Subdepartament')
        freshers=request.form.get('Pariticipant/Orga Freshers')
        acwo=request.form.get('Pariticipant/Orga AcWo')
        hss=request.form.get('Pariticipant/Orga HSS')
        wintercamp=request.form.get('Pariticipant/Orga WinterCamp')
        drowo=request.form.get('Pariticipant/Orga DroWo')
        alumni=request.form.get('Pariticipant/Orga Alumni')
        rowo=request.form.get('Pariticipant/Orga RoWo')
        aerocamp=request.form.get('Pariticipant/Orga AeroCamp')
        acc=request.form.get('ACC')
        mention=request.form.get('Mentiuni')
        new_row={'Nume':last_name,'Prenume':first_name,'CNP':CNP,'Serie buletin':series,'Numar buletin':number,'Adresa domiciuliu':adress, 'Email':email,'Telefon':phonenumber,'Facultate':college,'Experienta in EA':experience, 'Departament':department,'Subdepartament':subdepartment,'Pariticipant/Orga Freshers':freshers,'Pariticipant/Orga AcWo':acwo,'Pariticipant/Orga HSS':hss,'Pariticipant/Orga WinterCamp':wintercamp,'Pariticipant/Orga DroWo':drowo,'Pariticipant/Orga Alumni':alumni,'Pariticipant/Orga RoWo':rowo,'Pariticipant/Orga AeroCamp':aerocamp,'ACC':acc,'Mentiuni':mention}
        database_members = database_members.append(new_row, ignore_index=True)

        return Response(database_members, status=201)