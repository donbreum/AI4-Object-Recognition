import numpy as np
import os
#from matplotlib import pyplot as plt

# data = np.genfromtxt('../final_results/times/rockwool-yolov3-tiny352.txt', delimiter=',')

directory = "../final_results/times/"

for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        print(os.path.join(directory, filename))
        full_name = os.path.join(directory, filename)
        data = np.genfromtxt(full_name, delimiter=',')
        mean = np.mean(data)
        


# print(data)



# plt.boxplot(data)
# plt.ylim((0,10))
# plt.grid()
# plt.show()
