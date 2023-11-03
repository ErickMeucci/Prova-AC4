# Função para verificar se um número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Solicitar entrada dos números naturais INÍCIO e FIM
INICIO = int(input())
FIM = int(input())

# Inicializar uma lista para armazenar os números primos encontrados
primos = []

# Inicializar um contador
numero = INICIO

# Encontrar e armazenar os números primos no intervalo usando um loop while
while numero <= FIM:
    if eh_primo(numero):
        primos.append(numero)
    numero += 1

# Exibir os números primos encontrados
if len(primos) > 0:

    for primo in primos:
        print(primo)


# Exibir a quantidade de números primos encontrados
print(f"primos: {len(primos)}")
