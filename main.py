# OPEN TYPES
# w    → modo de gravação (se o arquivo não existir, crie-o e abra-o no modo de gravação)
# r    → modo de leitura
# a    → modo anexar (se o arquivo não existir, crie-o e abra-o no modo anexar)
# w+   → criar um arquivo - se ele não existir e abri-lo no modo de gravação
# r+   → abre um arquivo existente no modo de leitura + gravação
# a+   → criar um arquivo - se ele não existir e abri-lo no modo anexar
# rb   → modo de leitura em binário

# CURSOR
# 0 →  desde o início do arquivo.
# 1 →  localização atual do cursor.
# 2 →  do final do arquivo. Este valor pode ser usado apenas no modo binário.
# .tell() onde está o cursor
# .seek() para onde ir o cursor


try:
    f = open("exemplo.txt", "w+")
    f.write("Usando Python\n")

    paises = ['Angola\n', 'Brasil\n', 'Portugal\n']
    f.writelines(paises)
    f.close()

except Exception as e:
    print(e)
# finally:
#     f.close()


# Ler um arquivo
with open("exemplo.txt", "r") as f:
    c = f.read()  # Lê o conteudo do arquivo
    linha = f.readline()  # Lê a linha do arquivo
    linhas = f.readlines()  # Lê as linhas do arquivo em uma lista

    while linha != "":
        print(line)
        line = f.readline()

    print(c)


with open("exemplo.txt", "rb") as f:
    print(f.tell())
    print(f.seek(-10, 2))
    print(f.tell())
    print(f.read())


# Escrever em um arquivo
with open("exemplo.txt", "w") as f:
    f.write("hello")


# Copy File
import os
import shutil

os.system("copy main.py  ficheiro_copia")
shutil.copy("main.py", "ficheiro_copia.py")
shutil.copy2("main.py", "ficheiro_copia.py")  # Cópia os metadados
shutil.copyfile("exemplo.txt", "Ficheiro_copia")  # Cópia sem as permissões

# os.system("mv local onde esta localizado o arquivo")
# os.rename("caminho de origem", "caminho de destino")
# shutil.move("caminho de origem", "caminho de destino")

# os.remove("o local onde esta localizado o arquivo")
# os.system("rm o local onde esta localizado o arquivo")


