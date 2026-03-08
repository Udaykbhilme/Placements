from flask import Flask, render_template
from flask import request
import matplotlib.pyplot as plt
import analytics

app= Flask(__name__)

@app.route("/")
def home():
    year=request.args.get('year')
    if year:
        df=analytics.data[analytics.data["year"]==int(year)]
    else:
        df=analytics.data

    total=len(df)
    avg_salary=f"₹{round(df["Salary"].mean()/100000,2)} LPA"
    highest=f"₹{round(df['Salary'].max()/100000,2)} LPA"

    best_year=analytics.data.groupby("year").size().idxmax()
    top_company=analytics.data['name of company'].value_counts().idxmax()
    avg_salary_trend=analytics.data.groupby('year')["Salary"].mean().idxmax()

    companies=df["name of company"].value_counts().head(5)
    years=sorted(analytics.data["year"].unique()) 
    analytics.generate_chart(df)   

    return render_template(
        "index.html",
        total=total,
        avg_salary=avg_salary,
        highest=highest,
        companies=companies,
        years=years,
        best_year=best_year,
        top_company=top_company,
        avg_salary_trend=avg_salary_trend
    )


if __name__ =="__main__":
    app.run(debug=True)
