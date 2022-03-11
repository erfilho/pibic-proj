import nltk
import re
from nltk import word_tokenize

# Declaração de constantes
SOURCE_URL = "./stuff/c_tests/"

    #Auxiliares para a classificação dos tokens
OPERADORES = ['+', '-', '*', '/', '%', '==', '+=', '-=', '--', '++', '>', '<', '>=', '<=', '&&', '||']
SEPARADORES = [',', ';', ':', '\n', '{', '}', '[', ']', '(', ')']
FUNCOES = ['clrscr', 'printf', 'scanf', 'getch','main']
PALAVRA_CHAVE = ['return', 'break', 'continue']

# Declaração de variáveis
archive_lines = ""
archive = ""

# Declaração de funções

    # Função que vai verificar cada token e classificar
def lexer(tokens):
    for token in tokens:
        if token in OPERADORES:
            print(f'OPERADOR {token}')
        elif token in SEPARADORES:
            print(f'SEPARADOR {token}')
        elif token in PALAVRA_CHAVE:
            print(f'PALAVRA CHAVE {token}')
        elif token in FUNCOES:
            print(f'FUNÇÃO {token}')
        elif re.match(r'include*', token):
            print(f'INCLUSÃO {token}')
        elif re.match(r'^[^\d\W]\w*.h', token):
            print(f'BIBLIOTECA {token}')
        elif re.match(r'^[-+]?[0-9]+$', token):
            print(f'NÚMERO {token}')
        elif re.match(r'^[^\d\W]\w*\Z', token):
            print(f'IDENTIFICADOR {token}')


# Teste para abrir arquivos com Python
print("Início do programa: Lendo arquivos de código com python!")

# Abrindo o arquivo
archive = open(SOURCE_URL+'helloworld.c', 'r')

# Testando se o arquivo foi aberto corretamente
if archive:
    print("\nArquivo aberto com sucesso!")

    # Passando cada linha do arquivo para uma variável
    for line in archive:
        archive_lines += line

    # Criando os tokens 
    tokens = word_tokenize(archive_lines)

    # Mostrando os tokens que foram criados
    print(f'\n{tokens}')

    # Uso da função que vai classificar os tokens
    lexer(tokens)

else:
    print("Falha ao abrir o arquivo!")

# Fechando o arquivo
archive.close()