import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data=pd.read_csv("College Placement Data.csv")

def total_placement():
    return len(data)

def top_companies():
    return data['name of company'].value_counts().head(5)

def avg_salary():
    return np.mean(data["Salary"])

def highest_salary():
    return np.max(data["Salary"])

def placements_per_year():
    return data.groupby('year').size()

def generate_chart(df):
    plt.figure(figsize=(6,4))

    if df["year"].nunique()==1:
        #Single year
        company_counts= df["name of company"].value_counts().head(8)

        plt.bar(company_counts.index, company_counts.values)
        plt.title("Top Recruiting Companies")
        plt.xlabel("Company")
        plt.ylabel("Placements")
        plt.xticks(rotation=45)
    else:
        #Multiple years
        yearly=df.groupby("year").size()

        plt.bar(yearly.index, yearly.values)
        plt.title("Placements By Year")
        plt.xlabel("Year")
        plt.ylabel("Placements")

    plt.tight_layout()
    plt.savefig("static/placement_chart.png")    
    plt.close()    

    