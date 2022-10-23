import math
import random
import sys

def f(x, y):
    return math.sqrt(x**3 + (2 * y)**4)

def fitness(individual):
    z = f(individual[0], individual[1])

    if z == 0:
        return sys.maxsize

    return 1 / z

def generateRandomPopulation(individuals: int):
    population = []
    for _ in range(individuals):
        population.append((random.randint(0,7), random.randint(0,7)))

    return population

def crossover(most_fit):
    result = [x[1] for x in most_fit]

    random.shuffle(most_fit)

    for i in range(len(most_fit) // 2):
        parent_1 = most_fit[i][1]
        parent_2 = most_fit[i+1][1]

        child_1 = (
            parent_1[0] & parent_2[0],
            parent_1[1] & parent_2[1]
        )

        child_2 = (
            parent_1[0] >> 1,
            parent_2[1] >> 1
        )

        result.append(child_1)
        result.append(child_2)

    return result


def run(populationSize, iterations):
    # inicialização da população
    population = generateRandomPopulation(populationSize)
    most_fit_of_all = ()

    # épocas
    for iteration in range(iterations):
        results = []

        # avaliação de cada individuo
        for individual in population:
            results.append((fitness(individual), individual))

        results.sort()
        results.reverse()

        most_fit_of_all = results[0]

        print(f'==== Generation {iteration + 1} ====')
        print('Most fit: ', most_fit_of_all)

        # condição de parada
        if results[0][0] > 1:
            break

        # seleção de alguns individuos
        most_fit = results[:math.ceil(populationSize / 2)]

        # cross-over, mutação e concepção da nova geração
        population = crossover(most_fit)

    print(f'\n==== End of execution ====')
    print('Most fit of all: ', most_fit_of_all)


run(3, 10)