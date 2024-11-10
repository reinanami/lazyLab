import math
from flask import Flask, request

app = Flask(__name__)

def functions(n, data_points, mean_right_sigfig, std_dev_right_sigfig):
    data = [float(i) for i in data_points.split(',')]  # Convert comma-separated data points to a list of floats
    mean = mean_calculator(data)
    output = f"This is the raw mean: {mean}\n"
    std_dev = standard_deviation(mean_right_sigfig, n, data)
    output += f"This is the raw standard deviation: {std_dev}\n"
    per_con = percent_confidence(mean_right_sigfig, n, std_dev_right_sigfig)
    output += f"Mean: {mean}\n"
    output += f"Standard deviation: {std_dev}\n"
    output += f"Percent confidence interval (90%): {per_con}\n"
    return output


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

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/execute', methods=['GET'])
def execute_command():
    # Retrieve query parameters
    command = request.args.get('command')
    n = int(request.args.get('n', 5))  # Default to 5 data points
    data_points = request.args.get('data_points', '1,2,3,4,5')  # Default data points
    mean_right_sigfig = float(request.args.get('mean_right_sigfig', 3.0))  # Default sigfigs
    std_dev_right_sigfig = float(request.args.get('std_dev_right_sigfig', 2.0))  # Default sigfigs
    
    if command == 'L':  # Proceed if the command is 'L'
        try:
            # Call the functions with the parameters received
            output = functions(n, data_points, mean_right_sigfig, std_dev_right_sigfig)
            return output
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Invalid command"

if __name__ == "__main__":
    app.run(debug=True)