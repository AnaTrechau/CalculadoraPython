print('                                             ****** Calculadora mágica da Ana em Python ******')
print(
 '''
***Instruções***
 Para calcular o resultado de uma operação, apenas insira os números e os sinais das operações desejadas e aperte enter.
                    **Sinais matemáticos**
                        Soma -> +
                        Subtração -> -
                        Multiplicação -> x
                        Divisão -> /
 Caso deseje realizar mais uma operação utilizando o resultado obtido, responda sim e siga as intruções na tela.
 '''
)
#Definição das variáveis que vão entrar na função:
#num1 é o primeiro
num1= int(input("Insira um número:"))
op1= input("Escolha uma operação (+,-,*,/):")
num2= int(input("Insira outro número:"))
numMemory=0
print(f"Operação realizada:\n{num1}{op1}{num2}")

def calculadora (numA,op,numB):
    if op == '+':
        resultado = numA + numB
        print(resultado)
    elif op == '-':
        resultado = numA - numB
        print(resultado)
    elif op == '*':
        resultado = num1 * num2
        print(resultado)
    elif op == '/':
        resultado = numA // numB
        print(resultado)
    return (resultado)

numMemory= calculadora(num1,op1,num2)

outraOperacao= input(f"Deseja realizar outra operação com o resultado {numMemory}?")
if outraOperacao == 'sim' or  outraOperacao == 'Sim':
    op2 = input(f"Valor atual = {numMemory}.\nEscolha um sinal (+,-,*,/):")
    num3 = int(input(f"Operação atual= {numMemory}{op2}\nSelecione outro número:"))
    print(f"Operação realizada:\n{numMemory}{op2}{num3}")
    calculadora(numMemory,op2,num3)
else: print("Operação finalizada")
