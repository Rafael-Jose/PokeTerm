from pickle import dump
from pickle import load

from pokemon import *
from pessoa import *


def mostrar_menu():
    print('**********************************')
    print('1 - Explorar mundo PokeTerm')
    print('2 - Lutar com um inimigo aleatório')
    print('3 - Ver seu dinheiro no banco')
    print('4 - Ver sua bag de pokemons')
    print('5 - Sair do jogo')
    print('**********************************')


def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            dump(player, arquivo)
    except Exception as error:
        print(f'Erro ao salvar: {error}')


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = load(arquivo)
            print('>>> Jogo carregado com sucesso!!')
            return player
    except Exception as error:
        print('Nenhum dado salvo!')


if __name__ == '__main__':
    print('>>> Bem-vindo ao PokeTerm!!!')

    player = carregar_jogo()

    if not player:
        nome = input('Qual será o seu Nickname? ')

        player = Player(nome)

        gary = Inimigo('Gary', pokemons=[PokemonFogo('Charmander', level=1)])

        if player.pokemons == []:
            player.escolha_inicial()
            player.mostrar_pokemons()
            print('\n°Agora que já tem um pokemon, que tal sua primeira batalha?')
            print('°Gary é um bom adversário a altura, lute com ele!!!')
            player.batalhar(gary)
        else:
            print('Vejo que você já possui pokemons...')
            player.mostrar_pokemons()
            salvar_jogo(player)

    while True:
        mostrar_menu()
        resp = input('O que deseja fazer? ')

        if resp == '1':
            player.explorar_mundo(player)
            salvar_jogo(player)
        elif resp == '2':
            inimigo = Inimigo()
            inimigo.mostrar_pokemons()
            escolha = input(f'Deseja enfrentar {inimigo}? (s/n) ').upper()

            if escolha == 'S':
                player.batalhar(inimigo)
            elif escolha == 'N':
                print('OK, boa viagem!')
                continue
            salvar_jogo(player)
        elif resp == '3':
            player.mostrar_dinheiro()
        elif resp == '4':
            player.mostrar_pokemons()
        elif resp == '5':
            print('>>> Finalizando PokeTerm...')
            salvar_jogo(player)
            break
