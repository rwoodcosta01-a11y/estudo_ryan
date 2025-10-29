from datetime import datetime

historico_despesas = []

print("--- Bem-vindo ao seu Diário de Despesas---")

while True:
    print("/n0 que você deseja fazer?")
    print("1: Adicionar novas despesas")
    print("2: Ver todas as despesas")
    print("#: Sair do programa")

    escolha = input("Digite o número da sua opçao: ").strip()

    if escolha == '1':
        print("/n--Adicionando Despesas --")
        descricao = input("Qual a descrição da despesa(ex: Almoço)?")

        try:
            valor_str = input("Qual é o valor(ex:25.50)")
            valor_float = float(valor_str)

        except ValueError:
           print("Erro! Valor inválido. Tente novamente")
        continue

        nova_despesa = {
            "descricao": descricao,
            "valor": valor_float,
            "dat": agora
        }

        historico_despesas.append(nova_despesa)

        print(f"Sucesso! '{descricao} foi adicionada")

    elif escolha == '2':
        print("/n--- Resumo da despesa---")
    
        if not historico_despesas:
            print("Você ainda não resgistrou nenhuma despesa")
        
        else:
            toral_gasto = 0.0

            for despesa in historico_despesas:
            
                data_formatada = despesa["data"].strftime("%d/%m/%Y às  %H:%M")

                print(f"- {despesa['descricao']}: R$ {despesa['valor']:.2f} (em {data_formatada})")

                total_gasto = total_gasto + despesa["valor"]

            print("--------------------------")
            print(f"TOTAL GASTO: R$ {total_gasto:.2f}")
    elif escolha == '3':
        print("/nObrigado por usar o diaário. Até logo")
        break 
        
    else: 
        print("/nOpção inválida, por favor, digite 1, 2, ou 3.")


