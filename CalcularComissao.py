import json
from decimal import Decimal



caminho_dados_vendas = "./fonteDados/vendas.json"

try:
    with open(caminho_dados_vendas, 'r',encoding='utf-8') as file:
        dados = json.load(file)

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")

totais = {}

for item in dados["vendas"]:
    vendedor = item["vendedor"]
    valor = Decimal(str(item["valor"]))

    if valor < 100:
        comissao = Decimal("0")
    elif valor < 500:
        comissao = valor * Decimal("0.01")
    else:
        comissao = valor * Decimal("0.05")

    if vendedor not in totais:
        totais[vendedor] = Decimal("0")

    totais[vendedor] += comissao


for vendedor, comissao in totais.items():
    print(vendedor, f"{comissao:.2f}")


