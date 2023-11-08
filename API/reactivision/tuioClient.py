import subprocess


process = subprocess.Popen(["maptile.pde"], stdout=subprocess.PIPE)

while True:
    line = process.stdout.readline()
    if not line:
        break

    # Traitez ici les données TUIO (par exemple, analysez-les et réagissez en conséquence)
    # line contient une ligne de données TUIO

    # Exemple de traitement : affichage des données TUIO
    print("Données TUIO reçues : ", line.strip())

process.terminate()