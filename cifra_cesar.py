# Projeto de APS - Cifra de Cesar
# Integrantes
# CASSIANO AUGUSTO PROENÇA MARTINS DE MELO
# GABRIEL DOS SANTOS ALVES
# GABRIEL MANUTA
# LUCAS BULBOV NOGUEIRA
# NICHOLAS PEREIRA DE BRITES NASCIMENTO
# NICOLAS MACHADO FOGAÇA
# NATHAN SOUZA     

# Função que implementa a cifra de César

# Definição das variaveis mais importantes do software
def cesar(texto, chave, agir): 
    # Irá reconhecer se o texto tem mais de 128 caracteres
    if len(texto) > 128: 
        return "O texto deve ter no máximo 128 caracteres." # Texto para avisar ter mais de 128 caracteres
    resultado = '' # Inicializa uma string vazia para armazenar o resultado
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊẼÈÓÒÔÕÌÎĨÍÚÙÛŨÇ' #  Este alfabeto sera utilizado em Maiusculo pois trata-se de aprimoração do codigo, um exemplo seria caso escreva tudo minusculo algum texto no programa, o codigo ira pegar o alfabeto variavel e irá converter corretamente.

    # Itera cada caractere no texto de entrada
    for char in texto:  
            char_maiusculo = char.upper() # Converte cada letra para maíusculo
            
            # Verifica a ação a ser executada (criptografar ou descriptografar)
            
            # Ação da Criptografia
            if agir == 'criptografar':
                if char_maiusculo in alfabeto: # Verifica se o caractere está no alfabeto
                    calculo = (alfabeto.index(char_maiusculo) + chave) % 48  # Calcula a nova posição da letra após a criptografia, com o modulo, fazendo com que pegue o valor "48" sendo feito uma divisão para estar sendo utilizado o resto desta divisão para o valor da chave, desta forma, evitando erro ao digitar algum numero de chave
                    texto_cifrado = alfabeto[calculo]# Obtém o caractere cifrado usando a variavel alfabeto 
                    
                    # Para caracterese Minusculos
                    if char.islower():  
                        texto_cifrado = texto_cifrado.lower() # Mantém o caractere em minúsculas
                else:
                    texto_cifrado = char # Mantém caracteres que não estão no alfabeto inalterados

            # Ação da Descriptografia
            elif agir == 'descriptografar': 

                if char_maiusculo in alfabeto:  # Verifica se o caractere está no alfabeto
                    calculo = (alfabeto.index(char_maiusculo) - chave) % 48 # # Calcula a nova posição da letra após a descriptografia, com o modulo, fazendo com que pegue o valor "48" sendo feito uma divisão para estar sendo utilizado o resto desta divisão para o valor da chave, desta forma, evitando erro ao digitar algum numero de chave
                    texto_cifrado = alfabeto[calculo] # Obtém o caractere descriptografado

                    if char.islower(): # Para caracterese Minusculos
                        texto_cifrado = texto_cifrado.lower() # Mantém o caractere em minúsculas
                else:
                    texto_cifrado = char # Mantém caracteres que não estão no alfabeto inalterados

            resultado += texto_cifrado # Adiciona o caractere cifrado ou descriptografado ao resultado

    return resultado # Retorna o resultado final


# Função que implementa a cifra de César

print('APS 2023 - Cifra de Cesar') # Titulo do Softaware
print('Integrantes')
print('CASSIANO AUGUSTO PROENÇA MARTINS DE MELO')
print('GABRIEL DOS SANTOS ALVES')
print('GABRIEL MANUTA')
print('LUCAS BULBOV NOGUEIRA')
print('NICHOLAS PEREIRA DE BRITES NASCIMENTO')
print('NICOLAS MACHADO FOGAÇA')
print('NATHAN SOUZA')

painel = None # Variavel para estar definindo como valor nulo
while (painel!='0'): # Faz com que o menu funcione em looping tendo controle usando o operador !="0", tornado-se false para caso haja encerramento do software, digitando "0". 
    print('\n') # serve para dar um espaço entre os prints
    print('1 - Criptografar') # opção de criptografar
    print('2 - Descriptografar') # Opção de Descriptografar
    print('0 - Sair') # Opção de sair do software

    painel = input('O que deseja: ') # Este é o menu para estar realizando as operações de criptografia

    if painel == '0':  # Se a escolha for 0, sai do programa
        print("Saindo...") # Mostra na tela a mensagem de saida

    elif painel == '1': # Aqui é aonde funciona a criptografia do texto
        texto = input("Digite o texto: ")# Solicita o texto de entrada
        if len(texto) > 128: # limitador de caracter
            print("O texto deve ter no máximo 128 caracteres.") # Mostra mensagem de texto com no maxio de 128 caracteres
            continue # Retorna ao menu para que seja feito todo o processo novamente
        chave = int(input("Digite um valor entre 1 e 48 para a chave: ")) # Solicita a chave de criptografia
        while chave < 1 or chave > 48: # Define while para que os valore de chave são de 1 até 48 como um looping até que seja uns destes valores
            chave = int(input("Digite um valor válido: ")) # Mostra mensagem de texto com para colocar algum valor valido
        criptografado = cesar(texto, chave, 'criptografar') # Chama a função para criptografar
        print("Texto criptografado: " + criptografado) # Exibe o resultado criptografado

    elif painel == '2': # Aqui é aonde funciona a descriptografia do texto
        texto = input("Digite o texto: ") # Solicita o texto de entrada
        if len(texto) > 128:  # limitador de caracter
            print("O texto deve ter no máximo 128 caracteres.") # Mostra mensagem de texto com no maxio de 128 caracteres
            continue # Retorna ao menu para que seja feito todo o processo novamente
        chave = int(input("Digite um valor entre 1 e 48 para a chave: ")) # Solicita a chave de descriptografia
        while chave < 1 or chave > 48: # Define while para que os valores de chave são de 1 até 48 como um looping até que seja uns destes valores
            chave = int(input("Digite um valor válido: ")) # Mostra mensagem de texto com para colocar algum valor valido
        descriptografado = cesar(texto, chave, 'descriptografar')  # Chama a função para descriptografar
        print("Texto descriptografado: " + descriptografado) # Exibe o resultado descriptografado

    else: # Se a escolha for inválida
        print("Opção inválida. Tente novamente.") # Exibe uma mensagem de erro
