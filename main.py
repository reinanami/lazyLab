import numpy as np
import math

def main():
    print("Welcome to lazyLab because we hate entering things into L*bflow!")
    n = int(input("Enter number of data points: "))
    data = data_calculator(n)
    mean = mean_calculator(data)
    std_dev = standard_deviation(mean, n, data)
    per_con = percent_confidence(mean, n, std_dev)

    print(f"Mean: {mean}")
    print(f"Standard deviation: {std_dev}")
    print(f"Percent confidence interval (90%): {per_con}")


def data_calculator(n):
    data = []
    
    for i in range(n):
        point = float(input(f"Enter data point {i + 1}: "))
        data.append(point)
    
    return data


def mean_calculator(data):
    total = 0 

    for value in data:
        total += value

    mean = total / len(data)
    return mean

def standard_deviation(mean, n, data):
    
    squared_diffs = [(x - mean) ** 2 for x in data]
    
    variance = sum(squared_diffs) / n

    std_dev = math.sqrt(variance)
    
    return std_dev

def percent_confidence(mean, n, std_dev):

    t_value = 0
    if n == 2:
        t_value = 6.134
    elif n == 3:
        t_value = 2.920   
    elif n == 4:
        t_value = 2.353
    elif n == 5:
        t_value = 2.132
    elif n == 6:
        t_value = 2.015 
    else:
        raise ValueError("WIP for 7 and up")
    
    per_con = t_value * (std_dev / math.sqrt(n))

    return per_con


while(1):
    main()