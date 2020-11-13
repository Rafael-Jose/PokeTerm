import random


class Pokemon:


    def __init__(self, especie, nome=None, level=None):
        self.especie = especie

        if nome:
            self.nome = nome
        else:
            self.nome = self.especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        self.vida = self.level * 10
        self.ataque = self.level * 5


    def __str__(self):
        return f'{self.nome}({self.level})'


    def atacar(self, pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo

        if ataque_efetivo >= self.ataque:
            print('CRÍTICO!!!')
        elif ataque_efetivo == 0:
            print('DODGE!!!')
        print(f'{pokemon} perdeu {ataque_efetivo} pontos de vida')

        if pokemon.vida <= 0:
            print(f'{pokemon} foi derrotado')
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = 'elétrico'


    def atacar(self, pokemon):
        print(f'{self.especie}({self.level}) usou choque do trovão em {pokemon.especie}({pokemon.level})!')
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = 'fogo'


    def atacar(self, pokemon):
        print(f'{self.especie}({self.level}) usou lança chamas em {pokemon.especie}({pokemon.level})!')
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = 'água'


    def atacar(self, pokemon):
        print(f"{self.especie}({self.level}) usou jato d'água em {pokemon.especie}({pokemon.level})!")
        return super().atacar(pokemon)
