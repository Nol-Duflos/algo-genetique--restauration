from random import random
from string import ascii_letters

#Il manque une grosse partie du code que je ne retrouve pas :((
 
choice = lambda x: x[int(random() * len(x))]

EXPECTED_STR = "hello hey hey hello hello I love you random citizen, Nol talking !"
CHANCE_TO_MUTATE = 0.1
GRADED_RETAIN_PERCENT = 0.2
CHANCE_RETAIN_NONGRATED = 0.05
POPULATION_COUNT = 100
GENERATION_COUNT_MAX = 1000
 
GRADED_INDIVIDUAL_RETAIN_COUNT = int(POPULATION_COUNT * GRADED_RETAIN_PERCENT)
 
LENGTH_OF_EXPECTED_STR = len(EXPECTED_STR)
 
MIDDLE_LENGTH_OF_EXPECTED_STR = LENGTH_OF_EXPECTED_STR // 2
 
ALLOWED_CHARMAP = ascii_letters + ' !\'.'
 
MAXIMUM_FITNESS = LENGTH_OF_EXPECTED_STR



 
# Code de l'algorythme
 
def get_random_char():
    #Retroune un caractère random de la list ASCII
    return choice(ALLOWED_CHARMAP)
     
 
def get_random_individual():
    #Créer un individu random
    return [get_random_char() for _ in range(LENGTH_OF_EXPECTED_STR)]
 
 
def get_random_population():
    # Créer une nouvelle population
    return [get_random_individual() for _ in range(POPULATION_COUNT)]
 
 
def get_individual_fitness(individual):
    fitness = 0
    for c, expected_c in zip(individual, EXPECTED_STR):
        if c == expected_c:
            fitness += 1
    return fitness
 
 
def average_population_grade(population):
    total = 0
    for individual in population:
        total += get_individual_fitness(individual)
    return total / POPULATION_COUNT
 
 
def grade_population(population):
    graded_individual = []
    for individual in population:
        graded_individual.append((individual, get_individual_fitness(individual)))
    return sorted(graded_individual, key=lambda x: x[1], reverse=True)
 
 
def evolve_population(population):
    #fait en sort que la population évolue à la génération suivante.
 
    raw_graded_population = grade_population(population)
    average_grade = 0
    solution = []
    graded_population = []
    for individual, fitness in raw_graded_population:
        average_grade += fitness
        graded_population.append(individual)
        if fitness == MAXIMUM_FITNESS:
            solution.append(individual)
    average_grade /= POPULATION_COUNT
 
    #On arrête le script si on ne trouve pas de solution
    if solution:
        return population, average_grade, solution    
 
    # Filtre les meilleurs
    parents = graded_population[:GRADED_INDIVIDUAL_RETAIN_COUNT]
 
    # Ajoute des nouveaux individus pour le fun
    for individual in graded_population[GRADED_INDIVIDUAL_RETAIN_COUNT:]:
        if random() < CHANCE_RETAIN_NONGRATED:
            parents.append(individual)
 
    # Créer une mutation
    for individual in parents:
        if random() < CHANCE_TO_MUTATE:
            place_to_modify = int(random() * LENGTH_OF_EXPECTED_STR)
            individual[place_to_modify] = get_random_char()
 
    # melange les parents pour créer des bébés mutants
    parents_len = len(parents)
    desired_len = POPULATION_COUNT - parents_len
    children = []
    while len(children) < desired_len:
        father = choice(parents)
        mother = choice(parents)
        if True: #father != mother:
            child = father[:MIDDLE_LENGTH_OF_EXPECTED_STR] + mother[MIDDLE_LENGTH_OF_EXPECTED_STR:]
            children.append(child)
 
    # La génération suivante est prête !
    parents.extend(children)
    return parents, average_grade, solution