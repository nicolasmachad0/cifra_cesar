# Projeto de APS - Cifra de Cesar
# Integrantes
# CASSIANO AUGUSTO PROENÇA MARTINS DE MELO
# GABRIEL DOS SANTOS ALVES
# LUCAS BULBOV NOGUEIRA
# NICHOLAS PEREIRA DE BRITES NASCIMENTO
# NICOLAS MACHADO FOGAÇA


# Função que implementa a cifra de César
def cifra_cesar(texto, chave, acao):
    resultado = ''  # Inicializa uma string vazia para armazenar o resultado
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Define o alfabeto a ser usado na cifra de César

    # Itera sobre cada caractere no texto de entrada
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra
            char_maiusculo = char.upper()  # Converte o caractere para maiúsculas

            # Verifica a ação a ser executada (criptografar ou descriptografar)
            if acao == 'criptografar':
                if char_maiusculo in alfabeto:  # Verifica se o caractere está no alfabeto
                    # Calcula a nova posição da letra após a criptografia
                    indice = (alfabeto.index(char_maiusculo) + chave) % 26
                    char_cifrado = alfabeto[indice]  # Obtém o caractere cifrado

                    if char.islower():
                        char_cifrado = char_cifrado.lower()  # Mantém o caractere em minúsculas, se for o caso
                else:
                    char_cifrado = char  # Mantém caracteres que não estão no alfabeto inalterados
            elif acao == 'descriptografar':
                if char_maiusculo in alfabeto:
                    # Calcula a nova posição da letra após a descriptografia
                    indice = (alfabeto.index(char_maiusculo) - chave) % 26
                    char_cifrado = alfabeto[indice]  # Obtém o caractere descriptografado

                    if char.islower():
                        char_cifrado = char_cifrado.lower()  # Mantém o caractere em minúsculas, se for o caso
                else:
                    char_cifrado = char  # Mantém caracteres que não estão no alfabeto inalterados

            resultado += char_cifrado  # Adiciona o caractere cifrado ou descriptografado ao resultado
        else:
            resultado += char  # Mantém caracteres não alfabéticos inalterados

    return resultado  # Retorna o resultado final

# Loop principal para exibir o menu e processar a escolha do usuário
while True:
    
    print("Menu:")
    print("1. Criptografar")
    print("2. Descriptografar")
    print("3. Sair")
    
    menu = input("Escolha uma opção: ")  # Solicita a escolha do usuário
    
    if menu == '1':  # Se a escolha for 1, criptografa o texto

        texto = input("Digite o texto a ser criptografado: ")  # Solicita o texto de entrada
        chave = int(input("Digite a chave da cifra de César: "))  # Solicita a chave de criptografia
        texto_criptografado = cifra_cesar(texto, chave, 'criptografar')  # Chama a função para criptografar
        print("Texto criptografado: " + texto_criptografado)  # Exibe o resultado criptografado

    elif menu == '2':  # Se a escolha for 2, descriptografa o texto

        texto = input("Digite o texto a ser descriptografado: ")  # Solicita o texto de entrada
        chave = int(input("Digite a chave da cifra de César: "))  # Solicita a chave de descriptografia
        texto_descriptografado = cifra_cesar(texto, chave, 'descriptografar')  # Chama a função para descriptografar
        print("Texto descriptografado: " + texto_descriptografado)  # Exibe o resultado descriptografado

    elif menu == '3':  # Se a escolha for 3, sai do programa

        print("Saindo...")
        break

    else:  # Se a escolha for inválida

        print("Opção inválida. Tente novamente.")  # Exibe uma mensagem de erro