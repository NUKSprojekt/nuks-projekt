## backend
## About
APIs and database for single-page-application for rating restaurants
### API:
- get API za izpis vseh restavracij in pripadajočih povprečnih ocen
- get API za izpis posameznih restavracij in pripadajočih ocen uporabnikov
- post API za oddajo ocene restavracije
- get API za izpis vseh restavracij
#### API klici, ki niso dostopni preko spletne aplikacije
- get API za izpis vseh ocen
- get API za izpis posamezne ocene
- delete API za brisanje ocen
- put API za urejanje ocen
- get API za izpis posamezne restavracije
- post API za dodajanje restavracije
- delete API za brisanje restavracij

## Database:
- tabela kamor se zapisujejo vse ocene
- tabela, kjer so zapisane vse restavracije (tabela vezana na prvo tabelo)

## Project setup
### Development and testing:
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

## Project setup with Docker
### Building docker image
```
sudo docker build -t nuksvaje-backend .
```