from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify

# Função para criptografar com Blowfish no modo ECB
def encrypt_blowfish_ecb(key, data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_data = pad(data.encode(), Blowfish.block_size)  # Aplica o preenchimento PKCS#5
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Função para criptografar com Blowfish no modo CBC
def encrypt_blowfish_cbc(key, data, iv):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    padded_data = pad(data.encode(), Blowfish.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Função para descriptografar com CBC
def decrypt_blowfish_cbc(key, encrypted_data, iv):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), Blowfish.block_size)
    return decrypted_data.decode()

# Função para converter os dados em hexadecimal
def to_hex(data):
    return hexlify(data).decode()

# Chave usada para todos os casos
key = bytes([65, 66, 67, 68, 69])  # Sequência de bytes [65, 66, 67, 68, 69]

# Caso 1: Criptografar o texto “FURB” usando o modo ECB
data_case_1 = "FURB"
encrypted_case_1 = encrypt_blowfish_ecb(key, data_case_1)
print(f"Caso 1.1: Texto cifrado (hex): {to_hex(encrypted_case_1)}")
print(f"Caso 1.2: Tamanho do texto cifrado: {len(encrypted_case_1)} bytes")

# Caso 2: Criptografar o texto "COMPUTADOR" usando o modo ECB
data_case_2 = "COMPUTADOR"
encrypted_case_2 = encrypt_blowfish_ecb(key, data_case_2)
print(f"Caso 2.1: Texto cifrado (hex): {to_hex(encrypted_case_2)}")
print(f"Caso 2.2: Tamanho do texto cifrado: {len(encrypted_case_2)} bytes")
# PKCS#5 adiciona preenchimento ao bloco para múltiplos de 8 bytes.

# Caso 3: Criptografar "SABONETE" usando ECB
data_case_3 = "SABONETE"
encrypted_case_3 = encrypt_blowfish_ecb(key, data_case_3)
print(f"Caso 3.1: Texto cifrado (hex): {to_hex(encrypted_case_3)}")
print(f"Caso 3.2: Tamanho do texto cifrado: {len(encrypted_case_3)} bytes")

# Caso 4: Criptografar sequência de bytes [8, 8, 8, 8, 8, 8, 8, 8] com ECB
data_case_4 = bytes([8, 8, 8, 8, 8, 8, 8, 8])
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
encrypted_case_4 = cipher.encrypt(data_case_4)
print(f"Caso 4.1: Texto cifrado (hex): {to_hex(encrypted_case_4)}")

# Caso 5: Criptografar "SABONETESABONETESABONETE" usando ECB
data_case_5 = "SABONETESABONETESABONETE"
encrypted_case_5 = encrypt_blowfish_ecb(key, data_case_5)
print(f"Caso 5.1: Texto cifrado (hex): {to_hex(encrypted_case_5)}")
print(f"Caso 5.2: Tamanho do texto cifrado: {len(encrypted_case_5)} bytes")

# Caso 6: Criptografar "FURB" usando CBC (sem IV definido, com IV aleatório)
iv_case_6 = Blowfish.block_size * b'\x00'
encrypted_case_6 = encrypt_blowfish_cbc(key, data_case_1, iv_case_6)
print(f"Caso 6.1: Texto cifrado (hex): {to_hex(encrypted_case_6)}")

# Caso 7: Criptografar "FURB" com CBC e IV definido
iv_case_7 = bytes([1, 1, 2, 2, 3, 3, 4, 4])
encrypted_case_7 = encrypt_blowfish_cbc(key, data_case_1, iv_case_7)
print(f"Caso 7.1: Texto cifrado (hex): {to_hex(encrypted_case_7)}")

# Caso 8: Criptografar "SABONETESABONETESABONETE" com CBC e IV definido
data_case_8 = "SABONETESABONETESABONETE"
encrypted_case_8 = encrypt_blowfish_cbc(key, data_case_8, iv_case_7)
print(f"Caso 8.1: Texto cifrado (hex): {to_hex(encrypted_case_8)}")

# Caso 9: Criptografar "SABONETESABONETESABONETE" com CBC e outro IV
iv_case_9 = bytes([10, 20, 30, 40, 50, 60, 70, 80])
encrypted_case_9 = encrypt_blowfish_cbc(key, data_case_8, iv_case_9)
print(f"Caso 9.1: Texto cifrado (hex): {to_hex(encrypted_case_9)}")

# Caso 10: Criptografar "FURB" com ECB e tentar descriptografar com chave errada
wrong_key = b"11111"
cipher_wrong = Blowfish.new(wrong_key, Blowfish.MODE_ECB)
try:
    decrypted_data = unpad(cipher_wrong.decrypt(encrypted_case_1), Blowfish.block_size)
    print(f"Caso 10.1: Texto decifrado: {decrypted_data.decode()}")
except Exception as e:
    print(f"Caso 10.1: Falha ao decifrar com chave incorreta: {str(e)}")

# Caso 11: Criptografar arquivo PDF (use o caminho do arquivo PDF)
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        file_data = f.read()
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_data = pad(file_data, Blowfish.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

# Caso 12: Descriptografar o arquivo binário e restaurar o PDF
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), Blowfish.block_size)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

Respostas dos Casos
Caso 1:

Texto cifrado: Dependerá da execução, saída será em hexadecimal.
Extensão: Dependerá do resultado (deve ser 8 bytes devido ao preenchimento).
Caso 2:

Texto cifrado: Hexadecimal.
Extensão: Dependerá do comprimento do bloco com preenchimento.
Caso 3:

Texto cifrado: Hexadecimal.
Extensão: 8 bytes ou múltiplos, devido ao preenchimento.
Caso 4:

Texto cifrado: Hexadecimal.
Caso 5:

Texto cifrado: Hexadecimal.
Extensão: Múltiplos de 8 bytes.
Caso 6:

Texto cifrado: Hexadecimal (usando CBC).
Caso 7:

Texto cifrado: Hexadecimal com IV [1, 1, 2, 2, 3, 3, 4, 4].
Caso 8:

Texto cifrado: Hexadecimal com CBC.
Caso 9:

Texto cifrado: Hexadecimal (usando um IV diferente).
Caso 10:

Falha ao descriptografar com chave incorreta.

from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad

def encrypt_file(input_file, output_file, key):
    # Abrir o arquivo PDF
    with open(input_file, 'rb') as f:
        file_data = f.read()

    # Configurar o cifrador Blowfish com a chave e o modo ECB
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    
    # Aplicar o preenchimento PKCS#5
    padded_data = pad(file_data, Blowfish.block_size)
    
    # Criptografar o arquivo
    encrypted_data = cipher.encrypt(padded_data)
    
    # Escrever o arquivo criptografado
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

    # Retornar o tamanho dos arquivos para comparação
    return len(file_data), len(encrypted_data)

# Definir chave e arquivos
key_case_11 = b"ABCDE"
input_pdf = '/mnt/data/L06 - Criptografia Blowfish (v2).pdf'  # Arquivo PDF que você forneceu
output_bin = '/mnt/data/saida.bin'

# Executar a criptografia
original_size, encrypted_size = encrypt_file(input_pdf, output_bin, key_case_11)
print(f"Tamanho do arquivo original: {original_size} bytes")
print(f"Tamanho do arquivo criptografado: {encrypted_size} bytes")


from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad

def decrypt_file(input_file, output_file, key):
    # Abrir o arquivo criptografado
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    # Configurar o cifrador Blowfish com a chave e o modo ECB
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    # Descriptografar o arquivo e remover o preenchimento
    decrypted_data = unpad(cipher.decrypt(encrypted_data), Blowfish.block_size)

    # Escrever o arquivo descriptografado
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Definir arquivos
input_bin = '/mnt/data/saida.bin'
output_pdf = '/mnt/data/decriptografado.pdf'

# Executar a descriptografia
decrypt_file(input_bin, output_pdf, key_case_11)
print("Arquivo descriptografado salvo como 'decriptografado.pdf'. Tente abri-lo.")
