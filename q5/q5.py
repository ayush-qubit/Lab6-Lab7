import pandas as pd

def get_data(csv_path):
    data=pd.read_csv(csv_path)
    data_grouped=data.groupby('instance')
    instance_1=data_grouped.get_group('instance-1')
    instance_2=data_grouped.get_group('instance-2')
    instance_3=data_grouped.get_group('instance-3')
    return instance_1,instance_2,instance_3

i1,i2,i3=get_data('/home/ayush/git-workspace/Lab6-Lab7/q5/data.csv')
