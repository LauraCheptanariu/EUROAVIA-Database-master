"""
1. Fisierul model.py al programului -  aici dam forma bazei de date ce sta in spatele web app-ului
2.  Avand in vedere ca lucram cu SQLAlchemy, informatia pe care o punem in aceasta baza de date
trebuie sa fie una tabelata. Asa ca, pentru a intelege ce se intampla mai jos, trebuie sa va imaginati un tabel
numit Person, ce are urmatoarele coloane: id, name, department. 
3. Ce facem aici nu este sa cream tabelul, ci mai degraba sa cream matrita (capul de tabel) pe care vom lucra
4. De modificat: 
    - trebuie sa primim de la dept Legal un tabel cu toate info despre persoane si vom adauga aici 
    atributele (coloanele) respective (class Person)
    - class Admin (conturile pentru admini - ei pot sa editeze info)
    - class Viewer (conturile pentru cei care pot sa vada info, dar nu sa le editeze)

** formatul unei coloane este de genul: x = db.Column(db.String(nr maxim de caractere)) sau 
 x = db.Column(db.Integer); acestea sunt cele mai comune. Pentru mai multe info, consultati doc SQLAlchemy
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_login import UserMixin
from sqlalchemy.sql import func
import pandas as pd

db = SQLAlchemy()
DB_NAME = "baza.db"

# data = pd.read_excel('database.xlsx',index_col=None)
# database_members = pd.DataFrame(data, columns=['Nume', 'Prenume','CNP','Serie buletin', 'Numar buletin','Adresa domiciliu','Email','Telefon','Facultate','Experienta in EA','Departament','Subdepartament','Pariticipant/Orga Freshers','Pariticipant/Orga AcWo','Pariticipant/Orga HSS','Pariticipant/Orga WinterCamp','Pariticipant/Orga DroWo','Pariticipant/Orga Alumni','Pariticipant/Orga RoWo','Pariticipant/Orga AeroCamp','ACC','Mentiuni'])
# database_members=database_members.fillna('')

class Person():
    id = db.Column(db.String(150), primary_key = True) #toate clasele pe care le cream aici incep cu id
    last_name = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    CNP = db.Column(db.Integer())
    series =db.Column(db.String(150))
    number =db.Column(db.Integer())
    adress =db.Column(db.String(150))
    email =db.Column(db.String(150))
    phonenumber =db.Column(db.String(150))
    college = db.Column(db.String(150))
    experience = db.Column(db.String(150))
    department = db.Column(db.String(150))
    subdepartment = db.Column(db.String(150))
    freshers = db.Column(db.String(150))
    acwo = db.Column(db.String(150))
    hss = db.Column(db.String(150))
    wintercamp = db.Column(db.String(150))
    drowo = db.Column(db.String(150))
    alumni = db.Column(db.String(150))
    rowo = db.Column(db.String(150))
    aerocamp = db.Column(db.String(150))
    acc = db.Column(db.String(150))
    mention = db.Column(db.String(150))

    """
    metoda __init__ da niste valori standard obiectelor pe care le cream in cazul in care acestea nu sunt pasate de catre noi

    """

    def __init__(self, name= 'Nume', departament= 'niciunul'): 
        self.name = name                                      
        self.departament = departament


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) #toate clasele pe care le cream aici incep cu id
    username = db.Column(db.String(150), unique=True)
    password1 = db.Column(db.String(150))
    password2 = db.Column(db.String(150))
    user_credentials = db.Column(db.String(150))


class Viewer(db.Model):
    id = db.Column(db.Integer, primary_key = True) #toate clasele pe care le cream aici incep cu id
