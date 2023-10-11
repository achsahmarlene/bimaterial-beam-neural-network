import random  
import os
import numpy as np
from tqdm import tqdm
import pandas as pd

os.system('ls')
with open('prop.dat') as f:
    data = f.readlines()
X = []
Y = []
for i in tqdm(range(1000)):                                          ###creating dataset by shuffling n times
    data_copy = data[1:101]
    random.shuffle(data_copy)
    data[1:101] = data_copy                           #we should only shuffle the E values 
    data_int = [eval(j) for j in data[1:101]]               #converting the str after reading to int
    X.append(data_int)

    with open('prop.dat', 'w') as f:                        #writing the new shuffled values in prop file
        f.writelines(data)

    os.system('./main.e > shape')                           #running the command which outputs stress and displacement
    with open('stressf') as f:
        stressdata = f.readlines()                          #reading stress file
    with open('displacment') as f:
        dispdata = f.readlines()                            #reading displacement
    stressdata = np.array([[float(j) for j in s.split()] for s in stressdata[1:]]) #for a string in stressdata, 
    #we are taking all j elements ignoring spaces and converting each jth element into float

    dispdata = np.array([[float(j) for j in s.split()] for s in dispdata[1:]])

    output = []
    output.extend(list(np.max(stressdata[:,2:], axis=0)))
    output.extend(list(np.max(dispdata[:,3:], axis=0)))

    Y.append(output)

X = np.array(X)
Y = np.array(Y)

df1 = pd.DataFrame(X)
df2 = pd.DataFrame(Y)
 
df1.to_csv("input.csv")
df2.to_csv("output.csv")