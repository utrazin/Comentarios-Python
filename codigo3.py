# cria uma função para diagnosticar diabetes em função da glicemia em jejum e glicemia pos prandial
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):

# se a glicemia em jejum for maior ou igual a 126 ou a glicemia pos prandial for maior ou igual a 200
# irá retornar "Diabetes"
if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
return "Diabetes"
# se a glicemia em jejum for menor ou igual a 100 ou a glicemia pos prandial for menor que 200
# irá retornar "Pré-diabetes"
elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
return "Pré-diabetes"
# se nenhuma das outras condições forem satisfeitas irá retornar "Normal"
else:
return "Normal"

# define a glicemia em jejum como o número flutuante inserido pelo usuário
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
# define a glicemia pos prandial como o número flutuante inserido pelo usuário
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

# define o resultado como o que retornar da função diagnosticar_diabetes
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
# printa a variável resultado
print(f"O diagnóstico é: {resultado}")