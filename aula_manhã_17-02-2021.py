# Ex 1
print("\n--Exercicio 1--\n")
print("Insira o valor de X:")
x = float(input())

print("Insira o valor de z:")
y = float(input())

print("Insira o valor de z:")
z = float(input())

res = (x-5)*y-z

print("Resultado:\n(({}-5)*{})-{} = {}".format(x, y, z, res))

# Ex 2
print("\n--Exercicio 2--\n")
print("Insira o primeiro nome:")
nome1 = input()

print("Insira a idade:")
idade1= int(input())

print("Insira o segundo nome:")
nome2 = input()

print("Insira a idade:")
idade2= int(input())

print("Nome: {}\nIdade: {}\n\nNome: {}\nIdade: {}\n\nSoma das duas idades: {}".format(nome1, idade1, nome2, idade2, (idade1+idade2)))

# Ex 3
print("\n--Exercicio 3--\n")

print("Insira um número:")
temp = float(input())
if (temp>20):
    print("O número é maior que 20!\nMetade do número: {}".format(temp/2))
else:
    print("O número é menor que 20!\nNúmero: {}".format(temp))

#Ex 4
print("\n--Exercicio 4--\n")
print("Insira o valor 1:")
a1 = float(input())

print("Insira o valor 2:")
a2 = float(input())

if (a1 < a2):
    print("{}/{}={}".format(a2, a1, a2/a1))
else:
    print("{}/{}={}".format(a1, a2, a1/a2))

#Ex 5
print("\n--Exercicio 5--\n")
print("Insira o valor:")
temp = float(input())

if (temp < 0):
    print("O valor é negativo.")
else:
    print("O valor é positivo.")

#Ex 6
print("\n--Exercicio 6--\n")
print("Insira o valor:")
temp = float(input())

if (temp < 0):
    print("O valor é negativo.")
elif (temp > 0):
    print("O valor é positivo.")
else:
    print("O valor é neutro.")

#Ex 7
print("\n--Exercicio 7--\n")
print("Insira o valor 1:")
a1 = float(input())

print("Insira o valor 2:")
a2 = float(input())

if (a1 > a2):
    a1 = a2

print("{} é o menor valor.".format(a1))

#Ex 8
print("\n--Exercicio 8--\n")
print("Insira o valor:")
temp = float(input())

if (temp > 0):
    print("Número positivo.\nMetade de {}: {}".format(temp, temp/2))
else:
    print("Número Negativo.\nQuadrado de {}: {}".format(temp, temp**2))

#Ex 9
print("\n--Exercicio 9--\n")
print("Insira o valor:")
temp = float(input())

if (temp > 10):
    print("É MAIOR QUE 10!")
else:
    print("NÃO É MAIOR QUE 10!")

#Ex 10
print("\n--Exercicio 10--\n")
print("Insira a primeira nota:")
a1 = float(input())
print("Insira a segunda nota:")
a2 = float(input())
print("Insira a terceira nota:")
a3 = float(input())
print("Insira a quarta nota:")
a4 = float(input())


if ((a1+a2+a3+a4)/4 >= 8):
    print("aprovado")
else:
    print("reprovado")

#Ex 11
print("\n--Exercicio 11--\n")
print("Insira o primeiro valor:")
a1 = float(input())
print("Insira o segundo valor:")
a2 = float(input())
print("Insira o terceiro valor:")
a3 = float(input())

if (a1 > a2 and a1 > a3):
    print(a1)
elif(a2 > a1 and a2 > a3):
    print(a2)
else:
    print(a3)

#Ex 12
print("\n--Exercicio 12--\n")
print("Insira a quantidade de maçãs:")
temp = float(input())

if (temp < 12):
    temp = temp*1.3

print("Custo total: {}".format(temp))

#Ex 13
print("\n--Exercicio 13--\n")
print("Insira a quantidade de horas:")
a1 = float(input())

print("Insira o valor do salario:")
a2 = float(input())

if (a1 > 40*4):
    salario = ((40*4)*a2)+(((a1-(40*4))*a2)*1.5)
else:
    salario = a1*a2

print("Salario: {}".format(salario))
