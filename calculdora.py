
def calculadora (num1,num2,oper ):
    if (oper == 1): return num1 + num2
    elif (oper ==2): return num1 - num2
    elif (oper ==3): return num1 * num2
    elif (oper ==4): return num1 / num2
    else: return 0


executar =True

while (executar == True):
    print ("Qual a operação você quer realizar?")
    print ("1:Soma, 2:Subtração, 3:Multiplicação, 4:Divisão, 0:Sair")
    oper= int (input())
    if (oper < 0) or (oper > 4):
        print ("Essa opção não existe")
    elif (oper == 0):
        executar= False
    else:
        print ("Insira o primeiro número:")
        num1 = int (input())
        print ("Insira o segundo número:")
        num2 = int (input())
        resultado = calculadora(num1, num2, oper)
        print (resultado)