import random
def menu():
    print("\nMENU DE OPÇÕES")
    print("----------------")
    print("[1] Soma            [7] Sair") 
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Bhaskara")
    print("[6] Aleatoriedade")
    print("----------------")
          
print("BEM VINDO À CALCULADORA!!!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
opcao = 0
while opcao != 7:
    menu()
    try:
        opcao = int(input("Insira sua opção: "))  
    except ValueError:
        print("\nPor favor digite um número valido!")
        continue
    if opcao == 1: 
     soma1 = int(input("Digite o primeiro número: "))  
     soma2 = int(input("Digite o segundo número: ")) 
     resultado = soma1 + soma2       
     print(f"\nA soma dos números é {resultado}")
     print("ADICIONAR OUTRO NÚMERO?")
     continuar = str(input("\nDigite S/N:"))
     if continuar == "S":
      NValor = int(input("\nDigite o novo valor:"))
      print(f"\nSeu novo resultado é:{resultado + NValor} ")
     elif continuar == "N":
      print("Muito bem!") 
    elif opcao == 2:            
     subtracao1 = int(input("Digite o primeiro número: "))  
     subtracao2 = int(input("Digite o segundo número: "))
     resultado = subtracao1 - subtracao2       
     print(f"\nA subtração dos números é {resultado}")  
     print("\nSUBTRAIR OUTRO NÚMERO?")
     continuar = str(input("\nDigite S/N:"))
     if continuar == "S":
      NValor = int(input("\nDigite o novo valor:"))  
      print(f"\nSeu resultado novo é {resultado - NValor}")
     elif continuar == "N":
       print("Muito Bem!")            
    elif opcao == 3:         
     multiplicacao1 = int(input("Digite o primeiro número: "))  
     multiplicacao2 = int(input("Digite o segundo número: "))
     resultado = multiplicacao1 * multiplicacao2
     print(f"\nA multiplicação dos números é {resultado}") 
     print("\nMULTIPLICAR POR OUTRO NÚMERO?")
     continuar = str(input("\nDigite S/N:"))
     if continuar == "S":
      NValor = int(input("\nDigite o novo valor:"))  
      print(f"\nSeu resultado novo é {resultado * NValor}")
     elif continuar == "N":
      print("Muito Bem!")          
    elif opcao == 4: 
      divisao1 = int(input("Digite o primeiro número: "))  
      divisao2 = int(input("Digite o segundo número: "))
      if divisao2 != 0:
       resultado = divisao1 / divisao2         
       print(f"\nA divisão dos números é {resultado}")  
       print("\nDIVIDIR POR OUTRO NÚMERO?")
       continuar = str(input("\nDigite S/N:"))
       if continuar == "S":
        NValor = int(input("\nDigite o novo valor:"))  
        print(f"\nSeu resultado novo é {resultado / NValor}")
       elif continuar == "N":
         print("Muito Bem!")
      else:  
        print("\nErro: Divisão por zero!")                   
    elif opcao == 5:        
      A = int(input("Digite o valor de A:"))  
      B = int(input("Digite o valor de B:"))  
      C = int(input("Digite o valor de C:"))  
      Delta = (B**2) - (4*A*C)  
      x1 = ((((-1)*B) + (Delta**0.5))/(2*A))  
      x2 = ((((-1)*B) - (Delta**0.5))/(2*A))  
      if Delta == 0:       
       print(f"\nComo Delta é igual a zero temos apenas um valor de raiz (x1=x2): {x1:.4f} ")  
      elif Delta > 0:               
        print(f"\nComo Delta é maior que zero temos duas raizes: {x1:.2f} e {x2:.2f}.")  
      else:    
        print("\nComo Delta é menor que zero não temos raizes.")             
    elif opcao == 6:
      numero1 = int(input("\nNumero aleatorio entre:"))
      numero2 = int(input("\nSeu segundo numero:"))
      if numero1 > numero2:
       numero1, numero2 = numero2, numero1
      aleatoriedade = random.randint(numero1, numero2) 
      print(f"\nSeu numero aleatorio entre {numero1} e {numero2} é {aleatoriedade}")
    elif opcao == 7:    
        print("\nAté logo!")  
    else:    
      print("\nOpção inválida!")
