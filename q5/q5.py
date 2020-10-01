import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import argparse
import sys

plt.rcParams['figure.figsize'] = (10.0, 5.0)

# Reading Data
parser=argparse.ArgumentParser()
parser.add_argument('--data',required=True,help='Data file')
args=vars(parser.parse_args())
csv_path=args['data']
data = pd.read_csv(csv_path)


#Instance1
x1 = []
y1= []
grouped = data.groupby(['instance','algorithm','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-1','round-robin')]
for i, v in regavgrb.items():
    x1.append(i)
    y1.append(v)
x2 = []
y2= []
regavgrb = regavg[('instance-1','ucb')]
for i, v in regavgrb.items():
    x2.append(i)
    y2.append(v)
x3 = []
y3= []
regavgrb = regavg[('instance-1','kl-ucb')]
for i, v in regavgrb.items():
    x3.append(i)
    y3.append(v)
x4 = []
y4= []
regavgrb = regavg[('instance-1','thompson-sampling')]
for i, v in regavgrb.items():
    x4.append(i)
    y4.append(v)


x5 = []
y5= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-1','epsilon-greedy',0.2)]
for i, v in regavgrb.items():
    x5.append(i)
    y5.append(v)

x6 = []
y6= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-1','epsilon-greedy',0.02)]
for i, v in regavgrb.items():
    x6.append(i)
    y6.append(v)

x7 = []
y7= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-1','epsilon-greedy',0.002)]
for i, v in regavgrb.items():
    x7.append(i)
    y7.append(v)

plt.plot(x1, y1, label = "round-robin")
plt.plot(x2, y2, label = "ucb")
plt.plot(x3, y3, label = "kl-ucb")
plt.plot(x4, y4, label = "thompson-sampling")
plt.plot(x5, y5, label = "epsilon-greedy-0.2")
plt.plot(x6, y6, label = "epsilon-greedy-0.02")
plt.plot(x7, y7, label = "epsilon-greedy-0.002")
plt.xlabel('horizon')
plt.ylabel('regret')
plt.title('instance-1')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()


#Instance2
x1 = []
y1= []
grouped = data.groupby(['instance','algorithm','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-2','round-robin')]
for i, v in regavgrb.items():
    x1.append(i)
    y1.append(v)
x2 = []
y2= []
regavgrb = regavg[('instance-2','ucb')]
for i, v in regavgrb.items():
    x2.append(i)
    y2.append(v)
x3 = []
y3= []
regavgrb = regavg[('instance-2','kl-ucb')]
for i, v in regavgrb.items():
    x3.append(i)
    y3.append(v)
x4 = []
y4= []
regavgrb = regavg[('instance-2','thompson-sampling')]
for i, v in regavgrb.items():
    x4.append(i)
    y4.append(v)


x5 = []
y5= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-2','epsilon-greedy',0.2)]
for i, v in regavgrb.items():
    x5.append(i)
    y5.append(v)

x6 = []
y6= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-2','epsilon-greedy',0.02)]
for i, v in regavgrb.items():
    x6.append(i)
    y6.append(v)

x7 = []
y7= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-2','epsilon-greedy',0.002)]
for i, v in regavgrb.items():
    x7.append(i)
    y7.append(v)

plt.plot(x1, y1, label = "round-robin")
plt.plot(x2, y2, label = "ucb")
plt.plot(x3, y3, label = "kl-ucb")
plt.plot(x4, y4, label = "thompson-sampling")
plt.plot(x5, y5, label = "epsilon-greedy-0.2")
plt.plot(x6, y6, label = "epsilon-greedy-0.02")
plt.plot(x7, y7, label = "epsilon-greedy-0.002")
plt.xlabel('horizon')
plt.ylabel('regret')
plt.title('instance-2')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

#Instance3
x1 = []
y1= []
grouped = data.groupby(['instance','algorithm','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-3','round-robin')]
for i, v in regavgrb.items():
    x1.append(i)
    y1.append(v)
x2 = []
y2= []
regavgrb = regavg[('instance-3','ucb')]
for i, v in regavgrb.items():
    x2.append(i)
    y2.append(v)
x3 = []
y3= []
regavgrb = regavg[('instance-3','kl-ucb')]
for i, v in regavgrb.items():
    x3.append(i)
    y3.append(v)
x4 = []
y4= []
regavgrb = regavg[('instance-3','thompson-sampling')]
for i, v in regavgrb.items():
    x4.append(i)
    y4.append(v)


x5 = []
y5= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-3','epsilon-greedy',0.2)]
for i, v in regavgrb.items():
    x5.append(i)
    y5.append(v)

x6 = []
y6= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-3','epsilon-greedy',0.02)]
for i, v in regavgrb.items():
    x6.append(i)
    y6.append(v)

x7 = []
y7= []
grouped = data.groupby(['instance','algorithm','epsilon','horizon'])
regavg = grouped['regret'].agg(np.mean)
regavgrb = regavg[('instance-3','epsilon-greedy',0.002)]
for i, v in regavgrb.items():
    x7.append(i)
    y7.append(v)

plt.plot(x1, y1, label = "round-robin")
plt.plot(x2, y2, label = "ucb")
plt.plot(x3, y3, label = "kl-ucb")
plt.plot(x4, y4, label = "thompson-sampling")
plt.plot(x5, y5, label = "epsilon-greedy-0.2")
plt.plot(x6, y6, label = "epsilon-greedy-0.02")
plt.plot(x7, y7, label = "epsilon-greedy-0.002")
plt.xlabel('horizon')
plt.ylabel('regret')
plt.title('instance-3')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
