import pandas as pd

placements = pd.read_csv('College Placement Data.csv')
companies = pd.read_csv('College Placement Companies.csv')

print("Placement Data")
print(placements.head())

print("\nColumns")
print(placements.columns)

print("\nInfo")
print(placements.info())

print("Companies Data")
print(companies.head())