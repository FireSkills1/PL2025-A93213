import sys


def calcular_soma(linha):
    soma = 0
    ativo = True
    tokens = iter(linha.lower().split())

    for token in tokens:
        if token == "on":
            ativo = True
        elif token == "off":
            ativo = False
        elif token == "=":
            print(soma)
            soma = 0
        else:
            try:
                numero = int(token)
                if ativo:
                    soma += numero
            except ValueError:
                continue

    print(soma)


if __name__ == "__main__":
    for entrada in sys.stdin:
        calcular_soma(entrada.strip())