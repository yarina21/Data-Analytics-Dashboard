from pydantic import BaseModel, Field # BaseModel e folosit pentru a verifica datele primite de la utilizator si a le valida
                                      # Field e folosit pentru a adauga constrangeri

# Schema pentru input ul de la utilizator, acesta trimite un JSON (JAVASCRIPT Object Notation) folosit pentru a trimite date intr o aplicatie web si server
class TransactionCreate(BaseModel):
    titlu: str = Field(min_length = 3, description = "Numele tranzactiei")   
    suma: float = Field(gt=0, description="Suma trebuie sa fie pozitiva") # gt vine de la greater than 
    categorie : str

# Schema pentru ce trimite server ul (output ul)
class TransactionResponse(TransactionCreate): # backend ul primeste datele si le salveaza in SQLite, baza de date genereaza automat un ID.
    id: int                                   # TransactionResponse este pachetul pe care l trimit utilizatorului

    class Config:                             # pentru a putea trimite inapoi catre utilizator rezultatul ne folosim de from_attributes pentru a
        from_attributes = True                # transforma dintr-un obiect in JSON
