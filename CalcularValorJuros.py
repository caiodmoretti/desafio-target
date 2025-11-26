from datetime import date,datetime

TAXA_DIARIA = 0.025


def calcularJurosComposto(valor, dataVencimento):
    data = datetime.strptime(dataVencimento, "%Y-%m-%d").date()
    quantiadeDias = abs((date.today() - data).days)
    montante = valor * (1 + TAXA_DIARIA)**quantiadeDias
    return round(montante,2)

print(calcularJurosComposto(100,"2025-11-25"))
