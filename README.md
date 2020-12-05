# Installation

Clonez le dépôt et rentrez dedans:
```
git clone git@github.com:Pakopac/tweet-api.git
cd tweet-api/
```

Télécharger le fichier csv et l'inclure dans le dossier: https://drive.google.com/file/d/1OEWrVjE7B2d23-eQrTMcJpRJMxoB6iUH/view

Installez les dépendances:
```
npm install requirements.txt
```
Enfin lancez la commande:
```
flask run
```

# GET /training

:warning: Il n'est pas nécessaire de lancer l'algorithme de training pour la prédiction car le fichier est déjà crée cependant vous pouvez quand même le lancer en faisant une requête GET sur http://localhost:5000/training (il faudra patienter un moment)

# POST /predict

Pour faire une prédiction sur l'algorithme vous pouvez faire une requête POST sur http://localhost:5000/predict avec un body json de la forme:
```
{
    "text": "Hello, I'm john"
}
```
et l'algorithme vous retournera hate speech, offensive language ou neither selon le texte entré

