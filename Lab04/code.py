from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
import base64

#   Agregar bytes faltantes o eliminar sobrantes
def to_bytes_config(txt, num_bytes):
    txt = txt.encode("utf-8")
    length = len(txt)
    if length > num_bytes:
        txt = txt[:num_bytes]
    elif length < num_bytes:
        txt = txt + get_random_bytes(num_bytes - length)
    return txt

#   Funciones de padding faltantes en librería
#   Usando estándar de padding PKCS#7
def pad(txt, block_size):
    pad_len = block_size - (len(txt) % block_size)
    padding = bytes([pad_len]) * pad_len
    return txt + padding
def unpad(txt, block_size):
    pad_len = txt[-1]
    if pad_len > block_size:
        raise ValueError("Padding incorrecto")
    return txt[:-pad_len]

#   Verificación IV: Este debe tener la misma cantidad de bytes que el bloque
def IV_verification(IV, opt):
    IV = IV.encode("utf-8")
    length = len(IV)
    if (length != 8 and (opt == 1 or opt == 2)) or (length != 16 and opt == 3):
        raise ValueError("Largo de IV ingresado incorrecto!")

#   Sección: DES
def DES_encrypt(txt, key, IV):
    txt = txt.encode("utf-8")
    enc = DES.new(key, DES.MODE_CBC, IV)
    txt = pad(txt, DES.block_size)
    return enc.encrypt(txt)
def DES_decrypt(txt_encrypted, key, IV):
    deenc = DES.new(key, DES.MODE_CBC, IV)
    return unpad(deenc.decrypt(txt_encrypted), DES.block_size).decode("utf-8")

#   Sección: 3DES
def DES3_encrypt(txt, key, IV):
    txt = txt.encode("utf-8")
    enc = DES3.new(key, DES3.MODE_CBC, IV)
    txt = pad(txt, DES3.block_size)
    return enc.encrypt(txt)
def DES3_decrypt(txt_encrypted, key, IV):
    deenc = DES3.new(key, DES3.MODE_CBC, IV)
    return unpad(deenc.decrypt(txt_encrypted), DES3.block_size).decode("utf-8")

#   Sección AES-256
def AES256_encrypt(txt, key, IV):
    txt = txt.encode("utf-8")
    enc = AES.new(key, AES.MODE_CBC, IV)
    txt = pad(txt, AES.block_size)
    return enc.encrypt(txt)
def AES256_decrypt(txt_encrypted, key, IV):
    deenc = AES.new(key, AES.MODE_CBC, IV)
    return unpad(deenc.decrypt(txt_encrypted), AES.block_size).decode("utf-8")

print("===================\n===== Ingreso =====\n===================\n")
print("==== DES ====")
DES_key = input("Key para DES (8 bytes): ")
DES_IV = input("IV para DES (8 bytes): ")
IV_verification(DES_IV, 1)
print("==== 3DES ====")
DES3_key = input("Key para 3DES (24 bytes): ")
DES3_IV = input("IV para 3DES (8 bytes): ")
IV_verification(DES3_IV, 2)
print("==== AES ====")
AES256_key = input("Key para AES-256 (32 bytes): ")
AES256_IV = input("IV para AES-256 (16 bytes): ")
IV_verification(AES256_IV, 3)
print("==== Texto ====")
text = input("Texto a cifrar: ")

print("\n=======================\n==== Procesando... ====\n=======================\n")
#   DES
DES_key = to_bytes_config(DES_key, 8)
print(f"Clave a utilizar para DES (bytes): {DES_key}")
#   3DES
DES3_key = to_bytes_config(DES3_key, 24)
print(f"Clave a utilizar para 3DES (bytes): {DES3_key}")
#   AES256
AES256_key = to_bytes_config(AES256_key, 32)
print(f"Clave a utilizar para AES-256 (bytes): {AES256_key}")

print("\n========================\n==== Encriptando... ====\n========================\n")
#   DES
DES_encrypted = DES_encrypt(text, DES_key, DES_IV)
DES_encrypted_b64 = base64.b64encode(DES_encrypted).decode("utf-8")
print(f"Texto encriptado con DES (base64): {DES_encrypted_b64}")
print(f"Texto encriptado con DES (HEX): {DES_encrypted.hex()}\n")
#   3DES
DES3_encrypted = DES3_encrypt(text, DES3_key, DES3_IV)
DES3_encrypted_b64 = base64.b64encode(DES3_encrypted).decode("utf-8")
print(f"Texto encriptado con 3DES (base64): {DES3_encrypted_b64}")
print(f"Texto encriptado con 3DES (HEX): {DES3_encrypted.hex()}\n")
#   AES256
AES256_encrypted = AES256_encrypt(text, AES256_key, AES256_IV)
AES256_encrypted_b64 = base64.b64encode(AES256_encrypted).decode("utf-8")
print(f"Texto encriptado con AES-256 (base64): {AES256_encrypted_b64}")
print(f"Texto encriptado con AES-256 (HEX): {AES256_encrypted.hex()}")

print("\n===========================\n==== Desencriptando... ====\n===========================\n")
#   DES
DES_decrypted = DES_decrypt(DES_encrypted, DES_key, DES_IV)
print(f"Texto desencriptado con DES: {DES_decrypted}")
#   3DES
DES3_decrypted = DES3_decrypt(DES3_encrypted, DES3_key, DES3_IV)
print(f"Texto desencriptado con 3DES: {DES3_decrypted}")
#   AES256
AES256_decrypted = AES256_decrypt(AES256_encrypted, AES256_key, AES256_IV)
print(f"Texto desencriptado con AES-256: {AES256_decrypted}")