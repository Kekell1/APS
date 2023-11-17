import math
quantidade_Onibus_Linha = int(input('Qual o tamanho da frota disponivel da linha esolhida: '))
intervalo_Entre_Onibus = float(input('Qual o intervalo de tempo entre a saida de cada onibus em minutos: '))
distacia_Percuso = float(input('Qual a distacia até o destino em Km: '))
tempo_Percuso = float(input('Quanto tempo leva até a chegada do destino em minutos: '))

# funçao para calcular o tempo total de operaçao
def calcular_tempo_operacao():
    c = c2 = 0 # contadores
    tempo_Operacao = horaIni = minutosIni = minutosFim = horaFim = 0

    print('\nDigite a hora e minutos  iniciais e de encerramento da linha ')
    print('digite apenas a hora sem os minutos, eles seram pedidos em seguida.\n')
    while  c != 2:
        c2 += 1
        if c2 == 1:
            horaIni = int(input('digite a hora inicial : '))
            minutosIni = int(input('digite o minuto inicial :'))
        elif c2 == 2:
            horaFim = int(input('\ndigite a hora do encerramento : '))
            minutosFim = int(input('digite o minuto de encerramento : '))
        c += 1

        inicio = (horaIni * 60) + minutosIni
        fim = (horaFim * 60) + minutosFim
        tempo_Operacao =  (fim - inicio)
    return tempo_Operacao

tempo_Operacao = calcular_tempo_operacao()


# Funçao para emissao de carbono
def emissao_Carbono_Onibus_Util(distacia,tempo_De_Percurso,horario_Funcional,onibus_Por_Linha,intervalo):
    carbono_Diesel_Litro = 3.2
    Km_litro = distacia / 6
    total_Viagens = horario_Funcional/(tempo_De_Percurso * 2 + intervalo)
    total_Viagens_Frota = total_Viagens * onibus_Por_Linha
    emissao_Quantidade_Dia = (total_Viagens_Frota * Km_litro) * carbono_Diesel_Litro
    return emissao_Quantidade_Dia


#funçao para o gasto em eletricidade
def gasto_eletrico(distacia,tempo_De_Percurso,horario_Funcional,onibus_Por_Linha,intervalo):
    consumo_total_de_energia = distacia * 1.25
    gasto = consumo_total_de_energia * 0.20 #retorna quanto vai gastar de acordo com os kWh (quilowwats)
    total_Viagens = horario_Funcional/(tempo_De_Percurso * 2 + intervalo)
    total_Viagens_Frota = total_Viagens * onibus_Por_Linha
    gasto_total= total_Viagens_Frota  * gasto
    return gasto_total

#funçao para gasto com combustivel
def gasto_combustivel(distancia, tempo_De_Percurso, horario_Funcional, onibus_Por_Linha, intervalo):
    eficiencia_km_por_litro = 6
    custo_por_litro = 6.154
    litros_consumidos = distancia / eficiencia_km_por_litro
    gasto = litros_consumidos * custo_por_litro
    total_viagens = horario_Funcional / (tempo_De_Percurso * 2 + intervalo)
    total_viagens_frota = total_viagens * onibus_Por_Linha
    gasto_total = total_viagens_frota * gasto
    return gasto_total


#saida de resultados
resultado_Emissao = emissao_Carbono_Onibus_Util(distacia_Percuso,tempo_Percuso,tempo_Operacao,quantidade_Onibus_Linha,intervalo_Entre_Onibus)
gasto_De_eletricidade = gasto_eletrico(distacia_Percuso,tempo_Percuso,tempo_Operacao,quantidade_Onibus_Linha,intervalo_Entre_Onibus)
gasto_De_Combustivbel = gasto_combustivel(distacia_Percuso,tempo_Percuso,tempo_Operacao,quantidade_Onibus_Linha,intervalo_Entre_Onibus)



#funçao credito de carbono
def Valor_Credito_A_Receber(emissao_Total_dia):
    credito = 0
    emissao_Total_dia *= 365
    while True:
        if emissao_Total_dia >= 1000:
            emissao_Total_dia -= 1000
            credito += 1
        elif emissao_Total_dia < 1000:
            credito_Ano = credito * 365 # creditos a receber no período de 1 ano
            break
    return credito_Ano

credito_Valor = Valor_Credito_A_Receber(resultado_Emissao)
valor_Receber = credito_Valor * 305.45

#Visao do Usuario com saida das informaçoes
print('\n','-='*50)
if resultado_Emissao >= 1000:
    print(f'No dia a linha emitiu {resultado_Emissao/1000:.2f}T de carbono')
else:
    print(f'No dia a linha emitiu {resultado_Emissao:.2f}kg de carbono')
print(f'O gasto do dia da linha com combustivel foi R${math.ceil(gasto_De_Combustivbel):.2f}')

print('Por fazer a troca para onibus eletricos e nao emitir carbono nessa linha:')
print(f'No dia a linha gastara R${math.ceil(gasto_De_eletricidade):.2f} com eletricidade e nao emitira carbono.')
print(f'No Periodo de 1 ano a empresa recebera {credito_Valor} creditos de carbono e o valor deses creditos deve ser R${(valor_Receber):.2f}')
print(f'E evitara a emissao de {(math.ceil(resultado_Emissao) * 365)/1000:.2f}T de carbono E economizara R${(gasto_De_Combustivbel * 365) - (gasto_De_eletricidade * 365):.2f} em combustivel.')













