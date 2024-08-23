 # Exercicios Aula 10

 # Exercicio 1



numero = int(input("Digite um número: "))

if numero % 2 == 0:
      print("O número é par.")
else:
     print("O número é ímpar.")



 # Exercicio 2 

numero1 = 4
numero2 = 76
numero3 = 9   
print('O resultado da soma é', numero1 + numero2 + numero3)



 # Exercicio 3 


def elevado():
      print(n**2)

n = int(input('Digite um numero: '))
elevado()   



 # Exercicio 4 



idade = int(input("Digite a sua idade: "))

if idade >= 18:
     print("Você pode entrar nesta festa.")
else:
     print("Você não pode entrar nesta festa.")


 # Exercicio 5
idade = int(input("Qual e a sua idade: "))
print("Obrigado por nos informar, e tenha um otimo dia")



 # Exercicio 6



def copa():
      ano =  int(input('Ano da copa: '))
      copas  = [1958, 1962, 1970, 1994, 2002] 
      if ano in copas:
         print('Esse ano o Brasil ganhou a copa do mundo deste ano')
      else:
          print('O Brasil não ganhou a copa do mundo deste ano')

copa()


# Exercicio 7


restaurante = []
total_valores = []
op = ["salada" , "macarronada" , "sanduiche" , "sorvete"]
valores = [18.0,26.7,50,11.99]

op1 = int(input("Digite a op 0 "))
op2 = int(input("Digite a op 1 "))
op3 = int(input("Digite a op 2 "))
op4 = int(input("Digite a op 3 "))

if (op1, op2, op3, op4): 
   restaurante += (op[op1], op[op2], op[op3], op[op4]) 
   print(restaurante)
   total_valores+=(valores[op1], valores[op2], valores[op3], valores[op4])
   somar = sum(total_valores)
print("Total do pedido R$", somar)



