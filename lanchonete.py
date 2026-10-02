def mostrar_cardapio():
    print()
    print("========== CARDÁPIO ==========")
    print("1 - X-Bacon              R$ 23.00")
    print("2 - X-Salada             R$ 18.00")
    print("3 - Batata Frita pequena R$ 6.00")
    print("4 - Batata Frita grande  R$ 12.00")
    print("5 - Coca Cola 300ml      R$ 8.00")
    print("==============================")


def escolher_produto():
    codigo = int(input("Digite o código do produto: "))

    while codigo < 1 or codigo > 5:
        print("Código inválido!")
        codigo = int(input("Digite um código válido (1 a 5): "))

    return codigo


def calcular_preco(codigo):
    if codigo == 1:
        preco = 23.00
    elif codigo == 2:
        preco = 18.00
    elif codigo == 3:
        preco = 6.00
    elif codigo == 4:
        preco = 12.00
    elif codigo == 5:
        preco = 8.00

    return preco


def mostrar_produto(codigo):
    if codigo == 1:
        produto = "X-Bacon"
    elif codigo == 2:
        produto = "X-Salada"
    elif codigo == 3:
        produto = "Batata Frita pequena"
    elif codigo == 4:
        produto = "Batata Frita grande"
    elif codigo == 5:
        produto = "Coca Cola 300ml"

    return produto


def calcular_desconto(total):
    if total < 50:
        desconto = 0
    elif total < 100:
        desconto = 5
    else:
        desconto = 10

    return desconto


def escolher_pagamento():
    print()
    print("Forma de pagamento:")
    print("1 - Dinheiro")
    print("2 - PIX")
    print("3 - Cartão")

    pagamento = int(input("Escolha a forma de pagamento: "))

    while pagamento < 1 or pagamento > 3:
        print("Opção inválida!")
        pagamento = int(input("Escolha uma forma de pagamento válida (1 a 3): "))

    if pagamento == 1:
        forma_pagamento = "Dinheiro"
    elif pagamento == 2:
        forma_pagamento = "PIX"
    elif pagamento == 3:
        forma_pagamento = "Cartão"

    return forma_pagamento


print("====================================")
print("   SISTEMA DA LANCHONETE DO MOREL   ")
print("====================================")

nome = input("Digite o nome do cliente: ")

total = 0

while True:

    mostrar_cardapio()

    codigo = escolher_produto()

    produto = mostrar_produto(codigo)
    preco = calcular_preco(codigo)

    print("Produto escolhido:", produto)
    print("Preço: R$ {:.2f}".format(preco))

    quantidade = int(input("Digite a quantidade: "))

    while quantidade <= 0:
        print("Quantidade inválida!")
        quantidade = int(input("Digite uma quantidade válida: "))

    subtotal = preco * quantidade

    print("Subtotal: R$ {:.2f}".format(subtotal))

    total = total + subtotal

    print("Total até agora: R$ {:.2f}".format(total))

    continuar = input("Deseja escolher outro produto? (s/n): ")

    while continuar.lower() != "s" and continuar.lower() != "n":
        print("Opção inválida!")
        continuar = input("Digite apenas s ou n: ")

    if continuar.lower() == "n":
        break


print()
print("Pedido finalizado!")
print("Total da compra: R$ {:.2f}".format(total))

desconto = calcular_desconto(total)

valor_desconto = total * desconto / 100
valor_final = total - valor_desconto

print("Desconto:", desconto, "%")
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Valor final: R$ {:.2f}".format(valor_final))

forma_pagamento = escolher_pagamento()

print()
print("================================")
print("      RESUMO DA COMPRA")
print("================================")
print("Cliente:", nome)
print("Valor original: R$ {:.2f}".format(total))
print("Desconto aplicado:", desconto, "%")
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Valor final: R$ {:.2f}".format(valor_final))
print("Forma de pagamento:", forma_pagamento)
print("Obrigado pela preferência!")