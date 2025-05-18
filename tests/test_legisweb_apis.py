import json
import os
import sys
from dotenv import load_dotenv

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from legiswebapi.legisweb_client import LegiswebClient

load_dotenv()

token = os.getenv("LEGISWEB_TOKEN")
codigo_cliente = os.getenv("LEGISWEB_CODIGO_CLIENTE")

client = LegiswebClient(token, codigo_cliente)

# Execução dos testes com parâmetros específicos
testes = []

# API ICMS
testes.append(("consulta_icms", {"ncm": "90318099", "estado": "SP"}))

# API IPI
testes.append(("consulta_ipi", {"ncm": "21069030"}))

# API II
testes.append(("consulta_ii", {"ncm": "21069030"}))

# API PIS/COFINS (requer regime e atividade)
testes.append(("consulta_piscofins", {
    "ncm": "22030000",
    "regime_tributario_origem": "2",  # Lucro Real
    "atividade_origem": "3", # Fabricante
}))

# API ST Interna
testes.append(("consulta_st_interna", {
    "ncm": "22030000",
    "estado": "SP"
}))

# API ST Interestadual
testes.append(("consulta_st_interestadual", {
    "ncm": "22030000",
    "uf_origem": "SP",
    "uf_destino": "MG",
    "destinacao": 1  # Comercialização
}))

# API consulta sem similar nacional
testes.append(("consulta_produto_ssn", {
    "ncm": "22030000"
}))

# API consulta pauta fiscal
testes.append(("consulta_pauta_fiscal", {
    "estado": "SP",
    "opcao": 5,
    "busca": "Cerveja"
}))

# API consulta aliquota padrão
testes.append(("consulta_aliquota_padrao", {
    "estado": "SP"
}))

# API agenda tributária
testes.append(("consulta_agenda_tributaria", {
    "data": "23/05/2025",
    "incluir_estadual": True,
    "estado": "SP"
}))

# API consulta empresa
testes.append(("consulta_empresa", {
    "empresa": "29979036000140"
}))

# Executa os testes
for metodo, params in testes:
    try:
        print(f"Consultando {metodo} com parâmetros: {params}")
        resposta = getattr(client, metodo)(**params)
        identificador = "_".join([str(v).replace("/", "-") for v in params.values()])
        arquivo = f"output\\{metodo}_{identificador}.json"
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(resposta, f, indent=4, ensure_ascii=False)
        print(f"> Resultado salvo em {arquivo}\n")

    except Exception as e:
        print(f"> Erro ao consultar {metodo} com parâmetros {params}: {e}")
