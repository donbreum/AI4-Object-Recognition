import numpy as np
import os
import matplotlib
from matplotlib import pyplot as plt

# data = np.genfromtxt('../final_results/times/rockwool-yolov3-tiny352.txt', delimiter=',')

THRESHOLD = 0
PRECISION_IDX = 1 
RECALL_IDX = 2

directory = "/home/fnatgaflen/Documents/repositories/AI4-Object-Recognition/darknet/final_results/times/"
# directory = "../final_results/times/"

plot_data = {}

for filename in os.listdir(directory):
    if filename.endswith("recall.txt"): 
        print(os.path.join(directory, filename))
        full_name = os.path.join(directory, filename)
        key = filename.split('_')[0]
        data = np.genfromtxt(full_name, delimiter=',')

        if key in plot_data:
            plot_data[key]["recall"] = data[RECALL_IDX]
            plot_data[key]["precision"] = data[PRECISION_IDX]
        else:
            data_dict = {}
            data_dict["recall"] = data[RECALL_IDX]
            data_dict["precision"] = data[PRECISION_IDX]
            plot_data[key] = data_dict
        

    else:
        print(filename)
        full_name = os.path.join(directory, filename)
        data = np.genfromtxt(full_name, delimiter=',')
        key = filename.split('_')[0]
        mean = np.mean(data)
        if key in plot_data:
            plot_data[key]["time"] = mean
        else:
            data_dict = {}
            data_dict["time"] = mean
            plot_data[key] = data_dict

legend = []
scatter_plots = []
colors = ['r', 'g', 'b', 'orange', 'y', 'purple']
itr = 0

for k, v in sorted(plot_data.items()):
    print(k)
    print("Time: {}, Recall: {}, Precision: {}".format(v["time"], v["recall"], v["precision"]))
    scatter_plots.append(plt.scatter(v["time"], v["recall"], s=50, marker='o', c=colors[itr]))
    legend.append(str(k))
    itr += 1

plt.title("Recall vs Inference Time")
plt.legend(scatter_plots, legend, loc='lower left')
plt.xlabel("Inference Time [s]")
plt.ylabel("Recall")
plt.ylim((0,1))
plt.xlim((0,110))
plt.grid()
plt.show()
        


# print(data)



# plt.boxplot(data)
# plt.ylim((0,10))
# plt.grid()
# plt.show()
