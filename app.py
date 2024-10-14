# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
used_car_data = pd.read_csv('./updated_vehicles_us.csv')


# Introduction
st.title('Used Car Data Visualization: Interactive Graphs')
st.subheader('By Mikhail Karepov')
st.write("""
Welcome to the **Used Car Data Visualization** app!
         
This project is designed to provide additional practice with common software engineering tasks, aimed at enhancing and complementing data skills.
The goal is to develop and deploy a web application that makes the analysis accessible to the public via a cloud service.
The dataset provided includes used car sales advertisements, and the project follows a series of steps for analysis, visualization, and deployment.
         
This application allows you to explore and interact with various graphs based on a dataset of used car sales advertisements. Dive into the data to uncover trends, patterns, and insights about used cars.
Use the controls below to select different variables and customize the graphs to your liking.
""")

# Data Visualization

# Distribution of Car Prices
st.subheader('Distribution of Car Prices')

st.write("""
Use the controls below to explore the price distribution of used cars. You can filter by selecting specific manufacturers, choose to view only cars below $50,000, and normalize the histogram to compare relative frequencies.
""")

## Checkbox to filter cars below $50,000
show_below_50k = st.checkbox('Show only cars below $50,000')

## Get unique brands list
unique_brands = list(used_car_data['brand'].unique())

## Dropdown for manufacturer 1
manufacturer_1 = st.selectbox('Select manufacturer 1', ['None'] + unique_brands, index=0)

## Define available options for manufacturer 2 based on manufacturer 1 selection
if manufacturer_1 == 'None':
    available_brands_2 = unique_brands
else:
    available_brands_2 = [brand for brand in unique_brands if brand != manufacturer_1]

## Get the current value of manufacturer_2 from session state, if it exists
current_manufacturer_2 = st.session_state.get('manufacturer_2', 'None')

## If the current manufacturer_2 is the same as manufacturer_1, reset it to 'None'
if current_manufacturer_2 == manufacturer_1:
    current_manufacturer_2 = 'None'

## Dropdown for manufacturer 2
manufacturer_2 = st.selectbox(
    'Select manufacturer 2',
    ['None'] + available_brands_2,
    index=(['None'] + available_brands_2).index(current_manufacturer_2),
    key='manufacturer_2')

## Filter data based on the price checkbox selection
filtered_data = used_car_data[used_car_data['price'] < 50000] if show_below_50k else used_car_data

## Filter data based on manufacturer selection
selected_brands = [brand for brand in [manufacturer_1, manufacturer_2] if brand != 'None']
if selected_brands:
    filtered_data = filtered_data[filtered_data['brand'].isin(selected_brands)]

## Checkbox for normalization
normalize_hist = st.checkbox('Normalize histogram')

## Plot histogram to compare price distribution
fig_price_hist = px.histogram(
    filtered_data,
    x='price',
    color='brand' if len(selected_brands) > 1 else None,
    barmode='overlay',
    nbins=50,
    title='Price Distribution',
    labels={'price': 'Price (USD)', 'brand': 'Manufacturer'})

## Normalize y-axis if checkbox is selected
if normalize_hist:
    fig_price_hist.update_layout(yaxis_title='Percent')
    fig_price_hist.update_traces(histnorm='percent')
else:
    fig_price_hist.update_layout(yaxis_title='Count')

## Display the plot
st.plotly_chart(fig_price_hist)

# Average Age per Brand
st.subheader('Average Age per Brand')
average_age_per_brand = used_car_data.groupby('brand')['age'].mean().round(0).reset_index()
fig_avg_age = px.bar(average_age_per_brand, x='brand', y='age', title='Average Age of Cars by Brand', text='age')
fig_avg_age.update_layout(xaxis_title='Brand', yaxis_title='Average Age (years)', xaxis_tickangle=-45, yaxis_range=[0, 19], template='ggplot2')
fig_avg_age.update_traces(textposition='outside')
st.plotly_chart(fig_avg_age)

# Average Price per Brand
st.subheader('Average Price per Brand')
average_price_per_brand = used_car_data.groupby('brand')['price'].mean().round(0).reset_index()
fig_avg_price = px.bar(average_price_per_brand, x='brand', y='price', title='Average Price of Cars by Brand', text='price')
fig_avg_price.update_layout(xaxis_title='Brand', yaxis_title='Average Price (USD)', xaxis_tickangle=-45, yaxis_range=[0, 39000], template='ggplot2')
fig_avg_price.update_traces(textposition='outside')
st.plotly_chart(fig_avg_price)

# Car Age vs. Price Scatter Plot
st.subheader('Car Age vs. Price')
st.write("""
Use the controls below to explore the relationship between the age of a car and its price. Each point is color-coded by the car's brand, allowing you to easily see how different brands are distributed in terms of price and age.
""")
fig_age_price_scatter = px.scatter(used_car_data, x='age', y='price', color='brand', title='Car Age vs. Price', opacity=0.6, hover_data=['model', 'brand', 'condition', 'price', 'age'])
fig_age_price_scatter.update_layout(xaxis_title='Car Age (years)', yaxis_title='Price (USD)', template='ggplot2')
st.plotly_chart(fig_age_price_scatter)

# Number of Listings per Brand
st.subheader('Number of Listings per Brand')
brand_counts = used_car_data['brand'].value_counts().reset_index()
brand_counts.columns = ['brand', 'count']
fig_listings = px.bar(brand_counts, x='brand', y='count', title='Number of Listings per Brand', text='count')
fig_listings.update_layout(xaxis_title='Brand', yaxis_title='Number of Listings', xaxis_tickangle=-45, yaxis_range=[0, 14000], template='ggplot2')
fig_listings.update_traces(textposition='outside')
st.plotly_chart(fig_listings)

# Price by Brand
st.subheader('Price by Brand')
fig_price_box = px.box(used_car_data, x='brand', y='price', title='Price Distribution by Brand')
fig_price_box.update_layout(xaxis_title='Brand', yaxis_title='Price (USD)', xaxis_tickangle=-45, template='ggplot2')
st.plotly_chart(fig_price_box)

# Dynamic Histogram
st.markdown("### Dynamic Histogram")
st.write("""
Use the controls below to generate a histogram based on the variables of your choice. Select the X-axis and Y-axis variables to visualize different aspects of the used car data.
""")

## Create mappings from display names to actual column names
x_options = {
    'Model Year': 'model_year',
    'Price': 'price',
    'Odometer': 'odometer',
    'Days Listed': 'days_listed'}

y_options = {
    'Condition': 'condition',
    'Fuel': 'fuel',
    'Brand': 'brand',
    'Transmission': 'transmission',
    'Paint Color': 'paint_color'}

## Dropdowns close to the graph title to create an experience like changing the title itself
x_axis_display = st.selectbox('Select X-axis', list(x_options.keys()), index=0)
y_axis_display = st.selectbox('Select Y-axis', list(y_options.keys()), index=0)

## Map the display names to actual column names
x_axis = x_options[x_axis_display]
y_axis = y_options[y_axis_display]

## Determine number of bins dynamically based on the selected x-axis
if x_axis == 'model_year':
    nbins = 100
elif x_axis in ['days_listed', 'price', 'odometer']:
    nbins = 50
else:
    nbins = len(used_car_data[x_axis].unique())

## Determine the ordered categories for the selected color group
if y_axis == 'condition':
    ordered_categories = ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']
elif y_axis == 'fuel':
    ordered_categories = ['gas', 'diesel', 'hybrid', 'electric', 'other']
elif y_axis == 'transmission':
    ordered_categories = ['automatic', 'manual', 'other']
elif y_axis == 'paint_color':
    ordered_categories = sorted(used_car_data['paint_color'].dropna().unique())
elif y_axis == 'brand':
    ordered_categories = sorted(used_car_data['brand'].dropna().unique())
else:
    ordered_categories = sorted(used_car_data[y_axis].dropna().unique())

## Define the color mapping for paint colors
paint_color_mapping = {
    'white': 'white',
    'red': 'red',
    'black': 'black',
    'blue': 'blue',
    'grey': 'grey',
    'silver': 'silver',
    'custom': 'pink',        
    'orange': 'orange',
    'yellow': 'yellow',
    'brown': 'brown',
    'green': 'green',
    'purple': 'purple',
    'NaN': 'lightgrey'}

## Create the histogram using the selected options
if y_axis == 'paint_color':
    # Apply the color mapping for paint colors
    fig_dynamic_hist = px.histogram(
        used_car_data,
        x=x_axis,
        color=y_axis,
        title=f"Histogram of {y_axis_display} vs {x_axis_display}",
        labels={x_axis: x_axis_display, y_axis: y_axis_display},
        nbins=nbins,
        template='ggplot2',
        barmode='stack',
        category_orders={y_axis: ordered_categories},
        color_discrete_map=paint_color_mapping)
else:
    # Use default colors for other categories
    fig_dynamic_hist = px.histogram(
        used_car_data,
        x=x_axis,
        color=y_axis,
        title=f"Histogram of {y_axis_display} vs {x_axis_display}",
        labels={x_axis: x_axis_display, y_axis: y_axis_display},
        nbins=nbins,
        template='ggplot2',
        barmode='stack',
        category_orders={y_axis: ordered_categories})

## Update chart layout
fig_dynamic_hist.update_layout(
    xaxis_title=x_axis.replace('_', ' ').title(),
    yaxis_title='Count',
    xaxis_tickangle=-45)

## Display the plot
st.plotly_chart(fig_dynamic_hist)