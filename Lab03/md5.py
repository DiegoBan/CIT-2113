import hashlib

s = input("Introduce la cadena: ")
md5_hex = hashlib.md5(s.encode('utf-8')).hexdigest()
print(md5_hex)