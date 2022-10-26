import math
import random
import sys

def f(x, y):
    return math.sqrt(x**3 + 2 * y**4)

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

def crossover(parents):
    result = [x[1] for x in parents]

    random.shuffle(parents)

    for i in range(len(parents) // 2):
        parent_1 = parents[i][1]
        parent_2 = parents[i+1][1]

        child_1 = (
            parent_1[0] & parent_2[0],
            parent_1[1] & parent_2[1]
        )

        child_2 = [
            parent_2[1],
            parent_1[0],
        ]

        mutate = random.randint(0,9)
        if (mutate < 1):
            index = random.randint(0, 1)
            child_2[index] = child_2[index] >> 1

        child_2 = (child_2[0], child_2[1])
        
        result.append(child_1)
        result.append(child_2)

    return result

def roulette(population):
    population.reverse()

    # gera as fatias da roleta
    scores = [x[0] for x in population]
    scores_sum = sum(scores)
    slices = [x[0] / scores_sum for x in population]

    results = []

    for i in range(math.ceil(len(population) / 2 - 1)):
        # Pega uma fatia aleatória
        random_slice = random.random()

        for i in range(len(slices)):
            if sum(slices[:i + 1]) > random_slice:
                results.append(population[i - 1])
                break

    return results

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

        # seleção de alguns individuos pelo método da roleta
        parents = roulette(results)

        # garante que o melhor individuo da geração não se perca
        parents.append(most_fit_of_all)

        # cross-over, mutação e concepção da nova geração
        population = crossover(parents)


    print(f'\n==== End of execution ====')
    print('Most fit of all: ', most_fit_of_all)


run(10, 100)