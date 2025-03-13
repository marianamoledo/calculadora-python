print("Qual operação deseja realizar?")
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")
print("5 - Exponenciação")

operacao = input()

def soma(numeros_soma):
    n = sum(numeros_soma)
    return print(f"O resultado é {n}")

if operacao == '1':
    print("Operação Soma selecionada.")
    print("Quais números deseja somar?")
    numeros_soma=[]
    soma(numeros_soma)
elif operacao == '2':
    print("Operação Subtração Selecionada.")
elif operacao == '3':
    print("Operação Divisão Selecionada.")
elif operacao == '4':
    print("Operação Multiplicação Selecionada.")
elif operacao == '5':
    print("Operação Exponenciação Selecionada.")
else:
    print("Operação selecionada não está disponível no momento. Selecione uma opção dentro das informadas.")

