nome = "Ana"
idade = 27


valor_produto1 = "30"
valor_produto2 = 20

valor_produto1 = 30

soma = valor_produto1 + valor_produto2


def subtrair_valores(valor1, valor2):
    if valor1 < 0 and valor2 < 0:
        return "Esse valor é menor que 0, coloque um valor maior do zero"
    return valor1 - valor2


print(subtrair_valores(100, 40))

minha_lista = [12, 16, 26, 30, 40]

lista_vazia = list()

lista_vazia.append("uva verde - sem semente")
lista_vazia.append("ovo de galinha")
lista_vazia.append(20)

lista_vazia.append(minha_lista)

print("lista selecionando elementos:", minha_lista[2:4])


menu = {"Pizza": 25.00, "Hambúrguer": 18.00, "Refrigerante": 5.00, "Sorvete": 8.00}
lista_vazia.append(menu)

item_menu = menu.items()
print(item_menu)

for fulano, ciclano in menu.items():
    print(fulano, ciclano)
