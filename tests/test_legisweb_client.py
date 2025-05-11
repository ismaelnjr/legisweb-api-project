
import pytest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from legiswebapi.legisweb_client import LegiswebClient

@pytest.fixture
def client():
    return LegiswebClient(token="fake_token", codigo_cliente="9999")

def mock_api(requests_mock, endpoint, response):
    requests_mock.get(f"https://www.legisweb.com.br/api/{endpoint}", json=response)

def test_consulta_ii(client, requests_mock):
    mock_api(requests_mock, "ii", {"registros": 1, "resposta": [{"ncm": "21069030"}]})
    result = client.consulta_ii("21069030")
    assert result["registros"] == 1

def test_consulta_ipi(client, requests_mock):
    mock_api(requests_mock, "ipi", {"registros": 1, "resposta": [{"ncm": "21069030"}]})
    result = client.consulta_ipi("21069030")
    assert result["registros"] == 1

def test_consulta_icms(client, requests_mock):
    mock_api(requests_mock, "icms", {"registros": 1, "resposta": [{"estado": "SP"}]})
    result = client.consulta_icms("21069030", "SP")
    assert result["resposta"][0]["estado"] == "SP"

def test_consulta_piscofins(client, requests_mock):
    mock_api(requests_mock, "piscofins", {"registros": 1})
    result = client.consulta_piscofins("21069030", 1, 1)
    assert result["registros"] == 1

def test_consulta_piscofins_importacao(client, requests_mock):
    mock_api(requests_mock, "piscofins-importacao", {"registros": 1})
    result = client.consulta_piscofins_importacao("21069030")
    assert result["registros"] == 1

def test_consulta_tipi(client, requests_mock):
    mock_api(requests_mock, "tipi", {"registros": 1})
    result = client.consulta_tipi("21069030")
    assert result["registros"] == 1

def test_consulta_st_interna(client, requests_mock):
    mock_api(requests_mock, "st-interna", {"registros": 1})
    result = client.consulta_st_interna("21069030", "SP")
    assert result["registros"] == 1

def test_consulta_st_interestadual(client, requests_mock):
    mock_api(requests_mock, "st-interestadual", {"registros": 1})
    result = client.consulta_st_interestadual("21069030", "SP", "RJ", 1)
    assert result["registros"] == 1

def test_consulta_preferencia_tarifaria(client, requests_mock):
    mock_api(requests_mock, "preferencia-tarifaria", {"registros": 1})
    result = client.consulta_preferencia_tarifaria("21069030", 1, 15)
    assert result["registros"] == 1

def test_consulta_nve(client, requests_mock):
    mock_api(requests_mock, "nve", {"registros": 1})
    result = client.consulta_nve("21069030")
    assert result["registros"] == 1

def test_consulta_ptax(client, requests_mock):
    mock_api(requests_mock, "ptax", {"registros": 1})
    result = client.consulta_ptax("94", "01/01/2024")
    assert result["registros"] == 1

def test_consulta_defesa_comercial(client, requests_mock):
    mock_api(requests_mock, "defesa-comercial", {"registros": 1})
    result = client.consulta_defesa_comercial("01012100")
    assert result["registros"] == 1

def test_consulta_cide_combustivel(client, requests_mock):
    mock_api(requests_mock, "cide-combustivel", {"registros": 1})
    result = client.consulta_cide_combustivel("01012100")
    assert result["registros"] == 1

def test_consulta_tratamento_adm_importacao(client, requests_mock):
    mock_api(requests_mock, "tratamento-administrativo-importacao", {"registros": 1})
    result = client.consulta_tratamento_adm_importacao("01012100")
    assert result["registros"] == 1

def test_consulta_tratamento_adm_exportacao(client, requests_mock):
    mock_api(requests_mock, "tratamento-administrativo-exportacao", {"registros": 1})
    result = client.consulta_tratamento_adm_exportacao("01012100")
    assert result["registros"] == 1

def test_consulta_produto_ssn(client, requests_mock):
    mock_api(requests_mock, "produto-ssn", {"registros": 1})
    result = client.consulta_produto_ssn("01012100")
    assert result["registros"] == 1

def test_consulta_correlacao_ncm(client, requests_mock):
    mock_api(requests_mock, "correlacao-nbm-ncm-naladi", {"registros": 1})
    result = client.consulta_correlacao_ncm("01012100", "NCM - 2002", "NALADI - 2017")
    assert result["registros"] == 1

def test_consulta_pauta_fiscal(client, requests_mock):
    mock_api(requests_mock, "pauta-fiscal", {"registros": 1})
    result = client.consulta_pauta_fiscal("SP", "cerveja")
    assert result["registros"] == 1

def test_consulta_agenda_tributaria(client, requests_mock):
    mock_api(requests_mock, "agenda-tributaria", {"registros": 1})
    result = client.consulta_agenda_tributaria("01/01/2024", "SP")
    assert result["registros"] == 1

def test_consulta_beneficio_fiscal(client, requests_mock):
    mock_api(requests_mock, "beneficio-fiscal", {"registros": 1})
    result = client.consulta_beneficio_fiscal("moinho", "SP", 2)
    assert result["registros"] == 1

def test_consulta_empresa(client, requests_mock):
    mock_api(requests_mock, "empresas", {"registros": 1})
    result = client.consulta_empresa("10750466000168")
    assert result["registros"] == 1

def test_consulta_cfop(client, requests_mock):
    mock_api(requests_mock, "cfop", {"registros": 1})
    result = client.consulta_cfop("5201")
    assert result["registros"] == 1

def test_consulta_aliquota_padrao(client, requests_mock):
    mock_api(requests_mock, "aliquota-padrao", {"registros": 1})
    result = client.consulta_aliquota_padrao("SP")
    assert result["registros"] == 1
