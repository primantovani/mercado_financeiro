def realizar_resgate(investimentos, saldo_investimentos):
    if not investimentos:
        print("Nenhum investimento disponível para resgate.")
        return
    
    print("\nEscolha o tipo de investimento para resgate:")
    print("1. CDB")
    print("2. LCI")
    print("3. LCA")

    tipo_resgate = input("Digite o tipo de investimento (1, 2 ou 3): ")
    valor_resgate = float(input("Digite o valor a ser resgatado: "))
    dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))
    
    # Verificar se o tipo de investimento existe e se há saldo suficiente
    if tipo_resgate not in saldo_investimentos or saldo_investimentos[tipo_resgate] < valor_resgate:
        print("Saldo insuficiente ou investimento não encontrado.")
        return
    
    # Calcular imposto de renda se aplicável
    if tipo_resgate == '1':  # CDB, que é tributável
        aliquota = calcular_aliquota(dias_investidos)
        valor_imposto = valor_resgate * aliquota
        valor_liquido = valor_resgate - valor_imposto
        print(f"Imposto sobre o resgate: R${valor_imposto:.2f}")
    else:  # LCI e LCA, isentos de imposto
        valor_liquido = valor_resgate
        print("Investimento isento de imposto de renda.")

def calcular_aliquota(dias):
    """Calcula a alíquota do imposto de renda com base nos dias investidos."""
    if dias <= 180:
        return 0.225  # 22,5%
    elif dias <= 360:
        return 0.20   # 20%
    elif dias <= 720:
        return 0.175  # 17,5%
    else:
        return 0.15   # 15%     