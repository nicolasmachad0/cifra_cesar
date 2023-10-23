# Projeto de APS - Cifra de Cesar
# Integrantes
# CASSIANO AUGUSTO PROENÇA MARTINS DE MELO
# GABRIEL DOS SANTOS ALVES
# LUCAS BULBOV NOGUEIRA
# NICHOLAS PEREIRA DE BRITES NASCIMENTO
# NICOLAS MACHADO FOGAÇA

# Função que implementa a cifra de César

def cesar(texto, chave, agir): 
    if len(texto) > 128:
        return "O texto deve ter no máximo 128 caracteres." # Define um limeite de 128 caracteres 
    resultado = '' # Inicializa uma string vazia para armazenar o resultado
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #  alfabeto que vai ser utilizado

# Itera cada caractere no texto de entrada
    for char in texto:     
        if char.isalpha(): # Verifica se o caractere é uma letra
            char_maiusculo = char.upper() # Converte o caractere para maiúsculas
            
            # Verifica a ação a ser executada (criptografar ou descriptografar)
            if agir == 'criptografar':
                if char_maiusculo in alfabeto: # Verifica se o caractere está no alfabeto
                    calculo = (alfabeto.index(char_maiusculo) + chave) % 26  # Calcula a nova posição da letra após a criptografia
                    texto_cifrado = alfabeto[calculo]# Obtém o caractere cifrado

                    if char.islower(): 
                        texto_cifrado = texto_cifrado.lower() # Mantém o caractere em minúsculas
                else:
                    texto_cifrado = char # Mantém caracteres que não estão no alfabeto inalterados

            elif agir == 'descriptografar':

                if char_maiusculo in alfabeto:  # Calcula a nova posição da letra após a descriptografia
                    calculo = (alfabeto.index(char_maiusculo) - chave) % 26 # Calcula a nova posição da letra após a descriptografia
                    texto_cifrado = alfabeto[calculo] # Obtém o caractere descriptografado

                    if char.islower():
                        texto_cifrado = texto_cifrado.lower() # Mantém o caractere em minúsculas
                else:
                    texto_cifrado = char # Mantém caracteres que não estão no alfabeto inalterados

            resultado += texto_cifrado # Adiciona o caractere cifrado ou descriptografado ao resultado
        else:
            resultado += char # Mantém caracteres não alfabéticos inalterados

    return resultado # Retorna o resultado final

# Função que implementa a cifra de César

print('APS 2023 - Cifra de Cesar')

while True:
    print('\n')
    print('1 - Critptografar')
    print('2 - Descriptografar')
    print ('3 - Sair')

    painel = input('O que deseja: ') # Este é o menu para estar realizando as operações de criptografia

    if painel == '1': # Aqui é aonde funciona a criptografia do texto

        texto = input("Digite o texto: ")  # Solicita o texto de entrada
        if len(texto) > 128: # limitador de caracter
            continue
        chave = int(input("Digite a chave da cifra de César: "))   # Solicita a chave de criptografia
        criptografado = cesar(texto, chave, 'criptografar')  # Chama a função para criptografar
        print("Texto criptografado: " + criptografado)  # Exibe o resultado criptografado


    elif painel == '2': # Aqui é aonde funciona a descriptografia do texto

        texto = input("Digite o texto: ") # Solicita o texto de entrada
        if len(texto) > 128: # limitador de caracter
            continue
        chave = int(input("Digite a chave da cifra de César: ")) # Solicita a chave de descriptografia
        descriptografado = cesar(texto, chave, 'descriptografar')  # Chama a função para descriptografar
        print("Texto descriptografado: " + descriptografado)   # Exibe o resultado descriptografado

    elif painel == '3': # Se a escolha for 3, sai do programa

        print("Saindo...")
        break

    else:  # Se a escolha for inválida

        print("Opção inválida. Tente novamente.") # Exibe uma mensagem de erro
