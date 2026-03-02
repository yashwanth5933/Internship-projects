import numpy as np
import matplotlib.pyplot as plt

# Regression coefficients
b = 10        # intercept
m1 = 1000     # area coefficient
m2 = 4        # rooms coefficient
m3 = 3        # age coefficient

# Fixed input values
rooms = 3
age = 3

# Create range of area values
area_values = np.linspace(100, 1000, 100)

# Calculate predicted prices
price_values = b + m1 * area_values + m2 * rooms + m3 * age

# Plot regression line
plt.plot(area_values, price_values)

# Highlight specific house (Area = 600)
Area = 600
Price = b + m1 * Area + m2 * rooms + m3 * age
plt.scatter(Area, Price)

# Labels
plt.xlabel("Area")
plt.ylabel("Predicted Price")
plt.title("House Price Prediction using Linear Regression")

plt.show() 