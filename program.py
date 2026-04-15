pecas_aprovadas = []
pecas_reprovadas = []
caixas = []
caixa_atual = []

# função que verifica qualidade da peça
def verificar_qualidade(peso, cor, comprimento):
    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("Peso fora do padrão")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")

    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora do padrão")

    if len(motivos) == 0:
        return True, "Aprovada"
    else:
        return False, ", ".join(motivos)


def cadastrar_peca():
    global caixa_atual

    id_peca = input("ID da peça: ")
    peso = float(input("Peso (g): "))
    cor = input("Cor: ")
    comprimento = float(input("Comprimento (cm): "))

    aprovada, motivo = verificar_qualidade(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    if aprovada:
        pecas_aprovadas.append(peca)
        caixa_atual.append(peca)

        print("Peça APROVADA")

        if len(caixa_atual) == 10:
            caixas.append(caixa_atual)
            caixa_atual = []
            print("Caixa fechada! Nova caixa iniciada.")

    else:
        pecas_reprovadas.append((peca, motivo))
        print("Peça REPROVADA:", motivo)


def listar_pecas():
    print("\nPeças Aprovadas:")
    for p in pecas_aprovadas:
        print(p)

    print("\nPeças Reprovadas:")
    for p, motivo in pecas_reprovadas:
        print(p, "Motivo:", motivo)


def remover_peca():
    id_remover = input("Digite o ID da peça que deseja remover: ")

    for p in pecas_aprovadas:
        if p["id"] == id_remover:
            pecas_aprovadas.remove(p)
            print("Peça removida das aprovadas.")
            return

    for p, motivo in pecas_reprovadas:
        if p["id"] == id_remover:
            pecas_reprovadas.remove((p, motivo))
            print("Peça removida das reprovadas.")
            return

    print("Peça não encontrada.")


def listar_caixas():
    print("\nCaixas fechadas:")
    for i, caixa in enumerate(caixas):
        print(f"Caixa {i+1} com {len(caixa)} peças")


def relatorio():
    print("\nRELATÓRIO FINAL")

    print("Total aprovadas:", len(pecas_aprovadas))
    print("Total reprovadas:", len(pecas_reprovadas))

    print("\nMotivos de reprovação:")
    for p, motivo in pecas_reprovadas:
        print(f"Peça {p['id']} -> {motivo}")

    print("\nCaixas utilizadas:", len(caixas))


# MENU
while True:

    print("\n===== SISTEMA DE CONTROLE =====")
    print("1 - Cadastrar nova peça")
    print("2 - Listar peças aprovadas/reprovadas")
    print("3 - Remover peça cadastrada")
    print("4 - Listar caixas fechadas")
    print("5 - Gerar relatório final")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_peca()

    elif opcao == "2":
        listar_pecas()

    elif opcao == "3":
        remover_peca()

    elif opcao == "4":
        listar_caixas()

    elif opcao == "5":
        relatorio()

    elif opcao == "0":
        print("Encerrando sistema.")
        break

    else:
        print("Opção inválida")