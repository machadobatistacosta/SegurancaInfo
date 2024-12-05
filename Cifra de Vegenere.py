def generate_vigenere_table():
    table = []
    for i in range(26):
        row = []
        for j in range(26):
            row.append(chr((i + j) % 26 + 65))  # Gera a tabela de A até Z
        table.append(row)
    return table

def vigenere_encrypt(plain_text, key):
    table = generate_vigenere_table()
    encrypted_text = []
    key = key.upper().replace(" ", "")
    plain_text = plain_text.upper().replace(" ", "")
    key_index = 0

    for char in plain_text:
        if char.isalpha():  # Cifra apenas letras
            row = ord(char) - 65
            col = ord(key[key_index % len(key)]) - 65
            encrypted_text.append(table[row][col])
            key_index += 1
        else:
            encrypted_text.append(char)  # Mantém o caractere não alfabético (ex: espaço)

    return ''.join(encrypted_text)

def vigenere_decrypt(cipher_text, key):
    table = generate_vigenere_table()
    decrypted_text = []
    key = key.upper().replace(" ", "")
    cipher_text = cipher_text.upper().replace(" ", "")
    key_index = 0

    for char in cipher_text:
        if char.isalpha():  # Decifra apenas letras
            col = ord(key[key_index % len(key)]) - 65
            row = 0
            while table[row][col] != char:
                row += 1
            decrypted_text.append(chr(row + 65))
            key_index += 1
        else:
            decrypted_text.append(char)  # Mantém o caractere não alfabético (ex: espaço)

    return ''.join(decrypted_text)

# Programa Principal
while True:
    print("\nCifra de Vigenère")
    print("1. Cifrar texto")
    print("2. Decifrar texto")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        texto_simples = input("Digite o texto a ser cifrado: ").upper()
        chave = input("Digite a chave: ").upper()
        texto_cifrado = vigenere_encrypt(texto_simples, chave)
        print(f"Texto Cifrado: {texto_cifrado}")
    elif opcao == '2':
        texto_cifrado = input("Digite o texto a ser decifrado: ").upper()
        chave = input("Digite a chave: ").upper()
        texto_simples = vigenere_decrypt(texto_cifrado, chave)
        print(f"Texto Decifrado: {texto_simples}")
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
