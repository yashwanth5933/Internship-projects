import numpy as np
import matplotlib.pyplot as plt
b = 10
m1 = 1000     
m2 = 4       
m3 = 3        
rooms = 3
age = 3
area_values = np.linspace(100, 1000, 100)
price_values = b + m1 * area_values + m2 * rooms + m3 * age
plt.plot(area_values, price_values)
Area = 600
Price = b + m1 * Area + m2 * rooms + m3 * age
plt.scatter(Area, Price)
plt.xlabel("Area")
plt.ylabel("Predicted Price")
plt.title("House Price Prediction using Linear Regression")
plt.show() 
