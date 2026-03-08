# College Placement Analytics Dashboard

This project is a small analytics dashboard built to explore trends in college placement data.
It started as a simple exercise in analyzing a CSV file with Python and slowly turned into a deployed web application.


![Resident Evil Leon GIF](https://github.com/user-attachments/assets/8c2b2c06-9b62-44a4-b429-23696f528c3b)

  ( honestly, was just practising)

           
The dashboard allows users to explore placement statistics, view recruitment patterns, and filter results by year.

Live demo:
https://placements-dashboard-qnww.onrender.com ( well, that's not live now... cuz you need to buy stupid $7 subcription from render for this shit. Anyways, it does work offline)

## What the dashboard shows

The application analyzes a dataset containing company placements, salaries, and yearly trends.
It calculates and displays:

<img width="1362" height="999" alt="Screenshot 2026-03-09 at 2 11 55 AM" src="https://github.com/user-attachments/assets/5b8dbcc5-315e-4593-96db-70fa3b434030" />


* Total placements
* Average salary
* Highest salary
* Top recruiting companies
* Placement trends over time
* Automatically generated insights from the data

Users can also filter the dashboard by year to focus on a specific placement cycle.

## Tech stack

Backend

* Python
* Flask

Data processing

* Pandas
* NumPy

Visualization

* Matplotlib

Deployment

* Gunicorn
* Render

## How the project works

The application reads placement data from a CSV file and uses Pandas to perform aggregation and analysis.
Flask serves the results through a simple web interface, while Matplotlib generates charts dynamically.

The filtering feature updates the statistics and charts based on the selected year, allowing the dashboard to behave more like a small analytics tool rather than a static report.

## Running the project locally

Clone the repository:

```bash
git clone <repo-url>
cd placement-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

Then open the browser at:

```
http://127.0.0.1:5000
```

## Notes from development

This project involved the usual cycle of building something small and gradually adding features:

* starting with basic Pandas analysis
* adding a Flask interface
* integrating charts
* adding filtering
* deploying the app online

Along the way there were several debugging sessions involving template issues, plotting backends, and the usual "why does this suddenly not work anymore" moments that come with building any web project.

## Possible future improvements

Some ideas for extending the project:

* storing data in a database instead of a CSV file
* adding more advanced visualizations
* comparing placement trends across multiple colleges
* improving the UI and layout
* adding an admin interface for updating the dataset

## Author
![Resident Evil GIF](https://github.com/user-attachments/assets/34711f83-859b-4987-98d0-5fa48b695e9d)

That's all, see yaa gang soon. 
and yeah, any issues just DM me on X. 
