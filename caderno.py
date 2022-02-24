'''

Python documentation:
    https://docs.python.org/3/index.html

Pesquisar sobre
    if(__name__ == "__main__"):

bool
    representa verdadeiro ou falso no Python

built-in
    são funções que não precisa ser importadas,
    pois estão disponíveis para uso automaticamente.

"Truth Value Testing"
    Função relacionada com o tipo bool.
    Decidir quando um valor é considerado True ou False.

    >>> bool(0)
    False
    >>> bool("")
    False
    >>> bool(None)
    False
    >>> bool(1)
    True
    >>> bool(-100)
    True
    >>> bool(13.5)
    True
    >>> bool("teste")
    True
    >>> bool(True)
    True

find()
    A função find encontra a primeira ocorrência
    do texto que estamos procurando e devolve o índice.

Strings
    >>> palavra = "alura"
    >>> palavra.upper()
    >>> print(palavra) #qual é o resultado?

    Strings são imutáveis, são sequências imutáveis!

min()
    Funciona apenas em listas de mesmo tipo.

STRINGS
    Strings, listas e tuplas são tipos de sequências.
    Strings são imutáveis.

LISTA
    listas são mutáveis.

    >>> dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    >>> dias.append("Sábado2")
    >>> dias
    ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Sábado2']

TUPLAS
    É uma lista imutável.

    >>> dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
    >>> type(dias)
    <class 'tuple'>

    tuple() --> recebe por parâmentros a lista a ser convertida.
    >>> linhas_tuple = tuple(linhas)
    >>> type(linhas_tuple)
    <class 'tuple'>
    >>> linhas_tuple
    ('linha 1', 'linha 2', 'linha 3')

    Convertendo uma lista em uma tupla!
    >>> linhas_list = list(linhas_tuple)
    >>> type(linhas_list)
    <class 'list'>
    >>> linhas_list
    ['linha 1', 'linha 2', 'linha 3']

Set
    É importante notar que o set não é uma sequência, pois não tem um índice.
    colecao = {11122233344, 22233344455, 33344455566}
    colecao.add(44455566677) #vai adicionar pois não existe ainda

Dictionary
    instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
    Nesse par, temos no lado esquerdo a chave e no lado direito o valor.
    >>> instrutores['Flavio']
'''