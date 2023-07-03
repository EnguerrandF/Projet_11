# Projet 11
Améliorez une application Web Python par des tests et du débogage
## Lancer le projet Python_Testing
### 1- Sélectionner la commande Git ci-dessous afin de récupérer le projet:
```
     git clone https://github.com/EnguerrandF/Projet_11.git
```
---
### 2- Accéder au dossier:
```
    cd nom_du_dossier
```
---
### 3- Créer l'environnement virtuel en exécutant la commande ci-dessous:
```
    python -m venv env
```
---
### 4- Activer l'environnement:
* Windows:
```
    env/Scripts/activate
```
* Mac et linux:
```
    source venv/bin/activate
```
---
### 5- Ajoutez-les modules du fichier requirements.txt en executant la commande si dessous:
```
    pip install -r requirements.txt
```
---
### 7- Lancer le serveur flask:
```
    python .\server.py
```
---
### 8- Accéder au site via URL suivante:
- [http://127.0.0.1:5000](http://127.0.0.1:5000)
---
## Test de performance avec Locust
### 1- Lancer le serveur Locust
```
    locust -f .\tests\performance_tests\locustfile.py
```
### 2- Lancer le serveur flask
```
    python .\server.py
```
### 3- Ouvrer la page web de Locust et réaliser le test de performance
- [http://localhost:8089](http://localhost:8089)

