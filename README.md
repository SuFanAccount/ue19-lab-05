# ue19-lab-05

## Description
Cette application interroge l'API JokeAPI pour récupérer une blague et l'affiche dans la console.

## Prérequis
- Python 3.7 ou plus
- Docker (optionnel pour exécuter avec un conteneur)

## Installation et exécution

### Méthode 1 : Exécution locale
1. Clonez le repository :
   ```bash
   git clone https://github.com/SuFanAccount/ue19-lab-05.git
   cd ue19-lab-05
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
3. Lancez l'application :
   ```bash
   python app.py

### Méthode 2 : Exécution avec Docker
1. Construisez l'image Docker :
    ```bash
   docker build -t joke-app .
2. Lancez le conteneur :
    ```bash
   docker run --rm joke-app
## Fonctionnalités
Affiche une blague aléatoire tirée de JokeAPI.
