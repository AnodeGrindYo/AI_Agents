import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

USE_API = False  # Changez à True pour utiliser l'API Mistral

if USE_API:
    from langchain.llms import MistralAI
    api_key = os.getenv("MISTRAL_API_KEY")  # Nécessite un fichier .env
    llm = MistralAI(api_key=api_key)
else:
    from langchain.llms import CTransformers
    llm = CTransformers(model="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

# Création de la mémoire
memory = ConversationBufferMemory()

# Construction du pipeline
conversation = ConversationChain(llm=llm, memory=memory)

# Test du pipeline
if __name__ == "__main__":
    print(conversation.predict(input="Bonjour, qui es-tu ?"))
    print(conversation.predict(input="Peux-tu me rappeler ce que je viens de dire ?"))
