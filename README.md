# Used Car Data Analysis Dashboard

## Introduction
This project is an interactive web application that performs **Exploratory Data Analysis (EDA)** on a dataset of used car sales. The goal is to provide insights into the used car market by developing and deploying a dashboard that allows users to explore different visualizations of the data.

The dashboard is created using **Streamlit**, **Pandas**, and **Plotly Express**, and is deployed using the **Render** platform. The project aims to provide additional practice with common software engineering tasks and to make the analysis accessible to the public.

## Features
The web application includes the following visualizations:
1. **Distribution of Car Prices**: Histogram of car prices.
2. **Average Age per Brand**: Bar plot showing the average age of cars by brand.
3. **Average Price per Brand**: Bar plot showing the average price of cars by brand.
4. **Car Age vs. Price Scatter Plot**: Scatter plot of car age versus price.
5. **Number of Listings per Brand**: Bar plot showing the number of car listings by brand.
6. **Price Distribution by Brand**: Box plot showing price distributions for each brand.
7. **Dynamic Histogram**: A histogram that allows users to dynamically select both the X and Y-axis, providing interactive exploration of different variables in the used car dataset.

## Technologies Used
- **Streamlit**: For creating the web application.
- **Pandas**: For data manipulation and analysis.
- **Plotly Express**: For interactive visualizations.

## Installation and Setup
To run the project locally, follow the steps below:

1. Clone the repository.
2. Install the required dependencies from `requirements.txt`:
3. Run the Streamlit app:
4. Once the app starts, open a browser and navigate to the local server URL provided.

## Dataset
The dataset contains information about used car listings and includes the following columns:
- **model**: Vehicle model name.
- **price**: Vehicle price in US dollars.
- **condition**: Condition of the vehicle (e.g., new, like new, excellent).
- **cylinders**: Number of engine cylinders.
- **fuel**: Type of fuel used (e.g., gasoline, diesel).
- **odometer**: Mileage of the vehicle in miles.
- **transmission**: Type of transmission (e.g., automatic, manual).
- **paint_color**: Color of the vehicle.
- **is_4wd**: Whether the vehicle is four-wheel drive.
- **date_posted**: Date the advertisement was published.
- **days_listed**: Number of days the advertisement remained active.

## Usage
The dashboard includes a series of visualizations that are designed to provide insights into:
- **Price distributions** of cars based on various attributes.
- The **relationship between car age and price**, showing how vehicles depreciate over time.
- The **number of car listings by brand** and their **average prices**.
- **Price variability** within brands to understand pricing patterns.

Use the checkboxes and dropdowns to interactively explore the data and gain different perspectives on the used car market. These features are intended to make the analysis accessible and adaptable based on your interests.

## Conclusions
- The **car prices** are primarily in the **affordable range**, with the majority under **$50,000**.
- Some brands, like **Mercedes-Benz**, have higher median prices due to the **luxury segment**.
- There are **significant price variations** between brands, which may be attributed to differences in the model features, brand positioning, and market value.
- The **age of cars** affects their **price**, with prices generally decreasing as cars get older, reflecting typical vehicle depreciation patterns.

## Deployment
The web application is deployed using the **Render** platform. To see the live version of the project, visit the link below:
- [Deployed Application](https://car-data-dashboard.onrender.com)
