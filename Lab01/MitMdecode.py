import sys
import re
from scapy.all import rdpcap, IP, ICMP

if len(sys.argv) < 2:
    print("Uso: python3 MitMdecode_cesar_lineal_detect_shift.py archivoCaptura.pcapng")
    sys.exit(1)

pcap_file = sys.argv[1]

# leer pcap
try:
    packets = rdpcap(pcap_file)
except FileNotFoundError:
    print("Archivo no encontrado:", pcap_file)
    sys.exit(1)
except Exception as e:
    print("Error al leer pcap:", e)
    sys.exit(1)

# reconstruir bytes (primer byte del payload de cada ICMPv4)
raw_b = bytearray()
for pkt in packets:
    if pkt.haslayer(IP) and pkt.haslayer(ICMP):
        payload = bytes(pkt[ICMP].payload)
        if len(payload) > 0:
            raw_b.append(payload[0])

# decodificar (utf-8 preferido, latin1 fallback)
try:
    mensaje = raw_b.decode("utf-8")
except Exception:
    mensaje = raw_b.decode("latin1")

print("Mensaje reconstruido (sin descifrar):")
print(mensaje)
print("\nProbando corrimientos César (0-25):\n")

# diccionario pequeño (español + inglés)
COMMON_WORDS = {
    "de","la","que","el","en","y","a","los","se","del","las","un","por","con",
    "no","una","su","para","es","al","lo","como","mas","pero","sus","le","ya",
    "o","este","si","porque","esta","entre","cuando","muy","sin","sobre","tambien",
    "me","hasta","hay","donde","quien","desde","todo","nos","durante","ni","contra",
    "yo","tu","el","ella","ellos","estas","esto","mundo","mensaje","hola",
    "the","be","to","of","and","a","in","that","have","i","it","for","not","on",
    "with","he","as","you","do","at","this","but","his","by","from","they","we",
    "say","her","she","or","an","will","my","one","all","would","there","their",
    "hello","hi","flag","secret","password","key","test","ok","success","error"
}

# probar los 26 shifts y puntuar cada candidato
candidates = []
for shift in range(26):
    # construir candidato aplicando shift a cada char (solo A-Z / a-z)
    chars = []
    for c in mensaje:
        oc = ord(c)
        if 97 <= oc <= 122:  # a-z
            nc = (oc - 97 + shift) % 26 + 97
            chars.append(chr(nc))
        elif 65 <= oc <= 90:  # A-Z
            nc = (oc - 65 + shift) % 26 + 65
            chars.append(chr(nc))
        else:
            chars.append(c)
    cand = "".join(chars)

    # tokenizar por secuencias no-alfabéticas (incluimos letras acentuadas y ñ)
    tokens = re.split(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ]+', cand)

    score = 0
    recognized = 0
    total_alpha_tokens = 0
    for t in tokens:
        if not t:
            continue
        # consideramos token "alfabético" si contiene al menos una letra (incl acentos/ñ)
        if re.search(r'[A-Za-zÁÉÍÓÚáéíóúÑñ]', t):
            total_alpha_tokens += 1
            lower = t.lower()
            # normalizar acentos/ñ a formas base para matching simple
            lower_norm = (lower.replace("á","a").replace("é","e").replace("í","i")
                                .replace("ó","o").replace("ú","u").replace("ñ","n")
                                .replace("ü","u"))
            if lower in COMMON_WORDS or lower_norm in COMMON_WORDS:
                recognized += 1
                score += 1

    # bonus por longitud del mensaje (ligero)
    extra = min(len(cand) // 50, 2)
    total_score = score + extra

    candidates.append((shift, cand, total_score, recognized, total_alpha_tokens))

# elegir mejor candidato por (score, recognized)
best = max(candidates, key=lambda x: (x[2], x[3]))

# deducir corrimiento de descifrado y corrimiento original de cifrado
decryption_shift = best[0]                       # shift que aplicamos al cifrado para obtener claro
encryption_shift = (26 - decryption_shift) % 26  # shift original que aplicó el emisor

# imprimir todos los candidatos; el mejor en verde
GREEN = "\033[92m"
RESET = "\033[0m"

for shift, cand, total_score, recognized, total_alpha_tokens in sorted(candidates, key=lambda x: x[0]):
    if shift == best[0]:
        print(f"{GREEN}Shift={shift:2d} | score={total_score:2d} | recog={recognized}/{total_alpha_tokens:2d}: {cand}{RESET} <-- opción más probable")
    else:
        print(f"Shift={shift:2d} | score={total_score:2d} | recog={recognized}/{total_alpha_tokens:2d}: {cand}")

print("\nResultado más probable (marcado en verde):")
print(f"Shift de descifrado detectado = {decryption_shift} (aplicado al texto cifrado para obtener este candidato).")
print(f"Corrimiento original aplicado por el emisor = {encryption_shift} (si se usó Caesar estándar).")
print(f"Puntuación = {best[2]}, reconocidos = {best[3]}/{best[4]}")
print(GREEN + best[1] + RESET)