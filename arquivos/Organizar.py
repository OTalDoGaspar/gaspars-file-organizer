class Organizar:

    from Arquivo import Arquivo
    import os

    extensoes_imagem = ["jpg", "jpeg", "png", "gif", "webp", "bmp", "svg", "raw"]
    extensoes_texto = ["txt", "doc", "docx", "pdf", "rtf", "odt", "tex", "md", "pages"]
    extensoes_comprimidos = ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "iso", "z"]
    extensoes_video = ["mp4", "mkv", "avi", "mov", "wmv", "flv", "webm", "m4v", "mpg", "mpeg"]
    extensoes_audio = ["mp3", "wav", "flac", "aac", "ogg", "wma", "m4a", "aiff", "opus", "alac"]

    username = os.getlogin
    destino = os.getenv("Destino")
    downloads = os.getenv("Downloads")
    
    if (destino != None) and (downloads != None):

        os.chdir(downloads)
        conteudo = os.listdir()

        for i in conteudo:
            arquivo = Arquivo(i)
            os.chdir(destino)
            if(os.path.isdir(f"{downloads}\'{arquivo.getNome()}'") == False):
                os.chdir(downloads)
                if arquivo.getExtensao() in extensoes_imagem:
                    os.system(f"move {downloads}/'{arquivo.getNome()}' {destino}/Imagens/")
                elif arquivo.getExtensao() in extensoes_texto:
                    os.system(f"move {downloads}/'{arquivo.getNome()}' {destino}/Textos/")
                elif arquivo.getExtensao() in extensoes_comprimidos:
                    os.system(f"move {downloads}/'{arquivo.getNome()}' {destino}/Comprimidos/")
                elif arquivo.getExtensao() in extensoes_video:
                    os.system(f"move {downloads}/'{arquivo.getNome()}' {destino}/Videos/")
                elif arquivo.getExtensao() in extensoes_audio:
                    os.system(f"move {downloads}/'{arquivo.getNome()}' {destino}/Audios/")
                else:
                    os.system(f"move {downloads}/'{arquivo.getNome()}' {destino}/{arquivo.getExtensao}/")
            print(arquivo.getNome())
    else:
        print("\033[1;31m Variáveis de ambiente não configuradas corretamente! Certifique-se que as variáveis 'destino' e 'downloads' existem! \033[0m")
    
Organizar()