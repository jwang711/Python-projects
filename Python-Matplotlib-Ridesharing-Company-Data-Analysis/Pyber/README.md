# The Power of Plots
![Ride](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/ride.png)

## Pyber - Background

The ride sharing bonanza continues! Seeing the success of notable players like Uber and Lyft, you've decided to join a fledgling ride sharing company of your own. In your latest capacity, you'll be acting as Chief Data Strategist for the company. In this role, you'll be expected to offer data-backed guidance on new opportunities for market differentiation.

You've since been given access to the company's complete recordset of rides. This contains information about every active driver and historic ride, including details like city, driver count, individual fares, and city type.

## Objectives

Merge the two datasets [City_data](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/data/city_data.csv)  and [Ride_data](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/data/ride_data.csv) and complete the [Final report](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/pyber_starter-Copy.ipynb) which includes the below requests.

```
# Read the City and Ride Data

city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)

# Combine the data into a single dataset

pyber_data = pd.merge(city_data_df, ride_data_df, on="city")
```
![Ride](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/merged%20dataset.png)

Build a Bubble Plot that showcases the relationship between four key variables:

* Average Fare ($) Per City
* Total Number of Rides Per City
* Total Number of Drivers Per City
* City Type (Urban, Suburban, Rural)

![Ride](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/Pyber%20Ride%20Sharing%20Data.png)

In addition, produce the following three pie charts:

* % of Total Fares by City Type

![Ride](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/%25%20of%20Total%20Fares%20by%20City%20Type.png)

* % of Total Rides by City Type

![Ride](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/%25%20of%20Total%20Rides%20by%20City%20Type.png)

* % of Total Drivers by City Type

![Ride](https://github.com/momoe711/The-Power-of-Plots/blob/master/Pyber/%25%20of%20Total%20Drivers%20by%20City%20Type.png)

Considerations:

* Use the Pandas Library and the Jupyter Notebook.
* Use the Matplotlib library.
* Include a written description of three observable trends based on the data.
* Use proper labeling of your plots, including aspects like: Plot Titles, Axes Labels, Legend Labels, Wedge Percentages, and Wedge Labels.
* Stick to the Pyber color scheme (Gold, SkyBlue, and Coral) in producing your plot and pie charts.
* When making Bubble Plot, experiment with effects like `alpha`, `edgecolor`, and `linewidths`.
* When making Pie Chart, experiment with effects like `shadow`, `startangle`, and `explosion`.


