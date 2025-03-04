import os
import subprocess

def download_mistral():
    """ Télécharge le modèle Mistral 7B GGUF depuis Hugging Face. """
    model_url = "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
    model_path = "models/mistral/"
    os.makedirs(model_path, exist_ok=True)
    output_file = os.path.join(model_path, "mistral-7b-instruct-v0.1.Q4_K_M.gguf")
    
    if not os.path.exists(output_file):
        print(f"📥 Téléchargement de Mistral 7B GGUF en cours...")
        subprocess.run(["wget", "-O", output_file, model_url], check=True)
        print("✅ Modèle téléchargé avec succès !")
    else:
        print("✅ Modèle déjà téléchargé.")

def main():
    print("🔹 Initialisation du téléchargement des modèles...")
    download_mistral()
    print("✅ Tous les modèles sont prêts !")

if __name__ == "__main__":
    main()
