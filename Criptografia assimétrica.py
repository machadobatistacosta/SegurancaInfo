Questão 1 
Crie um programa que gere um par de chaves privada e pública relacionadas.  
Exiba o valor do módulo e dos expoentes de cada chave gerada. 
Salve cada uma das chaves num arquivo separado, pois as chaves precisarão ser recuperadas nas questões seguintes. 
Qual é o expoente e o módulo do par de chaves gerados?

Módulo: 27015189443743614140572373718157484622042113768217126863469837214702135312501243870654289430104826560328779169865995145806561135439174537741400903953431456164528143071002389718889908654273441737613486783431544897759625623270489762716448092381639830205499194964099382110069484741507215422467327312715270763575479040873583016147392148809424251110229568966376787020450887512215347701169892451788238503508915417242482523920710016887320514585834146384580557684611631452576761277311528841530321409775864230353274352762027574881948077271694987284138193203265365065372035000060693399987699856100176660981332452103088820472891
Expoente público: 65537
Expoente privado: 7408082107637492737343735817566675845477056435075058294197906213345429677413004931892878259504232578985132899755050303841533995232389721913111469023591153309745907246296282204449852653924884541366262992331660117644797776654494511049615436962885701337231316390700093772847608908433357064938455724254428620894926388006165076492168946323188140027581019855155281634627427134206808182776321027736443902008923880179078978206424207328164968281234496136725943044035472377170014267561920249745347579199911672208334092335146528257348744907592552502371186368974148143439264646207222508346020729606329128562880621587567833063197

Questão 2 
Crie um programa que criptografe um arquivo submetido pelo usuário utilizando o algoritmo AES.  
Criptografe a chave simétrica (do algoritmo AES) utilizando a chave pública gerada na questão 1. 
Qual é o texto simples e o texto cifrado pelo algoritmo RSA?

Texto simples (conteúdo do arquivo): -----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1gBjxRO13CBvH9rRLRTw
FjgMxYWr26m9B2eNm5IpRRqz+ce9YXVxbKbkuuPhxZ/ebG7tBmDEXVJbsU2ulZAG
eVwtyZR3t9WjWQxtaDgwbmUgI/G1NlH/QAivbSiyIWX3JgyI3CaSViCTB/XUcE1p
buwYVfeZXojA5HDLtKMEP6n+CqTMdeAOKcKUeNsj/yFCV1OjpHsB0rHbCk6QVAYq
YRk9oJ+m8nDxkT7rcpmQFQK2qSj7hdW3r12yWvtJPlCsl3n1RUC6C9bb5hwId06B
1lhEI/1sYFeXLyRwQpJi2GIswmphXDCCRZiUFoEB2b0ZnqcqhRQrc5zKwS0779BM
OwIDAQAB
-----END PUBLIC KEY-----
Texto cifrado (AES): b'\xe3V\x18d\xe0\x1f\xdf\xc3\xcal\x05\xee\xbd\x9bS[\x0e\xd3\xd9\x0e\x9e\x17o@\x15\xd1\xfe$\xb5\xab*\x1f\xfa\xffE/\xfaK\xb5\xc8\xba\x81\xc1\x87(3\xae\xb7P\xb4y#\xbe\x00\xb9\xff\x02=kY\xaa\x98\xd5\x0f.9\xe4\xbd\x93p]\x17\xba\xc0\x7f\xcd`\xbb1\x99\xfds<\xbe\xaa\xe5\xce\xe6\xd0\x10\x1f\x13)I\xea\xc6f\xaa\x05\x18\xff\x8c\xc8O\x88a-\xa3n\xfd)\xecf*y^~\xc7\x9bl\x8ah6\xbf\xc4\xf0F\xfal\xaf\xeb\xb7\xda\xaf\xd8\xa1U\x84x}\x93M\x81\t7(\xae*\xbb\x94\\\xa2Vs\xc1\xb1e4\xdcIvo\xf4\xff\xcf\x8a\xe4sLH\xfc\xbd6H\xba\xf5\xb4J\xbb:\xa9\xb0\x02Z\xab\x08\x04r\x930\xb7\xbc\x851\x15T\xcbm3\xb9\xbc\x05:\x9aQ\x92_\xce\xe0\xd3\xa8$8\xba\xbf5\xb4e\x8d\xd4\xa0\x86\xeanH\xeb\xdc\xf0\xbe7\xb9e!\xbaB\x02\x97\xe5|\xdd\xfe^\xd5\xedm\xbbL\xc3\x8d\xa1`\xef0\x97\xe4,\x13GJ\xb2"\x91f\x94\xd8\xba\xc4\x02\x99\x1d\xb6\xc3\xfe&\xba\x89#@lb\xdak\x0c!\x9fp\x8f\x89\x139\xd6X!3\x97\xb3;$3\x18]\xeeu\xf8\xef4\x98P\x02\xc8\xbf\xe5\xb5\xcc\x8e+\xc86\xb8t\xc7\xba\xde\xb3\xa6\xedGl\xda\xd7AZ\xd0\xa4\x19"o\xd0\x87\x11\x88l\x05X\xbeE\x8b\xfd`\x87\xc7K]\x94\xf7\x83\xcf\x99"\xe9\x9dU\x08\x08+\x14&\x00^\x98\x03\x96Y2hI-\xd3\x9a\x98\xe2\xaf\x035\x0eVy)\x1fa3\x12\xe2\xb7-u\x92\xf2\x19\xf5\x97\xd2\x045\xfd\xc1wy3\xd8\xcf\xc6p\x14{\xdd/\xab01\x1f<\'T\x00\x90_\xe5\x1b\xd8s?\x91\xdd\xd9\x83\x8c\xf5\x1eI\xff\x05rj\xd3\x0c\xd8\xc3\x05\xf4'
Chave AES criptografada com RSA: b'\xa5\xd4)+\x90\x06C\x94+\xa3\xbd\x0e\xf6\xd3\xcf\xc3\xc2\x1bk[\xf8\xad\x1a\x08\x01\xa4\x9fp\x92F\x84\xfc5\xc6\xc1e\xfc\xfcn\x0b<g\xb8\x97\xa1\x13\xd7:kc\x9f&\x9d\xb1\x1d,\x04\xe5\xa9\xe7c\xd1QQk\x92\x1c\xfex\x96\x99Y\xcde\xbfJ(k\xcf\xa9\xc3\xbcJ\xd4\xf8\xf3${\x93\xa8\xca\xf9\xe7X)q#vc\x1bm\xfb\xd4hU\xf5\xfe\xd4o\x1c\xb1\xd3;\x0f\xf5M\x01Z6\xb9A\x9b\xe5\xf39"\xd1\xb3JBF\xb8\xf7;6\xb2$,I\xac\xc4\xffE\xae\xf5\xc4\x0c\xba\x96d\xfaH\xcbvq\x021M\x90\xd1I\x14E\xc6\x81D\xefO\x91\xdf\xbb\xb7/,\xcdv\x8bD\x17\xdaN\xa2g\xce\x19\xb6l<\xf0\xbd\xef\xad\xcb\x00\xa2\xf1\xce_\xea\xd5\x92\xec\xf4\xe0_h\xde\x86KI\xdb\xc6u=\x7fuS\xb1\x0bp=\xa1\x82\xf3\xa6\x96\'\x1bv\xed\x1e\xfa\xaal\xc9\xca\xa1]\x1a\xf4\x96}\x87\x04]\x8d\xb5d\x95\x00\xe1\xe6G7\xf6\xb1'

Questão 3 
Crie um programa que decriptografe a chave de um algoritmo AES, utilizando a chave simétrica gerada na questão 2. 
Será preciso recorrer a chave privada, gerada na questão 1, para poder decifrar a chave. 
Decriptografe o arquivo utilizando a chave obtida. 

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1gBjxRO13CBvH9rRLRTw
FjgMxYWr26m9B2eNm5IpRRqz+ce9YXVxbKbkuuPhxZ/ebG7tBmDEXVJbsU2ulZAG
eVwtyZR3t9WjWQxtaDgwbmUgI/G1NlH/QAivbSiyIWX3JgyI3CaSViCTB/XUcE1p
buwYVfeZXojA5HDLtKMEP6n+CqTMdeAOKcKUeNsj/yFCV1OjpHsB0rHbCk6QVAYq
YRk9oJ+m8nDxkT7rcpmQFQK2qSj7hdW3r12yWvtJPlCsl3n1RUC6C9bb5hwId06B
1lhEI/1sYFeXLyRwQpJi2GIswmphXDCCRZiUFoEB2b0ZnqcqhRQrc5zKwS0779BM
OwIDAQAB
-----END PUBLIC KEY-----


# Importando a biblioteca necessária
from Crypto.PublicKey import RSA
from google.colab import files

# Gerando o par de chaves RSA (pública e privada)
key = RSA.generate(2048)
public_key = key.publickey()

# Salvando a chave privada e a chave pública em arquivos
with open("chave_privada.pem", "wb") as f:
    f.write(key.export_key())

with open("chave_publica.pem", "wb") as f:
    f.write(public_key.export_key())

# Exibindo o módulo e os expoentes
print("Módulo:", public_key.n)
print("Expoente público:", public_key.e)
print("Expoente privado:", key.d)

# Baixando os arquivos de chaves geradas
files.download("chave_privada.pem")
files.download("chave_publica.pem")


from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from google.colab import files

# Passo 1: Upload do arquivo para ser criptografado
uploaded = files.upload()  # Carregue o arquivo

# Verifica o nome do arquivo carregado
file_name = list(uploaded.keys())[0]

# Lendo o conteúdo do arquivo (Texto Simples)
with open(file_name, "rb") as f:
    data = f.read()
print("Texto simples (conteúdo do arquivo):", data.decode())

# Gerando uma chave AES aleatória
aes_key = get_random_bytes(16)  # chave de 128 bits para AES

# Criptografando o conteúdo do arquivo com AES
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

# Salvando o texto cifrado
with open("arquivo_criptografado.bin", "wb") as f:
    f.write(cipher_aes.nonce + tag + ciphertext)
print("Texto cifrado (AES):", ciphertext)

# Carregando a chave pública RSA para criptografar a chave AES
with open("chave_publica.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Criptografando a chave AES com RSA
cipher_rsa = PKCS1_OAEP.new(public_key)
aes_key_encrypted = cipher_rsa.encrypt(aes_key)

# Salvando a chave AES criptografada
with open("chave_aes_criptografada.bin", "wb") as f:
    f.write(aes_key_encrypted)
print("Chave AES criptografada com RSA:", aes_key_encrypted)

# Baixando os arquivos de saída
files.download("arquivo_criptografado.bin")
files.download("chave_aes_criptografada.bin")


from Crypto.Cipher import AES, PKCS1_OAEP
from google.colab import files

# Passo 1: Upload dos arquivos necessários para descriptografia
uploaded = files.upload()  # Suba "chave_privada.pem", "arquivo_criptografado.bin" e "chave_aes_criptografada.bin"

# Nome dos arquivos carregados
private_key_file = "chave_privada.pem"
encrypted_file = "arquivo_criptografado.bin"
encrypted_aes_key_file = "chave_aes_criptografada.bin"

# Carregando a chave privada RSA para descriptografar a chave AES
with open(private_key_file, "rb") as f:
    private_key = RSA.import_key(f.read())

cipher_rsa = PKCS1_OAEP.new(private_key)

# Lendo a chave AES criptografada e descriptografando
with open(encrypted_aes_key_file, "rb") as f:
    aes_key_encrypted = f.read()
aes_key = cipher_rsa.decrypt(aes_key_encrypted)

# Carregando e descriptografando o arquivo criptografado com AES
with open(encrypted_file, "rb") as f:
    nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
data_decrypted = cipher_aes.decrypt_and_verify(ciphertext, tag)

# Salvando o arquivo decriptado
with open("arquivo_decriptado.txt", "wb") as f:
    f.write(data_decrypted)

# Baixando o arquivo decriptado
files.download("arquivo_decriptado.txt")

