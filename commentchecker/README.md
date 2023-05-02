## FaaS
## About
Funkcija za brisanje neprimernih komentarjev.
Algoritem se sprehodi čez besede komentarjev ter preveri, če so prisotne neprimerne besede. V primeru neprimernih besed funkcija namesto komentarja vrne komentar "Comment was deleted for inappropriateness.".

## Project setup
- Building image, pushing to DockerHub and deployment
```
faas-cli build -f commentchecker.yml
sudo faas-cli push -f commentchecker.yml
faas-cli deploy --image username/commentchecker --name commentchecker
```