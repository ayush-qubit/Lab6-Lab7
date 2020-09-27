import pandas as pd

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

def split_epsilon_greedy(a5):
    a5_grouped=a5.groupby('epsilon')
    return a5_grouped.get_group('0'),a5_grouped.get_group('0.2'),a5_grouped.get_group('0.02')

i1,i2,i3=get_data('/home/ayush/git-workspace/Lab6-Lab7/q5/data.csv')
