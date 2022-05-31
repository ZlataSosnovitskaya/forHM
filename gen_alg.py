import pygad
import numpy
import random
import math


y = 200
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

function_inputs = a  # Функция получает список а
desired_output = y  # По итогу нужно найти x, с которым функция будет выдавать y

num_generations = 100  # Количество поколений
num_parents_mating = 3  # Количество особей для скрещивания
size_population = 30
last_fitness = 0

population = list()
for i in range(size_population):
    population.append(list(numpy.random.normal(size=1)))


def crossover_func(parents, offspring_size, ga_instance):
    offspring = (parents[0][0]+parents[1][0]+parents[2][0])/3
    return offspring


def mutation_func(offspring, ga_instance):
    offspring += random.uniform(-1, 1)
    return offspring


def fitness_func(solution, solution_idx):
    output = 0
    for i in range(len(a)):
        output += (solution[0]**i)*a[i]
    fitness = 1/(numpy.abs(desired_output-output)+0.000001)
    return fitness


ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=3,
    sol_per_pop=size_population,
    initial_population=population,
    fitness_func=fitness_func,
    crossover_type=crossover_func,
    mutation_type=mutation_func
)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution(
    ga_instance.last_generation_fitness)
print('x=', solution[0])
