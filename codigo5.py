# cria a função calcular imc em função do peso e altura
def calcular_imc(peso, altura):

# define a variável imc como o peso dividido pela altura ao quadrado
imc = peso / (altura ** 2)
# retorna o imc
return imc

# cria a função classificar imc em função da variável imc
def classificar_imc(imc):

# se imc for menor que 18.5 retorna "Abaixo do peso"
if imc < 18.5:
return "Abaixo do peso"
# se imc for maior ou igual a 18.5 e menor que 24.9 retorna "Peso normal"
elif 18.5 <= imc < 24.9:
return "Peso normal"
# se imc for maior ou igual a 25 e menor que 29.9 retorna "Sobrepeso"
elif 25 <= imc < 29.9:
return "Sobrepeso"
# se imc for maior ou igual a 30 e menor que 34.9 retorna "Obesidade grau 1"
elif 30 <= imc < 34.9:
return "Obesidade grau 1"
# se imc for maior ou igual a 35 e menor que 39.9 retorna "Obesidade grau 2"
elif 35 <= imc < 39.9:
return "Obesidade grau 2"
# se imc não satisfizer os outros casos retorna "Obesidade grau 3"
else:
return "Obesidade grau 3"

# cria a função sugestao atividade física com base na classificação do imc
def sugestao_atividade_fisica(classificacao_imc):

# se a classificação foi Abaixo do peso retonra atividades de fortalecimento muscular e dieta rica
if classificacao_imc == "Abaixo do peso":
return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em
proteínas e calorias."
# se a classificação for Peso normal retorna atividades aeróbicas e treino de força moderado
elif classificacao_imc == "Peso normal":
return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e
natação, junto a um treino de força moderado."
# se a classificação for Sobrepeso retorna atividades aeróbicas moderadas e exercícios de resistência
elif classificacao_imc == "Sobrepeso":
return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além
de exercícios de resistência."
# se a classificação for Obesidade grau 1 retorna atividades de baixo impacto e reeducação alimentar
elif classificacao_imc == "Obesidade grau 1":
return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um
programa de reeducação alimentar."
# se a classificação for Obesidade grau 2 retorna exercícios de baixo impacto e acompanhamento nutrcional
elif classificacao_imc == "Obesidade grau 2":
return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e
acompanhamento nutricional."
# se a classificação não satisfizer nenhum dos outros casos retorna atividades físicas supervisionadas
# por proffisionais da saúde e consultas regulares com nutrcionista
else:
return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica,
fisioterapia, e consultas regulares com um nutricionista."

# define a variável peso como o número flutuante do que o usuário inserir
peso = float(input("Digite seu peso (em kg): "))
# define a variável altura como o número flutuante do que o usuário inserir
altura = float(input("Digite sua altura (em metros): "))

# define o imc como o retorno da função calcular_imc
imc = calcular_imc(peso, altura)
# define a classificacao_imc como o retorno da função classificar_imc
classificacao_imc = classificar_imc(imc)
# define a sugestao como o retorno da função sugestao_atividade_fisica
sugestao = sugestao_atividade_fisica(classificacao_imc)

# printa o imc arredondado em até dois números depois da vírgula
print(f"Seu IMC é: {imc:.2f}")
# printa a classificação do imc
print(f"Classificação: {classificacao_imc}")
# printa a sugestão de atividade física
print(f"Sugestão de atividade física: {sugestao}")