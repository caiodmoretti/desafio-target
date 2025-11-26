import json
import uuid


caminho_dados_estoque = "./fonteDados/estoque.json"

try:
    with open(caminho_dados_estoque, 'r',encoding='utf-8') as file:
        dados = json.load(file)

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")

dados_estoque = {}

for item in dados["estoque"]:
    codigoProduto = str(item["codigoProduto"])
    quantidade = item["estoque"]
    
    dados_estoque[codigoProduto] = quantidade

historico_movimentacao = []

def registrar_movimentacao(codigo, tipo, quantidade):
    movimentacao_id = gerar_id()
    historico_movimentacao.append({
        "id": movimentacao_id,
        "codigo": codigo,
        "tipo": tipo,
        "quantidade": quantidade
    })
    return movimentacao_id

def gerar_id():
    return uuid.uuid4().hex[:8]

def entradaProduto(codigo, quantidade):
    dados_estoque[codigo] += quantidade
    registrar_movimentacao(codigo, "entrada", quantidade)
    return dados_estoque[codigo]

def saidaProduto(codigo, quantidade):
    if quantidade > dados_estoque[codigo]:
        raise ValueError("Estoque insuficiente")
    dados_estoque[codigo] -= quantidade
    registrar_movimentacao(codigo, "saida", quantidade)
    return dados_estoque[codigo]


#exemplo de uso
print("Quantidade final do produto: ",entradaProduto("101", 50))

print("Quantidade final do produto: ", saidaProduto("101",75))


print(historico_movimentacao)