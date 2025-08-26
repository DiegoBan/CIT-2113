from scapy.all import IP, ICMP, send
import sys
import time

if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    message = input("Introduce un string: ")

BASE_PATTERN = bytes.fromhex(
    "00 00 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d"
    " 1e 1f 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d"
    " 2e 2f 30 31 32 33 34 35 36 37"
)
IP_dest = "8.8.8.8"
DELAY = 0.1

toSend = message.encode("utf-8")
print(f"Enviando {len(toSend)} paquetes ICMP a {IP_dest}...")
for i, b in enumerate(toSend, 1):
    payload = bytes([b]) + BASE_PATTERN
    pkt = IP(dst=IP_dest)/ICMP()/payload
    send(pkt, verbose=True)
    print(f"{i}/{len(toSend)} -> enviado byte=0x{b:02x}")
    time.sleep(DELAY)