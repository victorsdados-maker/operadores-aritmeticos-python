

#**DEFININDO VARIÁVEIS
a = 10
b = 3

                                        # **OPERAÇÕES BÁSICAS**

soma = a + b 						# Resultado: 13
subtracao = a - b 					# Resultado: 7
multiplicacao = a * b 					# Resultado: 30
divisao = a / b 						# Resultado: 3.3333333333333335
divisao_inteira = a // b 				# Resultado: 3
modulo = a % b 					# Resultado: 1
exponenciacao = a ** b 				# Resultado: 1000

                                    # IMPRIMINDO OS RESULTADOS

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")					#Uso de formatação por f-string.
print(f"Divisão Inteira: {divisao_inteira}")
print(f"Módulo: {modulo}")
print(f"Exponenciação: {exponenciacao}")

                        #(Ordem de Precedência

        #"A ordem de execução dos operadores segue as regras matemáticas:"

        #" ** (Exponenciação)
        #"*, /, //, % (Multiplicação, Divisão, Divisão Inteira e Módulo)
        #+, - (Adição e Subtração)
        #Você pode usar parênteses para alterar a ordem de execução. Por exemplo:
        #resultado = (2 + 3) * 4 # Resultado: 20