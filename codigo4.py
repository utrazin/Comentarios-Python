# cria a função calcular media e aprovacao com base nas notas e nota minima da aprovacao
def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
# define a variável total_notas como 0
total_notas = 0
# define a variável num_aluno sendo o retorno númerico de notas
num_alunos = len(notas)
# cria um array para aprovados
aprovados = []
# cria um array para reprovados
reprovados = []

# para aluno com nota pertencente a notas.item
for aluno, nota in notas.items():
# adiciona a nota no valor total_notas
total_notas += nota
# se a nota for maior ou igual a nota minima para aprovacao adiciona o aluno ao último lugar da lista dos aprovados
if nota >= nota_minima_aprovacao:
aprovados.append(aluno)
# se não adiciona o aluno ao último lugar da lista dos reprovados
else:
reprovados.append(aluno)

# define a variável media_turma sendo o total de notas / número de alunos
media_turma = total_notas / num_alunos

# retorna a media da turma, a lista dos aprovados e reprovados
return media_turma, aprovados, reprovados

# passa as notas dos alunos pro sistema por meio do objeto chamado notas
notas = {
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

# define a nota mínima para aprovação como 70
nota_minima_aprovacao = 70

# define a media da turma, a lista dos aprovados e reprovados como o retorno da função calcular_media_e_aprovacao
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

# printa a média da turma arredondada em até dois números depois da vírgula
print(f"Média da turma: {media_turma:.2f}")
# printa os alunos aprovados
print(f"Alunos aprovados: {', '.join(aprovados)}")
# printa os alunos reprovados
print(f"Alunos reprovados: {', '.join(reprovados)}")