# 📘 Les Pipelines et la Mémoire dans LangChain

## 🧐 Qu'est-ce qu'un Pipeline en IA ?
Un **pipeline IA** est une chaîne de traitements permettant d'organiser et d'automatiser le passage de données d'une étape à une autre. Dans **LangChain**, un pipeline structure le flux d’informations entre différents composants, comme :
- **Les modèles de langage (LLM)** 🧠
- **Les outils (moteurs de recherche, bases de données, API, etc.)** 🛠
- **Les mémoires contextuelles** 💾

Grâce aux pipelines, on peut **construire des agents IA plus intelligents et plus efficaces**.

---

## ⚙️ Comment fonctionne un pipeline LangChain ?
Un pipeline LangChain se compose de plusieurs éléments :
1. **Un modèle de langage** (ex: Mistral, Llama, Falcon)
2. **Un ou plusieurs outils** pour récupérer des données externes (API open-source, vector stores, etc.)
3. **Un mécanisme de mémoire** pour stocker l’historique des interactions

### 🔹 Exemple d'un pipeline basique
```
Utilisateur → [Mémoire] → [LLM] → [Outil de recherche] → [Réponse générée]
```
Chaque étape reçoit des données, les transforme et les transmet à l’étape suivante.

---

## 🔗 Intégration de la Mémoire dans un Agent IA
Par défaut, un LLM ne retient pas le contexte entre deux interactions. **LangChain permet d’ajouter une mémoire** pour :
- **Stocker les conversations passées**
- **Rappeler des informations pertinentes**
- **Rendre les interactions plus naturelles**

### 📌 Types de Mémoires dans LangChain
1. **Mémoire courte** (conversationnelle) : Rappelle les derniers échanges.
2. **Mémoire longue** (vectorielle) : Stocke et retrouve des informations à long terme.
3. **Mémoire basée sur des fichiers** : Sauvegarde les interactions dans une base locale.

---

## 📝 Implémentation d'un Pipeline de Base
Nous allons maintenant créer un **pipeline minimal** en LangChain avec un LLM open-source (**Mistral**) et une mémoire conversationnelle.

### 🏗 Version 1 : Utilisation de l’API de Mistral
```python
from langchain.llms import MistralAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os

# Définir votre clé API de Mistral (à ajouter dans un fichier .env)
api_key = os.getenv("MISTRAL_API_KEY")
llm = MistralAI(api_key=api_key)

# Création de la mémoire
memory = ConversationBufferMemory()

# Construction du pipeline
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# Test du pipeline
print(conversation.predict(input="Bonjour, qui es-tu ?"))
print(conversation.predict(input="Peux-tu me rappeler ce que je viens de dire ?"))
```

### 🏗 Version 2 : Utilisation du modèle en local
#### 📥 Télécharger Mistral 7B GGUF
Avant de pouvoir l'utiliser localement, il faut télécharger le modèle via Hugging Face. Pour simplifier cela, nous avons ajouté un fichier `download_models.py`, qui permet de télécharger automatiquement tous les modèles nécessaires.

Exécutez la commande suivante pour télécharger le modèle localement :
```bash
python -m src.utils.download_models
```

#### 🔹 Code pour exécuter le modèle en local
```python
from langchain.llms import CTransformers
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Initialisation du modèle local Mistral 7B GGUF
llm = CTransformers(model="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

# Création de la mémoire
memory = ConversationBufferMemory()

# Construction du pipeline
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# Test du pipeline
print(conversation.predict(input="Bonjour, qui es-tu ?"))
print(conversation.predict(input="Peux-tu me rappeler ce que je viens de dire ?"))
```

---

## ✅ Explication du Code
- **Version API** : Utilise l’API Mistral avec une clé API.
- **Version Locale** : Télécharge un modèle **open-source** et l’exécute localement via `CTransformers`.
- **Utilisation de `download_models.py`** : Ce script permet de récupérer les modèles automatiquement, évitant les téléchargements manuels.
- On ajoute une **mémoire conversationnelle** pour conserver le contexte.
- On crée une **chaîne de conversation** (`ConversationChain`) pour gérer l’interaction.
- Lorsqu’on pose une question, la mémoire permet au LLM de **se souvenir du contexte**.

---

## 🔥 Mise à Jour de `main.py`
Pour intégrer et tester le pipeline au démarrage du projet, nous avons mis à jour `main.py` afin qu'il exécute un test du modèle lors de l'initialisation.

Exécutez :
```bash
python -m src.main
```
Cela affichera un message indiquant que le pipeline fonctionne correctement et montrera la réponse du modèle.

---

## 🚀 Prochaine Étape
Dans le prochain cours, nous verrons **comment créer et gérer des agents IA avancés** avec LangChain et CrewAI.

💡 **Prêt à concevoir des agents intelligents ?** 👉 Direction `03_agents.md` !