import matplotlib.pyplot as plt
import numpy as np

# code to visualize the relationship between a categorical independent variable(X) and a continuous dependent variable(y) by using the mean aggregate of y over a particular a category in X

def visualizeRelationshipBetweenCategoricalAndOutputVariables(df, independent_column_name, dependent_column_name):
	aggregate = df.groupby(independent_column_name)[dependent_column_name].mean().sort_values()

	plt.figure(figsize=(10, 6))
	x = np.arange(len(aggregate))
	y = aggregate.values
	
	plt.scatter(x, y, color='blue', label='Relationship', s=100)

visualizeRelationshipBetweenCategoricalAndOutputVariables(df, 'brand', 'price')
