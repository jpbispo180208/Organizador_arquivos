📁 Organizador de Arquivos

Script em Python que organiza automaticamente os arquivos da pasta Downloads, movendo-os para subpastas de acordo com o tipo de arquivo.

📌 Sobre o projeto

Todo mundo tem uma pasta Downloads bagunçada, cheia de imagem, PDF e slide misturados. Esse script resolve isso automaticamente: varre a pasta, identifica a extensão de cada arquivo e move para a subpasta correta — sem precisar arrastar nada manualmente.

Projeto feito para praticar manipulação de arquivos e diretórios em Python.

🛠️ Tecnologias utilizadas
Python 3
pathlib — manipulação de caminhos de arquivo
shutil — mover arquivos entre pastas

Sem dependências externas — roda com Python puro.

⚙️ Como funciona
Verifica se a pasta de destino (Downloads/arquivos_ordenados) existe; se não, cria.
Cria uma subpasta para cada categoria de arquivo definida.
Percorre os arquivos soltos em Downloads e move cada um para a subpasta correspondente à sua extensão.
Categorias configuradas
Extensão	Pasta de destino
.png, .jpeg	imagens
.pdf	documentos
.ppt	slides
.mp4	audios
▶️ Como executar
bash
git clone https://github.com/jpbispo180208/organizador-de-arquivos.git
cd organizador-de-arquivos
python organizador.py

O script identifica automaticamente a pasta Downloads do usuário atual — não é preciso passar caminho nenhum na mão.

🔧 Personalizando

Para adicionar ou mudar os tipos de arquivo organizados, basta editar o dicionário tipos_de_arquivos:

python
tipos_de_arquivos = {
    ".png": "imagens",
    ".jpeg": "imagens",
    ".pdf": "documentos",
    ".ppt": "slides",
    ".mp4": "audios"
}
🚧 Possíveis melhorias
Corrigir a categoria de .mp4 (é vídeo, não áudio)
Tratar arquivos com nome duplicado no destino (hoje pode sobrescrever)
Organizar também arquivos dentro de subpastas do Downloads, não só os da raiz
Adicionar log do que foi movido
👤 Autor

Joao Pedro bispo — GitHub