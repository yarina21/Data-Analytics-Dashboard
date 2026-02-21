from fastapi import FastAPI #importam libraria FastAPI

app = FastAPI() #am creat o aplicatie care va fi pornita live pe un server cu comanda din terminal fastapi dev main.py


@app.get("/") #este un decorator specific fastapi, identifica ruta "/" (principala) 
async def root(): #o functie asincrona, poate gestiona sute de cereri in ac timp fata de sync.
                  # Functia se numeste root pt ca e ruta principala, este o conventie de nume, poate fi
                  # numita oricum
    return {"message": "Hello Yari"} 

# am creat un fisier de tipul .gitignore pentru a pune acolo fiserele care trebuiesc ignorate 
# (nu le incarcam pe git)
# cu pip freeze > am facut un fiser de tip txt in care am adaugat ce este necesar pt venv
