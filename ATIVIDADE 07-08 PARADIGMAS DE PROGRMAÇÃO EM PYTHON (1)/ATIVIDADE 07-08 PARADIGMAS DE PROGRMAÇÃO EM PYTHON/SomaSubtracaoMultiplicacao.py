# DISCIPLINA : PARADIGMAS DE PROGRAMAÇÃO EM PYTHON
# NOME: KAMILLY AMANCIO BATITSA
# MATRICULA: 202202570397

# Melhore o seu código adicionando as opções de soma, subtração e muktiplicação.
#if calculo ==”+”:
#	print (“O resultaod da some é: ‘n1+ n2)

#variaveis
numero1=int(input("Informe a primeiro número:"))
numero2= int(input("Informe o segundo número:"))

#menu
print("-----MENU----")
print("'+' - Soma")
print("'-' - Subtração")
print("'*' - Multiplicação")
opcao=input("Digite a operação desejada: ")


if opcao == '+' :
    soma = int(numero1+numero2)
    print("SOMA DE", numero1, "E", numero2, "É:", soma)

elif opcao == '*':
    somaMultiplicacao = int(numero1*numero2)
    print("A multiplcação dos valores", numero1, "e", numero2, "é:",somaMultiplicacao)

elif opcao=='-':
    somaSubtracao = int(numero1-numero2)
    print("A multiplcação dos valores", numero1, "e", numero2, "é:",somaSubtracao)

else:
    print("!ESTA OPERAÇÃO NÃO ESTÁ HABILITADA!")