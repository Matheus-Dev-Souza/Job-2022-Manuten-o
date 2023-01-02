import os
import shutil
# listar arquivos
def listar():
    arquivos = os.listdir()
    print(arquivos)

#listar diretorio
def listadir():
    os.path.abspath('.')

#criar pasta
def novapasta():
    os.mkdir("arquivos1")
    
# caminho da pasta
def diretorio():
    caminho = os.getcwd()
    print(caminho)
    
#mudar diretório
def mudardir():
    os.chdir()

# renomear
def renomear():
    os.rename('OS.py', 'OS1.py')

# mover
def mover():
    os.rename('OS1.py', 'arqivos\OS1.py')

# copiar arquivos
def copiararq():
    shutil.copy2('OS.py', 'arquivos\OS.py')
    
# copiar arquivos
def copiarpasta():
    shutil.copytree('OS.py', 'arquivos\OS.py')
    
#criar atalho
def atalho():
    os.symlink()

#Apagar    
def apagar():
    shutil.rmtree('arquivos1')
      
#novapasta()
#listadir()
#copiar()
apagar()