# 🚀 LinkedIn Auto Cleanup
### **Unfollow & Remove Connections Effortlessly**

![GitHub Repo stars](https://img.shields.io/github/stars/votre-repo.svg?style=flat)
![GitHub forks](https://img.shields.io/github/forks/votre-repo.svg?style=flat)
![License](https://img.shields.io/github/license/votre-repo.svg?style=flat)

![Banner](./banner.png)

Scripts d'automatisation pour **se désabonner** et **supprimer des connexions** sur LinkedIn.  
📌 **Facile à utiliser**, **sécurisé**, et **compatible macOS, Windows et Linux**.

---

## 💌 **Fonctionnalités**
🇸️ **Unfollow (JS)** : Se désabonne automatiquement de tous les comptes sur LinkedIn  
🇸️ **Unconnect (Python + Selenium)** : Supprime les connexions avec une liste d'exclusion  
🇸️ **Défilement automatique** pour charger toutes les connexions et abonnements  
🇸️ **Ralentissement intelligent** pour éviter la détection de LinkedIn  
🇸️ **Facile à installer et exécuter**  

🚨 **Attention : L’automatisation sur LinkedIn peut violer ses CGU. Utilisation à vos propres risques.**

---

## 💜 **Installation et Pré-requis**

### **1️⃣ Unfollow (JavaScript)**
#### **📌 Pré-requis**
- **Google Chrome** recommandé.

#### **🚀 Utilisation**
1. **Ouvrez LinkedIn** et accédez à la page **"Gérer mes abonnements"** :  
   🔗 **[Lien direct](https://www.linkedin.com/feed/following/)**
2. **Ouvrez la console du navigateur** :
   - **Windows/Linux** : `Ctrl + Shift + J`
   - **macOS** : `Cmd + Option + J`
3. **Copiez-collez** le script `unfollow.js` et appuyez sur **Entrée**.

---

### **2️⃣ Unconnect (Python + Selenium)**
#### **📌 Pré-requis**
1. **Installer Python** :
   - macOS/Linux :  
     ```bash
     brew install python
     ```
   - Windows :  
     Téléchargez **[Python ici](https://www.python.org/downloads/)**.

2. **Installer Selenium** :
   ```bash
   pip install selenium
   ```

3. **Installer ChromeDriver** :
   - macOS (Apple Silicon & Intel) :
     ```bash
     brew install chromedriver
     ```
   - Windows/Linux : Télécharger **[ChromeDriver ici](https://chromedriver.chromium.org/downloads)** et ajoutez-le au `PATH`.

#### **🚀 Exécution du script**
1. **Clonez le projet** :
   ```bash
   git clone https://github.com/votre-repo/linkedin-unconnect.git
   cd linkedin-unconnect
   ```
2. **Ajoutez les personnes à exclure** dans `excluded_list.txt` (1 nom par ligne).
3. **Lancez le script** :
   ```bash
   python3 linkedin_unconnect.py
   ```
4. **Suivez les instructions** et laissez le script opérer.

---

## 💌 **Structure du projet**
```
💚 linkedin-auto-cleanup
🏰️ README.md            # Documentation
🏰️ unfollow.js          # Script JS pour se désabonner
🏰️ linkedin_unconnect.py # Script Python pour supprimer des connexions
🏰️ excluded_list.txt    # Liste des personnes à exclure
🏰️ banner.png           # Bannière pour GitHub
```

---

## 🔎 **Configuration de la Liste d'Exclusion**
Ajoutez les noms des personnes à **ne pas supprimer** dans `excluded_list.txt` :

```
John Doe
Jane Smith
Michael Jordan
```

Le script les conservera automatiquement.

---

## ⚠️ **Avertissements et Précautions**
- **🚨 Un usage excessif peut entraîner une suspension de compte LinkedIn.**
- **❌ Évitez d'exécuter ces scripts plusieurs fois par jour.**
- **📌 Testez d'abord sur un petit échantillon de connexions.**
- **🛡️ Ne partagez pas vos identifiants LinkedIn avec ce script sur des machines non sécurisées.**  

---

## 📝 **Licence**
Ce projet est sous **licence MIT**. Vous pouvez l’utiliser, le modifier et le distribuer librement.

---

## 📩 **Contact & Support**
📣 **Problèmes ?** Ouvrez une issue sur GitHub.  
🚀 **Idées d'amélioration ?** Faites un fork et proposez une PR !  

---

## 🎯 **Pourquoi ce projet ?**
L’objectif est d’offrir une solution simple et efficace pour gérer son réseau LinkedIn. **Soyez responsable dans son utilisation.**

---

## 🚀 **Contributions**
Les contributions sont les bienvenues ! Ajoutez des fonctionnalités en respectant les bonnes pratiques.

---

🎉 **Prêt à nettoyer votre réseau LinkedIn ?** Lancez le script et profitez d’un espace optimisé ! 🚀
