import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt

num_clicks = np.array([[4, 5, 4, 4, 10, 4],
                       [5, 5, 4, 4, 13, 8],
                       [4, 6, 5, 7, 14, 7],
                       [5, 6, 4, 4, 18, 6],
                       [6, 5, 6, 7, 12, 7],
                       [4, 5, 4, 5, 13, 8]])

time_completed = np.array([[6.65, 9.78, 7.13,   8.05,   13.44, 6.89],
                           [7.02, 9.85, 8.01,   8.20,   16.45, 8.79],
                           [6.55, 10.11,10.11,  11.20,  17.57, 7.77],
                           [7.80, 9.95, 7.88,   7.99,   20.08, 6.56],
                           [8.12, 9.70, 10.93,  10.98,  15.13, 7.46],
                           [6.92, 10.20, 7.81,  9.08,   16.31, 9.46]])

num_errors = np.array([[0, 0, 0, 0, 0, 1],
                       [0, 1, 0, 2, 0, 2],
                       [0, 0, 0, 0, 1, 0],
                       [1, 0, 0, 2, 2, 2],
                       [0, 1, 0, 1, 0, 1]])

def std(values, skip_first):
    if skip_first:
        t_values = np.transpose(values[1:])
    else:
        t_values = np.transpose(values)
    stds = []
    for task in range(6):
        stds.append(np.std(t_values[task]))
    return stds

def mean(values, skip_first):
    if skip_first:
        t_values = np.transpose(values[1:])
    else:
        t_values = np.transpose(values)
    stds = []
    for task in range(6):
        stds.append(np.mean(t_values[task]))
    return stds

print("Standard deviation table")
std_clicks = std(num_clicks, True)
std_time = std(time_completed, True)
std_error = std(num_errors, False)
std_table = PrettyTable(["Task", "Numer of Clicks", "Time Completed", "Number of Errors"])
for i in range(6): 
    std_table.add_row([f"Task {i+1}", f"{std_clicks[i]}", f"{std_time[i]}", f"{std_error[i]}"])
print(std_table)

print("\nMean table")
mean_clicks = mean(num_clicks, True)
mean_time = mean(time_completed, True)
mean_error = mean(num_errors, False)
mean_table = PrettyTable(["Task", "Numer of Clicks", "Time Completed", "Number of Errors"])
for i in range(6): 
    mean_table.add_row([f"Task {i+1}", f"{mean_clicks[i]}", f"{mean_time[i]}", f"{mean_error[i]}"])
print(mean_table)

 
x = np.arange(6) 
width = 0.2
  
plt.bar(x-0.1, num_clicks[0], width, color='cyan') 
plt.bar(x+0.1, mean_clicks, width, color='green') 
plt.xticks(x, ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6']) 
plt.xlabel("Tasks") 
plt.ylabel("Num of clicks") 
plt.legend(["Control", "Subjects"]) 
plt.show()

plt.bar(x-0.1, time_completed[0], width, color='cyan') 
plt.bar(x+0.1, mean_time, width, color='green') 
plt.xticks(x, ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6']) 
plt.xlabel("Tasks") 
plt.ylabel("Time completed") 
plt.legend(["Control", "Subjects"]) 
plt.show()

plt.bar(x, mean_error, width, color='green') 
plt.xticks(x, ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6']) 
plt.xlabel("Tasks") 
plt.ylabel("Num of errors") 
plt.legend(["Subjects"]) 
plt.show() 
