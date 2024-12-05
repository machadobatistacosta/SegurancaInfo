import math

def cifrar_colunar(texto, colunas):
    # Remover espaços em branco do texto
    texto = texto.replace(" ", "")
   
    # Calcular o número de linhas necessárias
    linhas = math.ceil(len(texto) / colunas)
   
    # Preencher a matriz com o texto
    matriz = [['' for _ in range(colunas)] for _ in range(linhas)]
   
    index = 0
    for i in range(linhas):
        for j in range(colunas):
            if index < len(texto):
                matriz[i][j] = texto[index]
                index += 1

    # Ler a matriz coluna por coluna para gerar o texto cifrado
    cifrado = ''
    for j in range(colunas):
        for i in range(linhas):
            if matriz[i][j] != '':
                cifrado += matriz[i][j]
   
    return cifrado

def decifrar_colunar(texto_cifrado, colunas):
    # Calcular o número de linhas necessárias
    linhas = math.ceil(len(texto_cifrado) / colunas)
   
    # Calcular o número de caracteres na última linha
    num_chars_last_row = len(texto_cifrado) % colunas
    if num_chars_last_row == 0:
        num_chars_last_row = colunas
   
    # Criar uma matriz vazia
    matriz = [['' for _ in range(colunas)] for _ in range(linhas)]
   
    # Preencher a matriz coluna por coluna com o texto cifrado
    index = 0
    for j in range(colunas):
        for i in range(linhas):
            # Se for a última linha, garantir que não ultrapasse o número de caracteres
            if i == linhas - 1 and j >= num_chars_last_row:
                continue
            if index < len(texto_cifrado):
                matriz[i][j] = texto_cifrado[index]
                index += 1

    # Ler a matriz linha por linha para decifrar o texto
    decifrado = ''
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] != '':
                decifrado += matriz[i][j]
   
    return decifrado

# Exemplo de uso
texto = "VAMOS ATACAR O SUL NO FINAL DESTA SEMANA"
colunas = 7

# Cifrar
texto_cifrado = cifrar_colunar(texto, colunas)
print("Texto Cifrado:", texto_cifrado)

# Decifrar
texto_decifrado = decifrar_colunar(texto_cifrado, colunas)
print("Texto Decifrado:", texto_decifrado)
 
def cifrar_ferroviaria(texto, trilhos):
    # Remover espaços em branco do texto
    texto = texto.replace(" ", "")
   
    # Criar uma lista de trilhos (linhas)
    linhas = ['' for _ in range(trilhos)]
   
    # Indicar a direção do ziguezague (subindo ou descendo)
    descendo = False
    linha_atual = 0
   
    for char in texto:
        linhas[linha_atual] += char
        if linha_atual == 0 or linha_atual == trilhos - 1:
            descendo = not descendo
        linha_atual += 1 if descendo else -1

    # Concatenar todas as linhas para formar o texto cifrado
    cifrado = ''.join(linhas)
    return cifrado

def decifrar_ferroviaria(texto_cifrado, trilhos):
    # Criar uma lista de trilhos vazios
    linhas = ['' for _ in range(trilhos)]
   
    # Identificar a sequência de ziguezague (subindo ou descendo)
    padrao_ziguezague = ['' for _ in range(len(texto_cifrado))]
    descendo = False
    linha_atual = 0
   
    # Marcar o padrão do ziguezague
    for i in range(len(texto_cifrado)):
        padrao_ziguezague[i] = linha_atual
        if linha_atual == 0 or linha_atual == trilhos - 1:
            descendo = not descendo
        linha_atual += 1 if descendo else -1

    # Preencher os trilhos com os caracteres do texto cifrado
    index = 0
    for linha in range(trilhos):
        for i in range(len(texto_cifrado)):
            if padrao_ziguezague[i] == linha:
                linhas[linha] += texto_cifrado[index]
                index += 1

    # Reconstruir o texto original seguindo o padrão ziguezague
    decifrado = ''
    linha_atual = 0
    descendo = False
    for i in range(len(texto_cifrado)):
        decifrado += linhas[linha_atual][0]
        linhas[linha_atual] = linhas[linha_atual][1:]
        if linha_atual == 0 or linha_atual == trilhos - 1:
            descendo = not descendo
        linha_atual += 1 if descendo else -1
   
    return decifrado

# Exemplo de uso
texto = "ataque ao amanhecer"
trilhos = 3
texto_cifrado = cifrar_ferroviaria(texto, trilhos)
print("Texto Cifrado:", texto_cifrado)

texto_decifrado = decifrar_ferroviaria(texto_cifrado, trilhos)
print("Texto Decifrado:", texto_decifrado)