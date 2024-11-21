#Questao 3:  Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo.
#Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada
#(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto
#(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km);
#Após receber os dados, o programa informa dados típicos de um computador de bordo:
#a) o tempo de viagem (em segundos)
#b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h)
#c) o custo da viagem com combustível (em R$)
#d) o desempenho do carro (em Km/l, l/h e R$/Km)

partida        = int(input('Digite o momento exato de partida (Exemplo: 14.): '))
minuto_partida = int(input('Digite os minutos de partida (Exemplo: 35.): '))
segundos_partida = ((partida * 60) * 60) + (minuto_partida * 60)
chegada        = int(input('Digite a hora de chegada: '))
minuto_chegada = int(input('Digite o minuto de chegada: '))
segundos_chegada = ((chegada * 60) * 60) + (minuto_chegada * 60)
segundos_parados = int(input('Digite o número de segundos parado para descansar: '))
litros_gas       = float(input('Digite a quantidade de litros de combustivel consumido durante a viagem: '))
preco_gas        = float(input('Digite o valor do combustivel em R$: '))
distancia_percorrida = float(input('Digite a distância percorrida em Km: '))

#Calculo Viagem:

tempo_ptd_minutos = partida 
if segundos_chegada >= segundos_partida:
    tempo_viagem = segundos_chegada - segundos_partida
else:
    tempo_viagem = (24 * 60 * 60) - segundos_partida + segundos_chegada
    # 24 * 60 * 60 = calculo para os segundos do dia gasto.

# Calculo VM (Km) e Velocidade Global:
#3600seg = 1hora
#Onde: vm é a velocidade média, ΔS é o deslocamento, Δt é o intervalo de tempo. 
#Para converter a velocidade de km/h para m/s, basta dividir o valor por 3,6. 
#dividir o espaço percorrido pelo tempo para ocorrer a movimentação.
dist_seg = tempo_viagem - segundos_parados
dist_hora = tempo_ptd_minutos / 3600
vm_global = distancia_percorrida / (tempo_viagem / 3600)
vm_em_movimento = distancia_percorrida / dist_hora