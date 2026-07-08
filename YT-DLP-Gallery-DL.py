import os
import subprocess
import sys
import time

# Configurações personalizadas por você
NAVEGADOR_COOKIES = "brave"
PASTA_DESTINO = r"C:\Users\mathe\Pictures\Docs\Baixados\poesia"

def inicializar_pasta():
    """Garante que a pasta de destino existe."""
    os.makedirs(PASTA_DESTINO, exist_ok=True)

def limpar_tela():
    """Limpa o terminal de forma limpa."""
    os.system('cls' if os.name == 'nt' else 'clear')

def baixar_video(link):
    print("\n[+] Buscando vídeo na máxima qualidade (MP4)...")
    comando = [
        "yt-dlp",
        "-P", PASTA_DESTINO,
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        link
    ]
    subprocess.run(comando)

def baixar_audio(link):
    print("\n[+] Extraindo apenas o áudio na máxima qualidade (MP3)...")
    comando = [
        "yt-dlp",
        "-P", PASTA_DESTINO,
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        link
    ]
    subprocess.run(comando)

def baixar_pinterest(link):
    print(f"\n[+] Acessando o Pinterest via cookies do {NAVEGADOR_COOKIES.upper()}...")
    comando = [
        "gallery-dl",
        "-d", PASTA_DESTINO,
        "--cookies-from-browser", NAVEGADOR_COOKIES,
        link
    ]
    subprocess.run(comando)

def main():
    inicializar_pasta()
    
    while True:
        limpar_tela()
        print("==================================================")
        print("       GERENCIADOR DE DOWNLOADS - POESIAS (PY)   ")
        print("==================================================")
        print(f" Salvando em: {PASTA_DESTINO}")
        print(" Navegador para cookies: Brave")
        print("--------------------------------------------------")
        print(" [1] Baixar Video (MP4 - Max Qualidade)")
        print(" [2] Baixar Apenas Audio (MP3 - Max Qualidade)")
        print(" [3] Baixar Pasta ou Imagem do Pinterest")
        print(" [4] Sair")
        print("==================================================")
        
        opcao = input("Escolha uma opcao (1-4): ").strip()
        
        if opcao == "1":
            link = input("\nCole o link do vídeo: ").strip()
            if link:
                baixar_video(link)
            input("\nProcesso finalizado. Pressione Enter para voltar ao menu...")
            
        elif opcao == "2":
            link = input("\nCole o link do áudio/vídeo: ").strip()
            if link:
                baixar_audio(link)
            input("\nProcesso finalizado. Pressione Enter para voltar ao menu...")
            
        elif opcao == "3":
            link = input("\nCole o link do Pin ou Pasta do Pinterest: ").strip()
            if link:
                baixar_pinterest(link)
            input("\nProcesso finalizado. Pressione Enter para voltar ao menu...")
            
        elif opcao == "4":
            print("\nSaindo... Bons momentos de escrita e inspiração! ✨")
            sys.exit()
            
        else:
            print("\n[!] Opção inválida! Tente novamente.")
            time.sleep(1)

if __name__ == "__main__":
    main()