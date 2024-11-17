import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        "type": "single",  # Choisir le type de blague (single = blague courte)
        "lang": "en",      # Langue de la blague
        "amount": 1        # Nombre de blagues à récupérer
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Vérifie les erreurs HTTP

        joke_data = response.json()
        if joke_data.get("error"):
            print("Erreur dans la récupération de la blague :", joke_data.get("message"))
        else:
            print("Voici une blague :")
            print(joke_data.get("joke", "Aucune blague trouvée."))
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la connexion à l'API :", e)

if __name__ == "__main__":
    print("Bienvenue dans l'application JokeAPI!")
    get_joke()
