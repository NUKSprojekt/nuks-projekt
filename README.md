## nuks-projekt
Single-page-application for rating restaurants

## About
Na glavni strani spletne aplikacije je seznam vseh restavracij s povprečnimi ocenami hrane, ambienta, osebja, postrežbe, cene ter končna skupna ocena restavracije. Drop down menu zgoraj nam omogoča podrobnejši prikaz ocen posameznih restavracij. Odpre se nam seznam vseh ocen, ki so jih vnesli uporabniki, prikazan pa je tudi komentar, ki ga je uporabnik podal za določeno restavracijo.
Desno zgoraj najdemo tipko Add Rating, prek katere oddamo oceno restavracije. V drop down menu-ju izberemo restavracijo, ki jo želimo oceniti, nato izpolnimo vprašalnik ter oceno oddamo. Oddana ocena se bo prikazala med ocenami restavracije ter se prištela k povprečnim ocenam na glavni strani.
Ob vsakem obisku glavne strani se izvede funkcija za iskanje neprimernih komentarjev. Če komentar vsebuje besede, ki so v funkciji označene kot neprimerne, podan komentar zamenja komentar "Comment was deleted for inappropriateness."

## Project setup
```
sudo docker compose build
```
```
sudo docker compose up
```
