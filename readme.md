# RSS Feed Discord Bot

## Description :
Le RSS Feed Discord Bot est un bot Discord qui permet de suivre les flux RSS et de recevoir des notifications sur Discord lorsqu'un nouveau post est publié sur le flux RSS. Par défaut, le bot vérifie le flux RSS toutes les 10 minutes pour le site Space.com.

## Les commandes du bot :
- `!help` : Affiche la liste des commandes du bot. (non implémenté)
- `!stop` : Permet d'arrêter manuellement le bot.
- `!start` : Permet de démarrer manuellement le bot.
- `!status` : Affiche le statut du bot.
- `!ping` : Affiche le ping du bot. 

## Prérequis :
- Python 3.6 ou supérieur
- Un compte Discord
- Un serveur Discord

## Installation :
- Téléchargez le code source du bot Discord RSS Feed.
- Installez les dépendances en utilisant la commande `pip install -r requirements.txt`.
- Créez une application bot sur le portail des développeurs Discord.
- Ajoutez le bot à votre serveur Discord.
- Modifiez le fichier `config.ini` et ajoutez les informations requises.
- Exécutez le fichier `main.py` pour démarrer le bot.

## Dépendances :
### Dépendances intégrées à Python :
- time : La bibliothèque time est utilisée pour gérer les dates et les heures. 
- configparser : La bibliothèque configparser est utilisée pour lire les fichiers de configuration.

### Dépendances à installer :

- discord.py : La bibliothèque Discord.py permet d'interagir avec l'API Discord et de créer des bots Discord en Python.
- feedparser : La bibliothèque feedparser est utilisée pour analyser les flux RSS. Elle permet de récupérer les données des entrées du flux.

Assurez-vous d'installer ces dépendances avant d'exécuter le code. Vous pouvez les ajouter à votre fichier `requirements.txt` en utilisant les commandes suivantes :

```
discord.py
feedparser
```

Ensuite, vous pouvez installer toutes les dépendances en une seule fois en utilisant la commande `pip install -r requirements.txt`.

## Créer une application bot sur le portail des développeurs Discord :
- Rendez-vous sur le portail des développeurs Discord et connectez-vous avec votre compte Discord.
- Cliquez sur "New Application" pour créer une nouvelle application.
- Donnez un nom à votre application et cliquez sur "Create".
- Dans le menu de gauche, cliquez sur "Bot".
- Cliquez sur "Add Bot" pour ajouter un bot à votre application.
- Cliquez sur "Yes, do it!" pour confirmer.
- Cliquez sur "Copy" pour copier le token de votre bot.
- Cliquez sur "OAuth2" dans le menu de gauche.
- Dans la section "Scopes", cochez la case "bot".
- Dans la section "Bot Permissions", cochez la case "Send Messages".
- Cliquez sur "Copy" pour copier le lien d'invitation de votre bot.
- Ouvrez le lien d'invitation dans votre navigateur et sélectionnez votre serveur Discord.
- Cliquez sur "Continue" pour confirmer.
- Cliquez sur "Authorize" pour ajouter le bot à votre serveur Discord.

## Configuration :
Pour configurer le bot, vous devez modifier le fichier `sample.config.ini` et ajouter les informations suivantes :
- `token` : Le token de votre bot Discord.
- `channel_id` : L'ID du salon Discord dans lequel vous souhaitez recevoir les notifications.
- `rss_url` : L'URL du flux RSS que vous souhaitez suivre.
- `check_interval` : L'intervalle de temps entre chaque vérification du flux RSS (en minutes).
- `bot_prefix` : Le préfixe que vous souhaitez utiliser pour les commandes du bot.

Renommez ensuite le fichier `sample.config.ini` en `config.ini`.
Par défaut, le bot vérifie le flux RSS toutes les 10 minutes pour le site Space.com. Si vous souhaitez suivre un autre flux RSS, vous devez modifier les informations dans le fichier `config.ini`. 
Ainsi que modifier le message envoyé par le bot dans le fichier main.py : 
```python
# Send the message to the Discord channel
message = f"**New post on Space.com!**\nTitle: {title}\nLink: {link}\nSummary: {summary}"
await channel.send(message)
```

## Problèmes connus : 
```
WARNING  discord.ext.commands.bot Privileged message content intent is missing, commands may not work as expected.
```

Le message d'avertissement que vous avez reçu indique que l'intention "Privileged message content" est manquante. Cela peut affecter le fonctionnement des commandes dans votre bot.

Pour résoudre ce problème, vous devez activer les intentions : "Privileged Gateway Intents" "PRESENCE INTENT" et "SERVER MEMBERS INTENT" dans le portail des développeurs Discord. Voici comment faire :

- Rendez-vous sur le portail des développeurs Discord et connectez-vous avec votre compte Discord.

- Sélectionnez votre application bot dans la liste des applications.

- Dans le menu de gauche, cliquez sur "Bot".

- Dans la section "Privileged Gateway Intents", activez l'intention "Message Content" en cochant la case correspondante.

- Après avoir activé l'intention, générez un nouveau token pour votre bot en cliquant sur "Generate a New Token". Remplacez l'ancien token dans votre code par ce nouveau token.

- Une fois ces étapes effectuées, redémarrez votre bot et vérifiez si les commandes fonctionnent comme prévu.
