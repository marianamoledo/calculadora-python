print("Qual operação deseja realizar?") 
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")
print("5 - Exponenciação")

operacao = input("Digite o número da operação desejada: ")

def soma(numeros):
    resultado = sum(numeros)
    print(f"O resultado é {resultado}")

def subtracao(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    print(f"O resultado é {resultado}")

def divisao(numeros):
    resultado = numeros[0]
    try:
        for num in numeros[1:]:
            resultado /= num
        print(f"O resultado é {resultado}")
    except ZeroDivisionError:
        print("Erro: divisão por zero.")

def multiplicacao(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    print(f"O resultado é {resultado}")

def exponenciacao(base, expoente):
    resultado = base ** expoente
    print(f"O resultado é {resultado}")

if operacao == '1':
    print("Operação Soma selecionada.")
    entrada = input("Digite os números separados por vírgula: ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    soma(numeros)

elif operacao == '2':
    print("Operação Subtração selecionada.")
    entrada = input("Digite os números separados por vírgula (na ordem da operação): ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    subtracao(numeros)

elif operacao == '3':
    print("Operação Divisão selecionada.")
    entrada = input("Digite os números separados por vírgula (na ordem da operação): ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    divisao(numeros)

elif operacao == '4':
    print("Operação Multiplicação selecionada.")
    entrada = input("Digite os números separados por vírgula: ")
    numeros = [float(num.strip()) for num in entrada.split(",")]
    multiplicacao(numeros)

elif operacao == '5':
    print("Operação Exponenciação selecionada.")
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    exponenciacao(base, expoente)

else:
    print("Operação inválida. Selecione uma opção de 1 a 5.")
