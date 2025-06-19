# 🎲 SmartRPG – Table Connectée pour Jeu de Rôle Immersif

> Projet réalisé dans le cadre du cours *INFOM453 – Informatique ambiante et mobile* à l’Université de Namur (2023–2024)

## 🧭 Objectif du projet

Concevoir une **table de jeu de rôle connectée** capable d’enrichir l’expérience immersive des joueurs et de faciliter la tâche du maître du jeu (MJ) grâce à des interactions physiques tangibles, des effets sonores, lumineux et une interface réactive.

---

## 🧙 Contexte

- **Persona ciblé** : Un MJ passionné souhaitant optimiser la mise en place et la gestion de ses parties.
- **Environnement** : Reprise d’une table interactive existante (ancienne installation muséale), enrichie par des objets connectés.
- **Contraintes techniques** : Faible puissance de calcul (Raspberry Pi), multi-modularité, autonomie de l’utilisateur final.

---

## 🛠️ Composants techniques

### ⚙️ Architecture matérielle

- 2x **Raspberry Pi** (communication via MQTT)
- **Table connectée** en MDF + plexiglas semi-transparent
- **Mini-projecteur** interne (projection de la carte)
- **LEDs RGB** (effets lumineux selon l’ambiance ou les événements)
- **Coffre et clés RFID** (une seule clé ouvre le coffre)
- **Dés connectés GoDice** (Bluetooth)
- **Livre et baguette** connectés (interrupteur capacitif pour changer d’ambiance)
- **Baffles** (ambiance sonore)

### 🧬 Architecture logicielle

- **Python** (langage principal)
- **Modèle acteur** avec `pykka`
- **MQTT** (via `paho-mqtt`) pour la communication inter-Raspberry
- **Processing** + `pygame` pour l'affichage dynamique de la carte
- **Bluetooth** via `bleak`, `godice` pour les dés
- **GPIO** via `RPi.GPIO` et `Phidget22`
- **Libs LED** : `board`, `neopixel`

---

## ✨ Fonctionnalités

| Élément               | Fonction                                                                 |
|------------------------|--------------------------------------------------------------------------|
| **Livre + baguette**   | Changement d’ambiance (carte, LEDs, sons) via contact physique           |
| **Clés RFID + coffre** | Interaction ludique pour "déverrouiller" le coffre                      |
| **Dés connectés**      | Déclenchement d’événements spéciaux (critiques, échecs)                  |
| **LED RGB**            | Couleurs dynamiques selon l’ambiance ou les actions                      |
| **Audio synchronisé**  | Sons de forêt, volcan, etc. en fonction du décor                         |
| **Projection carte**   | Dynamique, changeante selon les événements ou l’interaction du MJ        |

---

## 🚀 Installation

### Prérequis

- Raspberry Pi OS avec Python 3.x
- `mosquitto` installé si besoin d'un broker MQTT local
- Paquets Python à installer :
```bash
pip install pykka paho-mqtt pygame board neopixel bleak asyncio godice RPi.GPIO Phidget22
```

### Démarrage du système

1. Cloner le dépôt :
```bash
git clone https://github.com/carbonnm/Labo-Ambiante-Mobile.git
```
2. Lancer le serveur principal (`main.py`) sur le Pi contrôleur
3. Lancer les scripts liés au livre et à la baguette sur le second Pi
4. Vérifier la connexion MQTT, Bluetooth, GPIO
5. Interagir via les objets tangibles

---

## 🧪 Démo

---

## 🔄 Évolutions possibles

- Ajout d'un système bancaire détectant les pièces
- Détection automatique de la position des pions via caméra + reconnaissance d'image
- Modularité avancée avec map en tuiles
- Affichage des caractéristiques des personnages
- LEDs adressables individualisées par joueur
