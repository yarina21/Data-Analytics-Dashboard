from fastapi import FastAPI #importam libraria FastAPI
from app.database.connection import engine, Base, SessionLocal 
from app.models.transaction import Transaction

from fastapi import Depends # cerem o conexiune la baza de date doar atunci cand este nevoie
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.schemas.transaction import TransactionCreate, TransactionResponse

import pandas as pd
from fastapi.staticfiles import StaticFiles



Base.metadata.create_all(bind=engine) # pt a crea fisierul .db

app = FastAPI() #am creat o aplicatie care va fi pornita live pe un server cu comanda din terminal fastapi dev main.py

app.mount("/", StaticFiles(directory=".", html=True), name="static")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal() # creez o sesiune
    try:
        yield db # trimit conexiunea functiei de create
        # se executa functia de POST
    finally:
        db.close() # dupa ce utilizatorul a introdus datele, acestea au fost verificate si a primit un raspuns, sesiunea se inchide

@app.post("/transaction") # destinatia unde utilizatorul trimte datele
def create_transaction(transaction: TransactionCreate, db : Session = Depends(get_db)): # apeleaza functia get_db pt a porni sesiunea
    new_item = Transaction( # creez un rand nou pe care vreau sa o introduc in tabel
        titlu=transaction.titlu,
        suma=transaction.suma,
        categorie=transaction.categorie
    )
    
    db.add(new_item) # adaug in sesiune operatiunea
    db.commit() # o salvez
    db.refresh(new_item)
    return new_item # o returnez utilizatorului



# @app.get("/") #este un decorator specific fastapi, identifica ruta "/" (principala) 
# async def root(): #o functie asincrona, poate gestiona sute de cereri in ac timp fata de sync.
#                   # Functia se numeste root pt ca e ruta principala, este o conventie de nume, poate fi
#                   # numita oricum
#     return {"message": "Hello Yari"} 

### acum trebuie sa fac un request de tip GET care sa mi returneze datele din baza de date

@app.get("/transaction", response_model = list[TransactionResponse]) # response_model = list[TransactionResponse] decid ce pleaca
                                                                     # spre utilizator, in cazul meu doar id ul
def get_transactions(db: Session = Depends(get_db)): # apelez functia pentru a deschide o sesiune noua
    transactions = db.query(Transaction).all() # se duce in baza de date si cauta tabelul Transaction din care selecteaza TOT
    return transactions


### request de tip GET pentru a prelua datele si a forma grafice cu ele

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all() # preia toate datele din tabel
    
    if not transactions: # daca nu sunt date retuneaza mesajul de mai jos
        return {
            "balanca_totala": 0.0,
            "repartizare_pe_categorii": {},
            "total_tranzactii": 0
        }
    
    df = pd.DataFrame([ # fac un data frame cu datele respective din tabelul transactions
        {
            "suma" : t.suma, 
            "categorie" : t.categorie
         }
        for t in transactions
    ])
    
    total_general = df["suma"].sum() # calculez suma cheltuita in total
    
    stats_categorii = df.groupby("categorie")["suma"].sum().to_dict() # grupez categoriile si fac suma lor
    
    return {
        "balanta_totala": float(total_general),
        "repartizare_pe_categorii": stats_categorii,
        "total_tranzactii": len(df)
    }

### fac un request de tip DELETE
    
@app.delete("/transaction/{transaction_id}") # ii spun ce tranzactie sa stearga, o identifica dupa id ul ei care e primary key
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)): # ii dau ca parametru transaction_id care este de tip int si creez o noua sesiune
    db_item = db.query(Transaction).filter(Transaction.id == transaction_id).first() # caut tranzactia dupa id si o atribui lui db_item
    
    if not db_item: # daca nu gasesc o tranzactie cu id ul respectiv returnez mesajul de mai jos
        return {"error": "Tranzacția nu a fost găsită"}
    
    db.delete(db_item) # sterg tranzactia
    db.commit()        # salvez in baza de date
    return {"message": f"Tranzacția cu ID {transaction_id} a fost ștearsă."} # returnez mesajul de confirmare a stergerii
    

# am creat un fisier de tipul .gitignore pentru a pune acolo fiserele care trebuiesc ignorate 
# (nu le incarcam pe git)
# cu pip freeze > am facut un fiser de tip txt in care am adaugat ce este necesar pt venv


