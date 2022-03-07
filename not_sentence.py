import random

# inteiros = [1,3,4,5,7,8]
# quadrados = [value**2 for value in inteiros]
# print(quadrados)

# inteiros = [1,3,4,5,7,8,9]
# pares = [numero for numero in inteiros if numero%2 == 0]
# print(pares)

def write_file():
    # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    with open('palavras.txt', 'a') as f:
        f.write('banana\n')
        f.write('melancia\n')
        f.write('morango\n')
        f.write('manga\n')
    f.close()

def read_file():
    with open('palavras.txt') as file:
        frutas = [line.strip() for line in file]
        print(frutas[random.randrange(len(frutas))])
    file.close()

# write_file()
read_file()