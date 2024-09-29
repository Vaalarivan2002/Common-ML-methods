import matplotlib.pyplot as plt
import numpy as np

# code to visualize the relationship between a categorical independent variable(X) and a continuous dependent variable(y) by using the mean aggregate of y over a particular a category in X

def visualizeRelationshipBetweenCategoricalAndOutputVariables(df, independent_column_name, dependent_column_name):
	brand_mean_price = df.groupby(independent_column_name)[dependent_column_name].mean().sort_values()

	plt.figure(figsize=(10, 6))
	x = np.arange(len(brand_mean_price))  # Create numeric x-values for categorical 'Brand'
	y = brand_mean_price.values

	# Step 3: Plot the raw points
	plt.scatter(x, y, color='blue', label='Mean Price by Brand', s=100)

visualizeRelationshipBetweenCategoricalAndOutputVariables(df, 'brand', 'price')