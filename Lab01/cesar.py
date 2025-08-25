import argparse

def caesar(message: str, shift: int) -> str:
    shift = shift % 26
    out = []
    for ch in message:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            out.append(ch)
    return ''.join(out)

def main():
    parser = argparse.ArgumentParser(description="Cifrado César: desplaza sólo A-Z y a-z")
    parser.add_argument("message", nargs='+', help="Mensaje (si tiene espacios puede pasarlo sin comillas, p. ej. Hola mundo 3)")
    parser.add_argument("shift", type=int, help="Desplazamiento entero (puede ser negativo)")
    args = parser.parse_args()

    msg = " ".join(args.message)
    result = caesar(msg, args.shift)
    print(result)

if __name__ == "__main__":
    main()