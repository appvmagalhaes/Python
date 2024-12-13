#Limpa o ecrã
import os
os.system('cls')

salmax=-999
salmin=99999
nomemax=""
nomemin=""

def maximo(salario1, nome1):
    global salmax
    global nomemax

    if salario1>salmax:
        salmax=salario1
        nomemax=nome1

def minimo(salario1, nome1):
    
    global salmin
    global nomemin
    
    if salario1<salmin:
        salmin=salario1
        nomemin=nome1      
 
salario=int(input("Qual o seu salário? "))
while salario !=-1:
    nome=input("Qual o seu nome?")
    maximo(salario,nome)
    minimo(salario, nome)
    salario=int(input("Qual o seu salário? "))
    
print ("O ", nomemax, " é o que possui maior salário que é de: ", salmax)
print ("O ", nomemin, " é o que possui menor salário que é de: ", salmin)