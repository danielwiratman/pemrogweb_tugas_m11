from sklearn.linear_model import LinearRegression 
import numpy as np
import pandas as pd

ml1_x = np.array([[-50,100,20],[-21,20,10],[0,120,10],[-10,50,20],[-50,80,23],[-20,102,60]])
ml1_y = np.array([0.6,0.5,0.6,0.2,0.8,0.3])
model1 = LinearRegression().fit(ml1_x,ml1_y)
ml2_x = np.array([[-50,100,20],[-21,20,10],[0,120,10],[-10,50,20],[-50,80,23],[-20,102,60]])
ml2_y = np.array([0.6,0.5,0.6,0.2,0.8,0.3])
model2 = LinearRegression().fit(ml2_x,ml2_y)
ml3_x = np.array([[-50,100,20],[-21,20,10],[0,120,10],[-10,50,20],[-50,80,23],[-20,102,60]])
ml3_y = np.array([0.6,0.5,0.6,0.2,0.8,0.3])
model3 = LinearRegression().fit(ml3_x,ml3_y)