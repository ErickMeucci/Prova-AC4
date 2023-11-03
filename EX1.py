def calcular_pagamentos(dívida_total, valor_mensal):
    pagamento = 1

    while dívida_total > 0:
        valor_anterior = dívida_total
        if valor_mensal >= dívida_total:
            dívida_total = 0
        else:
            dívida_total -= valor_mensal
        print(f"pagamento: {pagamento}")
        print(f"antes = {int(valor_anterior)}")
        print(f"depois = {int(dívida_total)}")
        print("-----")
        pagamento += 1

# Solicitar entrada do usuário
dívida_total = int(input())
valor_mensal = int(input())

# Chamar a função para calcular os pagamentos
calcular_pagamentos(dívida_total, valor_mensal)


        
