# cria a função calcular custo da viagem em função da distancia, custo do combustível,
# consumo do veículo, número de pedágios e custo dos pedágios
def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio):

# define a variável custo do combustível total como a distancia dividida pelo consumo do veículo,
# multiplicado pelo custo do combustivel
custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel

# define a variável custo do pedagio total como o número de pedagios multiplicado pelo custo do pedágio
custo_pedagio_total = numero_pedagios * custo_pedagio

# define a variável custo total como o custo do combustivel total mais o custo do pedagio total
custo_total = custo_combustivel_total + custo_pedagio_total

# retorna o custo total, custo do combustivel total e o custo do pedagio total
return custo_total, custo_combustivel_total, custo_pedagio_total

# define a variável distancia sendo o número flutuante que o usuário inserir
distancia = float(input("Digite a distância da viagem (em km): "))
# define o custo combustivel sendo o número flutuante que o usuário inserir
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
# define o consumo veiculo sendo o número flutuante que o usuário inserir
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
# define o número de pedágios como o número inteiro que o usuário inserir
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
# define o custo pedagio sendo o número flutuante que o usuário inserir
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

# define que custo total, custo combustivel total e custo pedagio total sendo o retorno da funcao calcular custo viagem
custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia,
custo_combustivel,
consumo_veiculo, numero_pedagios,
custo_pedagio)

# printa o custo total da viagem arredondado em até dois números depois da vírgula
print(f"Custo total da viagem: R${custo_total:.2f}")
# printa o custo total com combustível arredondado em até dois números depois da vírgula
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
# printa o custo total com pedágios arredondado em até dois números depois da vírgula
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")