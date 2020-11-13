import random

from pokemon import *

NOMES = ['Ash', 'Misty', 'Brocky']

POKEMONS = [
    PokemonAgua('Squirtle'),
    PokemonAgua('Totodile'),
    PokemonAgua('Seadra'),
    PokemonFogo('Charmander'),
    PokemonFogo('Vulpix'),
    PokemonFogo('Growthe'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Electabuzz'),
    PokemonEletrico('Elekid'),
]


class Pessoa:


    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons
        self.dinheiro = dinheiro


    def mostrar_dinheiro(self):
        print(f'Você possui ${self.dinheiro} na sua conta!')


    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('-------------------------------')
        print(f'Você ganhou ${quantidade}!!')
        self.mostrar_dinheiro()
        print('-------------------------------')


    def mostrar_pokemons(self):
        if self.pokemons == []:
            print(f'{self} não tem pokemons na bag.')
        else:
            print(f'Pokemons de {self.nome}:')
            for index, pokemon in enumerate(self.pokemons):
                print(f"{index} - {pokemon}")


    def batalhar(self, pessoa):
        print(f'=-> {self} iniciou uma batalha com {pessoa}')
        print('************************************************')
        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} ganhou a batalha!')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f'{pessoa} ganhou a batalha!')
                    break
        else:
            print('Essa batalha não pode ocorrer!')
        print('************************************************')


    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'\n{self} escolheu {pokemon_escolhido}!')
            return pokemon_escolhido
        else:
            print(f'\n{self} não tem pokemons disponíveis!')


    def __str__(self):
        return f'{self.nome}'


class Player(Pessoa):
    tipo = 'player'

    def escolha_inicial(player):

        pikachu = PokemonEletrico('Pikachu', level=1)
        squirtle = PokemonAgua('Squirtle', level=1)
        charmander = PokemonFogo('Charmander', level=1)

        print(f'Olá {player}, escolha seu primeiro pokemon!')

        while True:
            print('*****************')
            print('1 -', pikachu)
            print('2 -', squirtle)
            print('3 -', charmander)
            print('*****************')
            resposta = input('°Qual é a sua escolha? ')
            if resposta == '1':
                player.capturar_pokemon(pikachu)
                break
            elif resposta == '2':
                player.capturar_pokemon(squirtle)
                break
            elif resposta == '3':
                player.capturar_pokemon(charmander)
                break
            else:
                print('Opção inválida...')
                continue


    def explorar_mundo(self, player):
        print('Explorando mundo PokeTerm...')
        if random.randint(1, 100) <= 30:
            pokemon = random.choice(POKEMONS)
            print(f'Você encontrou um pokemon: {pokemon}')

            resp = input('Deseja tentar captura-lo? (s/n) ').upper()
            while resp != 'S' and resp != 'N':
                resp = input('Deseja tentar captura-lo? (s/n) ').upper()
            if resp == 'S':
                if pokemon.level >= 1 and pokemon.level < 20:
                    if random.randint(1, 100) <= 90:
                        player.capturar_pokemon(pokemon)
                        player.mostrar_pokemons()
                    else:
                        print(f'{pokemon} fugiu! :(')
                elif pokemon.level >= 20 and pokemon.level < 50:
                    if random.randint(1, 100) <= 60:
                        player.capturar_pokemon(pokemon)
                        player.mostrar_pokemons()
                    else:
                        print(f'{pokemon} fugiu! :(')
                elif pokemon.level >= 50 and pokemon.level < 80:
                    if random.randint(1, 100) <= 40:
                        player.capturar_pokemon(pokemon)
                        player.mostrar_pokemons()
                    else:
                        print(f'{pokemon} fugiu! :(')
                elif pokemon.level >= 80 and pokemon.level <= 100:
                    if random.randint(1, 100) <= 15:
                        player.capturar_pokemon(pokemon)
                        player.mostrar_pokemons()
                    else:
                        print(f'{pokemon} fugiu! :(')
            elif resp == 'N':
                print('Ok, boa viagem!!')
        else:
            print('Você não encontrou nada... Boa sorte na próxima!')


    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}!')


    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input('\nEscolha seu pokemon: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]

                    print(f'{pokemon_escolhido} eu escolho você!!')

                    return pokemon_escolhido
                except:
                    print('Opção inválida...')
        else:
            print(f'\n{self} não tem pokemons disponíveis!')


class Inimigo(Pessoa):
    tipo = 'inimigo'


    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)
