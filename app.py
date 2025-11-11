import sys
from frases import frasesProvocar
from frases import frasesAproximar
from nomes import nomesCidades
from nomes import nomesPatos
from nomes import nomesPoderes
from nomes import nomesDrones
from nomes import nomesPaises
from random import *
from cores import *
# Variáveis e funções iniciais

pato = {}
pato['droneCodigo'] = choice([
    'abc123', 'def456', 'ghi789', 'jkl123', 'mno456', 'pqr789'
])
# Marca do drone
# Fabricante do drone
# País de origem do drone
divisao = '============================================'
cidade = 'DSIN City'
droneSaude = 100
escolha = 0
def DetectarPatos():
    global pato
    def CriarPato():
        # Aqui tudo que será personalizado de pato para pato e ataque para ataque
        pato['status'] = choice(['desperto', 'em transe', 'em hibernação profunda'])
        # Altura e peso do Pato
        # Quantidade de mutações
        # Se estiver desperto, Habilidade especial do Pato
        # Se o país do drone for os EUA, converte de pés e libras para cm e g
        # Coordenadas GPS.
        # Lugar de referência se tiver
        # Localização do pato = cidade atual - país da cidade + coordenadas GPS
        # Precisão do drone. Se for dos EUA, converte de jardas para cm ou m

    def ProvocarPato():
        # Mensagem e efeitos de fazer isso
        print(choice(frasesProvocar))
        dano = randint(1, 100)
        droneSaude -= dano
        if droneSaude <= 0:
            print("O pato destruiu seu drone...")
            pass # em teoria fecha o programa, na prática...
        print(f'Saúde do seu drone: {droneSaude}%')

    
    def AproximarPato():
        # Coletar as Bmp
        print(choice(frasesAproximar)) # pega uma aleatória
        pato['bpm'] = randint(50, 200) # Número aleatório entre 0 e 100
        print('Bpm coletadas')

    def PatoEncontrado():
        aproximar = ''
        
        while aproximar != 'S' and aproximar != 'N':
            aproximar = str(input('Deseja se aproximar? [S/N]: '))
        
        if aproximar == 'S':
            print(f"Drone se aproxima do pato que está {pato['status']}...")
            if pato['status'] == 'desperto':
                ProvocarPato()
            else:
                AproximarPato()

    # Chance de 50% de ter um pato
    # Se tiver, escolhe um pato aleatório da lista de patos
    # Ativa a função para patos
    temPato = choice([True, False])
    
    if temPato:
        print("Alerta: Pato primordial encontrado!")
        CriarPato()
        print(f"Status: {pato['status']}")
        PatoEncontrado()
    else:
        print('Não há patos aqui.')
        print('Pense na cidade do seu próximo destino.')


def EscolherCidade(listaCidades):
    global cidade, escolha
    escolha = 0

    cidade1 = choice(listaCidades)
    listaCidades.remove(cidade1)

    cidade2 = choice(listaCidades)
    listaCidades.remove(cidade2)
    
    cidade3 = choice(listaCidades)
    listaCidades.remove(cidade3)
    
    cidade4 = choice(listaCidades)
    listaCidades.remove(cidade4)

    print(f'{divisao}\n>> Cidade atual: {cidade}')
    
    if cidade != 'DSIN City':
        DetectarPatos()    
    while escolha < 1 or escolha > 4:
        print(f'[1] {cidade1}\n[2] {cidade2}\n[3] {cidade3}\n[4] {cidade4}')
        
        escolha = int(input('\nDigite seu destino (número inteiro de 1 a 4): '))
        if escolha == -1:
            break
        if escolha < 1 or escolha > 4:
            print('>> Você digitou um valor inválido, tente novamente.\n')

    # Cadastrar a cidade corretamente
    match escolha:
        case 1:
            cidade = cidade1
        case 2:
            cidade = cidade2
        case 3:
            cidade = cidade3
        case 4:
            cidade = cidade4

# Programa rodando

print(listaCidades)
print('\nOlá soldado!')
print(f'Esse é o seu drone: {pato["droneCodigo"]}')
print('Sua missão é catalogar patos primordiais. Esse mundo está cheio deles, mas você tem que encontrá-los.')
print('Escolha a cidade de destino:')

while escolha != -1:
    EscolherCidade(listaCidades)
