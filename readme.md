Esse é o jogo para terminal chamado PokeTerm.
O programa não contém interface gráfica, podendo ser usado apenas pelo terminal do computador.
Este código tem como objetivo trabalhar os conceitos de Orientação a Objetos e exercita-los.
O jogo possui um menu, no qual é possível escolher as opções de gameplay, sendo elas batalhar com um inimigo, explorar o mundo Pokemon, ver quanto de dinheiro possui o player e etc.
Sua estrutura é dividida em 3 arquivos, sendo eles pokemon.py, pessoa.py e main.py
Os arquivos de pokemon e pessoa se relacionam as classes criadas.
Dentro do arquivo main, existe uma função que trabalha na parte de save do jogo. Essa função é capaz de salvar os dados do player num arquivo database.db por meio da função dumb, que salva um código binário.
O player é carregado(dado load) se a pessoa ja tiver entrado no jogo antes e criado seu personagem, tendo seus pokemons e seu dinheiro salvos.