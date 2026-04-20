import json
import os

ARQUIVO_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados_plantio.json")
TAXA_FERTILIZANTE = {"milho": 0.300, "soja": 0.200}

dados = {"milho": [], "soja": []}


def salvar_json():
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"Dados exportados para {ARQUIVO_JSON}")


def calcular_registro(tamanho, ruas, taxa):
    area = tamanho ** 2
    fert_rua = tamanho * taxa
    fert_total = fert_rua * ruas
    return {"tamanho": tamanho, "area": area, "ruas": ruas,
            "fert_rua": fert_rua, "fert_total": fert_total}


def ler_cultura(prompt="Digite Milho ou Soja: "):
    cultura = input(prompt).strip().lower()
    if cultura not in TAXA_FERTILIZANTE:
        print("Cultura inválida. Tente Milho ou Soja.")
        return None
    return cultura


def mostrar_registro(i, reg):
    print(f"  Posição {i} | Tamanho={reg['tamanho']}m | Área={reg['area']}m² "
          f"| Ruas={reg['ruas']} | Fert/rua={reg['fert_rua']}L "
          f"| Fert total={reg['fert_total']}L")


def cadastrar():
    cultura = ler_cultura(
        "Digite Milho ou Soja para calcular área e fertilizante: ")
    if not cultura:
        return
    taxa = TAXA_FERTILIZANTE[cultura]
    tamanho = float(input(f"Comprimento do plantio de {cultura.title()} (m): "))
    ruas = int(input("Quantas ruas há na plantação? "))
    reg = calcular_registro(tamanho, ruas, taxa)
    dados[cultura].append(reg)
    salvar_json()
    print(f"Área: {reg['area']}m². "
          f"Sendo {int(taxa * 1000)}ml/m, por rua: {reg['fert_rua']}L, "
          f"total: {reg['fert_total']}L.")


def mostrar():
    if not any(dados.values()):
        print("Não há dados ainda.")
        return
    for cultura, registros in dados.items():
        print(f"\n=== Dados de {cultura.title()} ===")
        for i, reg in enumerate(registros):
            mostrar_registro(i, reg)


def editar():
    cultura = ler_cultura("Editar dados de Milho ou Soja? ")
    if not cultura:
        return
    registros = dados[cultura]
    if not registros:
        print("Não há dados dessa cultura.")
        return
    pos = int(input("Posição do registro: "))
    if not 0 <= pos < len(registros):
        print("Posição inválida.")
        return
    tamanho = float(input("Novo tamanho: "))
    ruas = int(input("Novo número de ruas: "))
    registros[pos] = calcular_registro(tamanho, ruas, TAXA_FERTILIZANTE[cultura])
    salvar_json()
    print("Dados atualizados com sucesso.")


def excluir():
    cultura = ler_cultura("Excluir dados de Milho ou Soja? ")
    if not cultura:
        return
    registros = dados[cultura]
    if not registros:
        print("Não há dados dessa cultura.")
        return
    pos = int(input("Posição do registro: "))
    if not 0 <= pos < len(registros):
        print("Posição inválida.")
        return
    registros.pop(pos)
    salvar_json()
    print("Dados deletados com sucesso.")


MENU = """
==== BEM VINDO AO PROGRAMA TECNOLÓGICO DE MELHORA AGRÍCOLA ====
1 - Cálculo de área e de insumos
2 - Mostrar dados
3 - Editar dados
4 - Excluir dados
5 - Sair do programa
"""

ACOES = {"1": cadastrar, "2": mostrar, "3": editar, "4": excluir}

while True:
    print(MENU)
    escolha = input("Escolha uma opção: ").strip()
    if escolha == "5":
        salvar_json()
        print("Saindo do programa.")
        break
    acao = ACOES.get(escolha)
    if acao:
        acao()
    else:
        print("Opção inválida.")