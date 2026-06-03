import os
import sys

def publicar_projeto():
    # Define a mensagem do commit
    mensagem = sys.argv[1] if len(sys.argv) > 1 else "Atualização automática do projeto"
    
    print("--- Iniciando automação de publicação ---")
    
    # 1. Adicionar arquivos
    print("-> Adicionando arquivos ao Git...")
    os.system("git add .")
    
    # 2. Commit
    print(f"-> Realizando commit: '{mensagem}'...")
    os.system(f'git commit -m "{mensagem}"')
    
    # 3. Push
    print("-> Enviando para o GitHub (push)...")
    os.system("git push -u origin main")
    
    print("--- Processo concluído com sucesso! ---")

if __name__ == "__main__":
    publicar_projeto()