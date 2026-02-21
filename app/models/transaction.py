from sqlalchemy import Column, Integer, String, Float # importam coloanele pt a defini structura tabelului si tipurile de date
from app.database.connection import Base # Importăm matrița de la Pasul 1 pentru a crea tabele

class Transaction(Base): # dupa clasa de baza creez un tabel Transaction
    __tablename__ = "transactions" # numele tabelului în baza de date

    id = Column(Integer, primary_key=True, index=True) # id ul este o coloana cu valori int si care are cheie primara
    titlu = Column(String) # titlul este o coloana de tin string
    suma = Column(Float) # suma este o coloana de tip float
    categorie = Column(String) # ex: "Salariu", "Mâncare", "Investiții"