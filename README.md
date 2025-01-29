![GitHub Repo stars](https://img.shields.io/github/stars/votre-repo.svg?style=flat)
![GitHub forks](https://img.shields.io/github/forks/votre-repo.svg?style=flat)
![License](https://img.shields.io/github/license/votre-repo.svg?style=flat)
LinkedIn Auto Unfollow & Unconnect 🚀
Scripts d'automatisation pour se désabonner et supprimer des connexions sur LinkedIn.

📌 Fonctionnalités :
✔️ Se désabonner (unfollow) automatiquement de tous les comptes sur LinkedIn
✔️ Supprimer des connexions (unconnect) automatiquement avec exclusion d'une liste définie
✔️ Défilement automatique pour charger toutes les connexions et abonnements
✔️ Ralentissement du script pour éviter la détection LinkedIn
✔️ Compatible macOS, Windows et Linux

⚠️ Attention : L’automatisation sur LinkedIn peut violer ses CGU. Utilisation à vos propres risques.

📜 Installation et Pré-requis
1️⃣ Pour le script Unfollow (JS)
📌 Pré-requis
Google Chrome recommandé.
🚀 Utilisation
Ouvrez LinkedIn et accédez à la page "Gérer mes abonnements" :
🔗 Lien direct
Ouvrez la console du navigateur :
Windows/Linux : Ctrl + Shift + J
macOS : Cmd + Option + J
Copiez-collez le script unfollow.js et appuyez sur Entrée.
2️⃣ Pour le script Unconnect (Python + Selenium)
📌 Pré-requis
Installer Python (si ce n’est pas déjà fait) :

macOS/Linux :
bash
Copier
Modifier
brew install python
Windows :
Téléchargez Python ici.
Installer les dépendances :

bash
Copier
Modifier
pip install selenium
Installer ChromeDriver (nécessaire pour Selenium) :

macOS (Apple Silicon & Intel) :
bash
Copier
Modifier
brew install chromedriver
Windows/Linux : Télécharger ChromeDriver ici et ajoutez-le au PATH.
🚀 Utilisation
Clonez ce dépôt :
bash
Copier
Modifier
git clone https://github.com/votre-repo/linkedin-unconnect.git
cd linkedin-unconnect
Ajoutez les personnes à exclure dans excluded_list.txt (1 nom par ligne).
Lancez le script :
bash
Copier
Modifier
python3 linkedin_unconnect.py
Suivez les instructions et laissez le script nettoyer votre réseau !
📜 Structure du projet
bash
Copier
Modifier
📂 linkedin-auto-cleanup
│── 📜 README.md            # Documentation du projet
│── 📜 unfollow.js          # Script JS pour se désabonner
│── 📜 linkedin_unconnect.py # Script Python pour supprimer des connexions
│── 📜 excluded_list.txt    # Liste des personnes à exclure
🔍 Configuration de la Liste d'Exclusion
Avant d’exécuter linkedin_unconnect.py, ouvrez excluded_list.txt et ajoutez les noms des personnes que vous ne voulez PAS supprimer (1 nom par ligne) :

Copier
Modifier
John Doe
Jane Smith
Michael Jordan
Le script utilisera cette liste et conservera ces connexions.

⚠️ Avertissements et Précautions
🚨 L'utilisation excessive de ces scripts peut entraîner une suspension temporaire de votre compte LinkedIn.
⛔ N’exécutez pas ces scripts plusieurs fois par jour.
📌 Il est recommandé de tester sur un petit nombre de connexions avant d’exécuter le script en masse.
✅ Ne partagez pas vos identifiants LinkedIn avec ce script sur des machines non sécurisées.
📝 Licence
Ce projet est sous licence MIT. Vous pouvez l’utiliser, le modifier et le distribuer librement.

📩 Contact
Problèmes ? Ouvrez une issue sur GitHub !
Améliorations ? Faites un fork et proposez une PR !
🎯 Objectif de ce projet
L’objectif de ce projet est d’offrir une solution simple et automatisée pour gérer son réseau LinkedIn efficacement. Soyez responsable dans l'utilisation de ces scripts.

🚀 Contributions
Les contributions sont les bienvenues ! Ajoutez de nouvelles fonctionnalités en respectant les bonnes pratiques de développement.

