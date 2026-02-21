from fastapi import FastAPI #importam libraria FastAPI
from app.database.connection import engine, Base, SessionLocal 
from app.models import transaction

from fastapi import Depends # cerem o conexiune la baza de date doar atunci cand este nevoie
from sqlalchemy.orm import Session
from app.schemas.transaction import TransactionCreate, TransactionResponse

Base.metadata.create_all(bind=engine) # pt a crea fisierul .db

app = FastAPI() #am creat o aplicatie care va fi pornita live pe un server cu comanda din terminal fastapi dev main.py

def get_db():
    db = SessionLocal() # creez o sesiune
    try:
        yield db # trimit conexiunea functiei de create
        # se executa functia de POST
    finally:
        db.close() # dupa ce utilizatorul a introdus datele, acestea au fost verificate si a primit un raspuns, sesiunea se inchide

@app.post("/transaction") # destinatia unde utilizatorul trimte datele
def create_transaction(transaction: TransactionCreate, db : Session = Depends(get_db)): # apeleaza functia get_db pt a porni sesiunea
    new_item = transaction( # creez un rand nou pe care vreau sa o introduc in tabel
        titlu=transaction.titlu,
        suma=transaction.suma,
        categorie=transaction.categorie
    )
    
    db.add(new_item) # adaug in sesiune operatiunea
    db.commit() # o salvez
    db.refresh(new_item)
    return new_item # o returnez utilizatorului



@app.get("/") #este un decorator specific fastapi, identifica ruta "/" (principala) 
async def root(): #o functie asincrona, poate gestiona sute de cereri in ac timp fata de sync.
                  # Functia se numeste root pt ca e ruta principala, este o conventie de nume, poate fi
                  # numita oricum
    return {"message": "Hello Yari"} 


# am creat un fisier de tipul .gitignore pentru a pune acolo fiserele care trebuiesc ignorate 
# (nu le incarcam pe git)
# cu pip freeze > am facut un fiser de tip txt in care am adaugat ce este necesar pt venv


