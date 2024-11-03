import numpy as np
import math

def main():
    print("Welcome to lazyLab because we hate entering things into L*bflow!")
    answer = input("Press L to proceed, press HELP if you don't know sigfigs: ")
    if answer == "L":
        functions()
        print(" ")
        return 0
    elif answer == "HELP":
        sigfiginfodump()
        print(" ")
        return 0
    else:
        print("Type as prompted bruh... try again.")
        print(" ")
        return 0

def functions():
    n = int(input("Enter number of data points: "))
    data = data_calculator(n)
    mean = mean_calculator(data)
    print("This is the raw mean: ", mean)
    mean_right_sigfig = float(input("Please enter mean of right sigfigs: "))
    std_dev = standard_deviation(mean_right_sigfig, n, data)
    print("This is the raw standard deviation: ", std_dev)
    std_dev_right_sigfig = float(input("Please enter the standard deviation of right sigfigs: "))
    per_con = percent_confidence(mean_right_sigfig, n, std_dev_right_sigfig)
    print(" ")
    print("HERE GOES!!!")
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
    
    variance = sum(squared_diffs) / (n - 1)

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

def sigfiginfodump():
    print("You should already know at this point... but sure")
    print("For volumes it's 3 sigfigs and for masses it's also 3.")
    print("For example: 0.131 mL, 13.0 mL, 0.0131 g, 130 g... etc. etc.")
    print("For standard deviation and stuff it just depends on the sigfig of the other values.")
    print("Let's say the average was 0.99939... it should be rounded to 3 sigfigs where it becomes 0.999")
    print("Use that sigfigs to calculate the standard deviation and stuff... but it's ok this is why this program exists.")

while(1):
    main()