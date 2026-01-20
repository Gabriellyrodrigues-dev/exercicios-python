# Exercício 04 - Funções
# Criando e utilizando funções em Python

def saudacao(nome):
    print(f"Olá, {nome}!")


def soma(a, b):
    return a + b


def verifica_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"


# Chamadas das funções
saudacao("Gabrielly")

resultado = soma(10, 5)
print("Resultado da soma:", resultado)

status = verifica_maioridade(20)
print("Status:", status)
