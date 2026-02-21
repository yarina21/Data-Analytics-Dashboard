from sqlalchemy import create_engine # stabileste conexiunea fizica intre codul Python si baza de date; fara create engine python nu are calea de 
                                     # acces catre dadef create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):te
from sqlalchemy.ext.declarative import declarative_base # traduce codul din python in limbaj sql
from sqlalchemy.orm import sessionmaker # folosita pt a grupa operatiuni intr o singura sesiune


URL_BAZA_DATE = "sqlite:///./wealth.db" # unde se afla baza de date, sqlite este protocolul care stocheaza baza de date local, / - calea relativa,
                                        # . - folder ul curent si /wealth.db numele fiserului pe care l creeaza daca nu exista deja

engine = create_engine(URL_BAZA_DATE) # creez motorul care face legatura

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # creez o sesiune care va fi folosita pentru a face operatiuni pe baza de date

Base = declarative_base() # clasa de baza din care voi crea tabele in baza de date, folosind mostenirea, fiecare tabela va fi o clasa care mosteneste de la Base    