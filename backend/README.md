# backend

## About
- Description: APIs for single-page-application for rating restaurants

## API:
- get API za izpis vseh restavracij in pripadajočih povprečnih ocen
- get API za izpis posameznih restavracij in pripadajočih ocen uporabnikov
- post API za oddajo ocene uporabnika
- put API za brisanje neprimernih komentarjev
- post, delete API-ja za dodajanje in brisanje restavracij
- delete API za brisanje ocen

## Database:
- tabela kamor se zapisujejo vse ocene
- tabela, kjer so zapisane vse restavracije (tabela vezana na prvo tabelo)

## Development and testing:
- Set up developing enviroment (only the first time):
```
pyenv local 3.11.2
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Development:
Activating virtual enviroment:
```
source .venv/bin/activate
```
Deactivating:
```
deactivate
```
Run:
```
uvicorn main:app --reload --host 0.0.0.0
```