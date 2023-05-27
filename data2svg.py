#!/usr/bin/env python3
"""
pip install matplotlib
"""
import matplotlib.pyplot as plt
import csv

__version__ = "0.1.0" # 2023/02

# Read the CSV file
input_dataset = 'data/dataset.csv'
output_file = 'data/btc_chart.svg'
title = 'Bitcoin Price Chart'

dates = []
prices = []

with open(input_dataset, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        dates.append(row[0])
        prices.append(float(row[1]))

# Create the chart
plt.plot(dates, prices)

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(title)


plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.savefig(output_file, format='svg')  # Save the chart as SVG
plt.show()  # Display the chart
