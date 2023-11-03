# Solicitar entrada dos números inteiros A e B
A = int(input())
B = int(input())

# Verificar se A é maior que B
if A > B:
    print("Nenhuma tabuada no intervalo!")
else:
    for i in range(A, B + 1):
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print("----------")
