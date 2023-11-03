# Lista para armazenar os tempos de corrida
tempos_de_corrida = []

# Ler os tempos de corrida da entrada
while True:
    tempo = int(input())
    if tempo < 0:
        break
    tempos_de_corrida.append(tempo)

# Calcular a média dos tempos de corrida
media = sum(tempos_de_corrida) / len(tempos_de_corrida)

# Exibir a média
print(f"MEDIA: {media:.2f}")

# Exibir os tempos de corrida abaixo da média
for tempo in tempos_de_corrida:
    if tempo < media:
        print(tempo)
