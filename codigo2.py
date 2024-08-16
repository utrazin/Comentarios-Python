# criação da função de calcular área dos comodos
def calcular_area_comodos():
# define a variável total_area como 0
total_area = 0

# enquanto for verdade vai executar um bloco de comando
while True:

# define a variável largura sendo o número flutuante inserido pelo usuário
largura = float(input("Digite a largura do cômodo (em metros): "))
# define a variável comprimento sendo o número flutuante inserido pelo usuário
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# define a variável area_comodo como o resultado da multiplicação da largura e comprimento
area_comodo = largura * comprimento
# printa o resultado da área sendo o número arredondado em até dois números depois da virgula
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

# adiciona a area do comodo a total_area
total_area += area_comodo

# define a variável mais_comodos sendo o retorno do input
mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()
# se a variável mais_comodos for == a 's' vai quebrar a execução e reiniciar
if mais_comodos != 's':
# comando padrão para quebrar o bloco de código que está sendo executado
break

# retorna a total_area
return total_area

# define a area_total sendo o retorno da função calcular_area_comodos
area_total = calcular_area_comodos()
# printa o valor total da área da casa sendo o número arredondado em até dois números depois da vírgula
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")