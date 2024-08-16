# criação de uma função para calcular juros atrasados com base em 3 variáveis
def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
# define a variável taxa de juros diaria sendo a taxa de juros anual dividida por 365 e depois diviida por 100
taxa_juros_diaria = taxa_juros_anual / 365 / 100

# define a variável juros sendo o valor principal vezes a taxa de juros diária vezes os dias de atraso
juros = valor_principal * taxa_juros_diaria * dias_atraso

# define a variável valor total sendo o valor principal mais os juros
valor_total = valor_principal + juros
# retorna o valor total e os juros
return valor_total, juros

# define o valor principal sendo 1000
valor_principal = 1000.00
# define a taxa de juros anual sendo 5
taxa_juros_anual = 5.0
# define os dias de atraso sendo 30
dias_atraso = 30
# define o valor total e juros o que for retornado da função calcular_juros_atraso
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
# printa o valor total a ser pago na tela sendo o número inteiro mais duas casas depois da vírgula, exp: 10.53
print(f"Valor total a ser pago: R${valor_total:.2f}")
# printa o valor dos juros na tela sendo o número inteiro mais duas casas depois da vírgula, exp: 10.53
print(f"Valor dos juros: R${juros:.2f}")