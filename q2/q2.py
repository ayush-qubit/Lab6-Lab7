import os
from shutil import copyfile

try:
    os.mkdir("./data/save_our_heroes")
except:
    print("save_our_heroes directory is already present, and files are copied there.")

file = open("./data/compromised_agents.txt", 'r')
agents = [line.rstrip() for line in file]
file.close()

all_files = list(os.listdir("./data/top_secret_data"))

for filename in all_files:
    if(filename.startswith("._")):
        continue
    location = os.path.join("./data/top_secret_data", filename)
    file = open(location, 'r')
    lines = [line.rstrip() for line in file]
    file.close()
    check = any(item in agents for item in lines)
    if(check):
        src = location
        dest = os.path.join("./data/save_our_heroes", filename)
        copyfile(src,dest)
