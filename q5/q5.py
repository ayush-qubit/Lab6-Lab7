import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import argparse


def get_data(csv_path):
    data=pd.read_csv(csv_path)
    data_grouped=data.groupby('instance')
    instance_1=data_grouped.get_group('instance-1')
    instance_2=data_grouped.get_group('instance-2')
    instance_3=data_grouped.get_group('instance-3')
    return instance_1,instance_2,instance_3

def graph_instance_1(instance_1):
    instance_1_grouped=instance_1.groupby('algorithm')
    a1=instance_1_grouped.get_group('round-robin')
    a2=instance_1_grouped.get_group('ucb')
    a3=instance_1_grouped.get_group('kl-ucb')
    a4=instance_1_grouped.get_group('thompson-sampling')
    a5,a6,a7=split_epsilon_greedy(instance_1_grouped.get_group('epsilon-greedy'))
    algos=[a1,a2,a3,a4,a5,a6,a7]
    values=[]
    colors=['red','blue','green','pink','gray','violet','yellow']
    i=0
    plt.clf()
    for algo in algos:
        #values.append((algo,get_random_horizon(algo)))
        points=get_random_horizon(algo)
        plt.plot(points[:,0],points[:,1],color=colors[i])
        i=i+1
    plt.xlabel('Horizon')
    plt.ylabel('Regret')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('./instance1.png')

def split_epsilon_greedy(a5):
    a5_grouped=a5.groupby('epsilon')
    return a5_grouped.get_group(float('0.2')),a5_grouped.get_group(float('0.02')),a5_grouped.get_group(float('0.002'))

def get_random_horizon(algo):
    algo_grouped=algo.groupby('horizon')
    horizon=[]
    for name,group in algo_grouped:
        regret=np.array(pd.to_numeric(group['regret']))
        regret=np.random.choice(regret,50)
        average_value=regret.sum()/50.0
        l=[]
        l.append(int(name))
        l.append(average_value)
        horizon.append(l)
    return np.array(horizon)
    pass

def graph_instance_2(instance_2):
    instance_2_grouped=instance_2.groupby('algorithm')
    a1=instance_2_grouped.get_group('round-robin')
    a2=instance_2_grouped.get_group('ucb')
    a3=instance_2_grouped.get_group('kl-ucb')
    a4=instance_2_grouped.get_group('thompson-sampling')
    a5,a6,a7=split_epsilon_greedy(instance_2_grouped.get_group('epsilon-greedy'))
    algos=[a1,a2,a3,a4,a5,a6,a7]
    values=[]
    colors=['red','blue','green','pink','gray','violet','yellow']
    i=0
    plt.clf()
    for algo in algos:
        #values.append((algo,get_random_horizon(algo)))
        points=get_random_horizon(algo)
        plt.plot(points[:,0],points[:,1],color=colors[i])
        i=i+1
    plt.xlabel('Horizon')
    plt.ylabel('Regret')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('./instance2.png')

def graph_instance_3(instance_3):
    instance_3_grouped=instance_3.groupby('algorithm')
    a1=instance_3_grouped.get_group('round-robin')
    a2=instance_3_grouped.get_group('ucb')
    a3=instance_3_grouped.get_group('kl-ucb')
    a4=instance_3_grouped.get_group('thompson-sampling')
    a5,a6,a7=split_epsilon_greedy(instance_3_grouped.get_group('epsilon-greedy'))
    algos=[a1,a2,a3,a4,a5,a6,a7]
    values=[]
    colors=['red','blue','green','pink','gray','violet','yellow']
    i=0
    plt.clf()
    for algo in algos:
        #values.append((algo,get_random_horizon(algo)))
        points=get_random_horizon(algo)
        plt.plot(points[:,0],points[:,1],color=colors[i])
        i=i+1
    plt.xlabel('Horizon')
    plt.ylabel('Regret')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('./instance3.png')


parser=argparse.ArgumentParser()
parser.add_argument('--data',required=True,help='Data file')
args=vars(parser.parse_args())
csv_path=args['data']
i1,i2,i3=get_data(csv_path)
graph_instance_1(i1)
graph_instance_2(i2)
graph_instance_3(i3)