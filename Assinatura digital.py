import rsa

# Parte 1: Criação de dois pares de chaves (A e B)
def gerar_chaves():
    # Gerar par de chaves A
    chave_publica_A, chave_privada_A = rsa.newkeys(512)
    # Gerar par de chaves B
    chave_publica_B, chave_privada_B = rsa.newkeys(512)
    
    # Salvar chaves em disco
    with open('chave_publica_A.pem', 'wb') as f:
        f.write(chave_publica_A.save_pkcs1('PEM'))
    with open('chave_privada_A.pem', 'wb') as f:
        f.write(chave_privada_A.save_pkcs1('PEM'))
    
    with open('chave_publica_B.pem', 'wb') as f:
        f.write(chave_publica_B.save_pkcs1('PEM'))
    with open('chave_privada_B.pem', 'wb') as f:
        f.write(chave_privada_B.save_pkcs1('PEM'))
    
    return chave_publica_A, chave_privada_A, chave_publica_B, chave_privada_B

# Gerar as chaves e salvar em arquivos
chave_publica_A, chave_privada_A, chave_publica_B, chave_privada_B = gerar_chaves()
print("Pares de chaves A e B gerados com sucesso!\n")


Pares de chaves A e B gerados com sucesso!

from google.colab import files

# Função para fazer upload de arquivos no Google Colab
def upload_arquivo():
    uploaded = files.upload()
    for nome_arquivo in uploaded.keys():
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso!")
        return nome_arquivo

# Parte 2: Assinatura do documento com a chave privada A
def assinar_documento(nome_arquivo):
    with open(nome_arquivo, 'rb') as f:
        conteudo = f.read()
    
    # Assinar o conteúdo usando a chave privada A
    assinatura = rsa.sign(conteudo, chave_privada_A, 'SHA-256')
    
    # Salvar a assinatura em um arquivo binário
    with open('assinatura.bin', 'wb') as f:
        f.write(assinatura)
    
    print("Documento assinado e assinatura salva em 'assinatura.bin'.")

# Faça o upload do documento para assinatura
print("Parte 2: Faça o upload do documento para assinatura:")
nome_arquivo = upload_arquivo()

# Assinar o documento carregado
assinar_documento(nome_arquivo)

Parte 2: Faça o upload do documento para assinatura:
documento.txt.txt
documento.txt.txt(text/plain) - 0 bytes, last modified: 12/11/2024 - 100% done
Saving documento.txt.txt to documento.txt.txt
Arquivo 'documento.txt.txt' carregado com sucesso!
Documento assinado e assinatura salva em 'assinatura.bin'.

# Parte 3: Validação da assinatura usando a chave pública A
def validar_documento(nome_arquivo, caminho_assinatura, chave_publica):
    with open(nome_arquivo, 'rb') as f:
        conteudo = f.read()
    with open(caminho_assinatura, 'rb') as f:
        assinatura = f.read()
    
    try:
        # Validar a assinatura
        rsa.verify(conteudo, assinatura, chave_publica)
        print("Assinatura válida: O documento é de autoria do usuário.")
    except rsa.VerificationError:
        print("Assinatura inválida: O documento NÃO é de autoria do usuário.")

# Validar o documento usando a chave pública A
print("\nParte 3: Validando o documento com a chave pública A:")
validar_documento(nome_arquivo, 'assinatura.bin', chave_publica_A)

Parte 3: Validando o documento com a chave pública A:
Assinatura válida: O documento é de autoria do usuário.

# Parte 4: Testar a validação com a chave pública B
def validar_com_chave_B(nome_arquivo):
    print("\nParte 4: Tentando validar com a chave pública B:")
    validar_documento(nome_arquivo, 'assinatura.bin', chave_publica_B)

# Validar com a chave pública B
validar_com_chave_B(nome_arquivo)

Parte 4: Tentando validar com a chave pública B:
Assinatura inválida: O documento NÃO é de autoria do usuário.