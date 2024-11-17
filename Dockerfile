# Image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY app.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut pour exécuter le programme
CMD ["python", "app.py"]
