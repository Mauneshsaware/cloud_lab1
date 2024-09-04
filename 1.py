﻿import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0],[11.0]]
weight=[ 8, 10 , 12, 14, 16, 18, 20, 22]
plt.scatter(height,weight,color='black')
plt.xlabel("height")
plt.ylabel("weight")
ma=linear_model.LinearRegression()
ma.fit(height,weight)
X_height=[[12.0]]
print(ma.predict(X_height))
