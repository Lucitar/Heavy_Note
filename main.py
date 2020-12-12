# Importa a biblioteca 'os' para uso no path
import os

# Cabeçalho do Programa
print("##################################")
print("   Heavy Note - By Victor Lucio   ")
print("##################################\n")


print("Opções para esse programa: ")
print("1- Criar arquivos com base no tamanho")
print("2- Criar arquivos com base em repetição de frases")
print("3- Sair do programa")

escolha = eval(input("Digite o código de uma opção: "))


if(escolha == 1):
    # Nome do Arquivo
    nome_arq = str(input("Nome do arquivo(sem extensão): "))
    
    # Recebe a unidade de armazenamento do arquivo
    unidade = str(input("Unidade de Armazenamento(B/KB/MB/GB): "))

    # Tamanho final do arquivo em Megabytes
    num = int(input("Tamanho inteiro do Arquivo: "))

    # Adiciona uma mensagem padrão para repetição
    frase = "L"
    
elif(escolha == 2):
    # Nome do Arquivo
    nome_arq = str(input("Nome do arquivo(sem extensão): "))
    
    # Frase que irá preencher o arquivo
    frase = str(input("Frase para preencher o arquivo: "))

    # Quantidade de vezes que a frase se repetirá.
    num = int(input("Quantidade de vezes que a frase se repetirá: "))

    # Adiciona uma unidade padrão
    unidade = "B"
    
else:
    exit()
    
# Cria o caminho do arquivo
path_arquivo = os.path.dirname(__file__) + "/" + nome_arq + ".txt"

# Cria o arquivo
arquivo = open(path_arquivo, 'w', encoding="utf-8")

# 1 MegaBytes = 1048576 Bytes = 1024 * 1024 Bytes

if(unidade == "GB"):
    # 1 GigaBytes = 1073741824 Bytes = 1024 * 1024 * 1024 Bytes
    conversor = 1073741824
elif(unidade == "MB"):
    # 1 MegaBytes = 1048576 Bytes = 1024 * 1024 Bytes
    conversor = 1048576
elif(unidade == "KB"):
    # 1 KiloBytes = 1024 Bytes
    conversor = 1024
else:
    # 1 Byte = 1 Byte
    conversor = 1
    

if(escolha == 1):
    # Calculo do loop
    quant_loop = int(num*(conversor))

    # Loop que escreve uma letra até alcançar o tamanho desejado
    for i in range(0, quant_loop):
        arquivo.write(frase)
    
elif(escolha == 2):
    # Loop que escreve frases no arquivo
    for i in range(0, num):
        arquivo.write(frase + '\n')


# Fechando o arquivo
arquivo.close()

# Escreve uma confirmação
print("\n-------------------------------------------------")
print(" Arquivo Criado com Sucesso. Programa Encerrado. ")
print("-------------------------------------------------")
