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
pato['bpm'] = 'não identificado'
pato['superpoder'] = 'não identificado'
def ZerarPato():
    global pato
    pato = {}
    pato['bpm'] = 'não identificado'
    pato['superpoder'] = 'não identificado'
    return pato

patosCatalogados = []

drone = {}
if nomesDrones:
    drone['codigo'] = choice(nomesDrones)
else:
    drone['codigo'] = 'SEM-DRONES'
drone['nacionalidade'] = choice(nomesPaises)
drone['saude'] = 100

divisao = '============================================'
cidade = 'DSIN City'
escolha = 0
exibiu = False
venceu = False

def DetectarPatos():
    global pato
    def CriarPato():
        global drone, pato
        # Aqui tudo que será personalizado desde a criação
        pato['nome'] = choice(nomesPatos)
        pato['status'] = choice(['desperto', 'em transe', 'em hibernação profunda'])
        pato['numeroMutacoes'] = randint(1, 10) # Quantidade de mutações

        # Altura e peso do Pato
        # Se o país do drone for os EUA, converte de pés e libras para cm e g
        if drone['nacionalidade'] == 'Estados Unidos':
            patoAlturaAmericana = round(uniform(3.00, 13.00), 2) # Pés
            pato['altura'] = f'{patoAlturaAmericana * 30.48} cm' # cm

            patoPesoAmericano = randint(4, 14) # Libra
            pato['peso'] = f'{patoPesoAmericano * 453.592} gramas' # gramas
        else:
            pato['altura'] = f'{randint(91, 396)} cm'
            pato['peso'] = f'{randint(1814, 6350)} gramas'
        # Coordenadas GPS.
        # Lugar de referência se tiver
        # Localização do pato = cidade atual - país da cidade + coordenadas GPS
        # Precisão do drone. Se for dos EUA, converte de jardas para cm ou m

    def ProvocarPato():
        # Mensagem e efeitos de fazer isso
        print(choice(frasesProvocar))
        
        def DroneAtacado(dano):
            global drone, nomesDrones

            drone['saude'] -= dano
            if drone['saude'] <= 0: # Drone destruído
                print("O pato destruiu seu drone...")
                # Cria um novo drone
                if isinstance(nomesDrones, list) and len(nomesDrones) > 1:
                    if drone['codigo'] in nomesDrones:
                        nomesDrones.remove(drone['codigo'])
                    if nomesDrones:
                        drone['codigo'] = choice(nomesDrones)
                        drone['saude'] = 100
                    else:
                        Perdeu('Sem drones')
                else:
                    Perdeu('Sem drones')
            else: # Drone continua
                print('Drone atacado pelo pato...')
                print(f'Saúde do seu drone: {drone["saude"]}%')

        DroneAtacado(randint(1, 100))
    
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
