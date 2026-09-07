from pathlib import Path
import shutil

def organizacao_das_pastas(inicio, tipos, informacoes):
    buscador_arquivos = Path(f"{informacoes}/Downloads") 
    if not inicio.exists():
        inicio.mkdir()
    
    for i in tipos.values():
        pastas = Path(f"{inicio}/{i}")
        if not pastas.exists():
            pastas.mkdir()
            
    
    for arquivos in buscador_arquivos.iterdir():
        if arquivos.suffix in tipos:
            shutil.move(f"{arquivos}",f"{inicio}/{tipos[arquivos.suffix]}" )
        
            

         
        
        
    

informacoes_usuario = Path.home()
pasta_inicial = Path(f"{informacoes_usuario}/Downloads/arquivos_ordenados")
tipos_de_arquivos = {
    ".png": "imagens",
    ".jpeg": "imagens",
    ".pdf": "documentos",
    ".ppt": "slides",
    ".mp4": "audios"
} 

organizacao_das_pastas(pasta_inicial,tipos_de_arquivos, informacoes_usuario)







    