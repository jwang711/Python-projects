# Whats-the-Weather-Like

## Background

![Equator](https://github.com/jwang711/python-projects/blob/master/Python-API-Weather-Analysis/images/equatorsign.png)

## WeatherPy

Create a Python script to visualize the weather of 500+ cities across the world of varying distance from the equator by utilizing a [simple Python library](https://pypi.python.org/pypi/citipy), the [OpenWeatherMap API](https://openweathermap.org/api) to create a representative model of weather across world cities.

## Analysis

* As expected, the weather becomes significantly warmer as one approaches the equator (0 Deg. Latitude). More interestingly, however, is the fact that the southern hemisphere tends to be warmer this time of year than the northern hemisphere. This may be due to the tilt of the earth.
* There is no strong relationship between latitude and cloudiness. However, it is interesting to see that a strong band of cities sits at 0, 80, and 100% cloudiness.
* There is no strong relationship between latitude and wind speed. However, in northern hemispheres there is a flurry of cities with over 20 mph of wind.

## Objectives

Perform API calls
* Perform a weather check on each city using a series of successive API calls.
* Include a print log of each city as it'sbeing processed (with the city number and city name).
```
# Save config information
base_url = "http://api.openweathermap.org/data/2.5/weather?"
query_url = base_url + "APPID=" + api_key + "&q="

# create list for each 
cities_2 =[]
Cloudiness = []
Country = []
Date = []
Humidity = []
Lat = []
Lng = []
Max_Temp = []
Wind_Speed = []

# set initial number for record and set
recordNum = 0
setNum = 1

# Build query URL
# print log of each city as it's being processed
print("Beginning Data Retrieval")
print("------------------------") 

# Loop through the list of cities and perform a request for data on each
for citi in cities:
    weather_response = requests.get(query_url + citi.replace(" ", "%20")).json() 
    print("Processing Record "+str(recordNum)+" for Set " + str(setNum) + " | "+citi)
    print(query_url + citi.replace(" ", "%20"))
    if weather_response['cod'] == 200:
        cities_2.append(citi)
        Cloudiness.append(weather_response['clouds']['all'])
        Country.append(weather_response['sys']['country'])
        Date.append(weather_response['dt'])
        Humidity.append(weather_response['main']['humidity'])
        Lat.append(weather_response['coord']['lat'])
        Lng.append(weather_response['coord']['lon'])
        Max_Temp.append(weather_response['main']['temp_max'])
        Wind_Speed.append(weather_response['wind']['speed'])
    else:
        print("City not found. Skipping...")

# increase record number as we go through the list, if record number hits 50, then record number reset to 0 and set number add 1.
    recordNum +=1
    if recordNum == 50:
        recordNum = 0
        setNum +=1
```
![](https://github.com/momoe711/Whats-the-Weather-Like/blob/master/Images/Retrieve%20APIs.JPG)

Convert Raw Data to DataFrame in [WeatherPy](https://github.com/momoe711/Whats-the-Weather-Like/blob/master/WeatherPy.ipynb) and save the cleaned data to a [CSV.file](https://github.com/momoe711/Whats-the-Weather-Like/blob/master/weather_data.csv)
```
weather_data = pd.DataFrame(weather_dict)
weather_data.head()

# Save data frame to CSV
weather_data.to_csv('weather_data.csv')
```

Build a series of scatter plots to showcase the following relationships:

* Temperature (F) vs. Latitude
```
Latitude = weather_data['Lat']
Temperature = weather_data['Max Temp']

x_axis = Latitude
y_axis = Temperature

# Build the scatter plots for each city types
plt.scatter(x_axis, y_axis, marker="o", facecolors="blue", edgecolors="black",
            s=10, alpha=0.75, linewidth=1)

# Add labels to the x and y axes
plt.title("City Latitude vs. Max Temperature (01/05/17)")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (F)")

# Set a grid on the plot
plt.grid()

# Save the plot and display it
plt.savefig("City Latitude vs. Max Temperature.png")
plt.show()
```

![](https://github.com/momoe711/Whats-the-Weather-Like/blob/master/Images/City%20Latitude%20vs.%20Max%20Temperature.png)

* Humidity (%) vs. Latitude
```
Latitude = weather_data['Lat']
Humidity = weather_data['Humidity']

x_axis = Latitude
y_axis = Humidity

# Build the scatter plots for each city types
plt.scatter(x_axis, y_axis, marker="o", facecolors="blue", edgecolors="black",
            s=10, alpha=0.75, linewidth=1)

# Add labels to the x and y axes
plt.title("City Latitude vs. Humidity (01/05/17)")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")

# Set a grid on the plot
plt.grid()

# Save the plot and display it
plt.savefig("City Latitude vs. Humidity.png")
plt.show()
```
![](https://github.com/momoe711/Whats-the-Weather-Like/blob/master/Images/City%20Latitude%20vs.%20Humidity.png)

* Cloudiness (%) vs. Latitude
```
Latitude = weather_data['Lat']
Cloudiness  = weather_data['Cloudiness']

x_axis = Latitude
y_axis = Cloudiness 

# Build the scatter plots for each city types
plt.scatter(x_axis, y_axis, marker="o", facecolors="blue", edgecolors="black",
            s=10, alpha=0.75, linewidth=1)

# Add labels to the x and y axes
plt.title("City Latitude vs. Cloudiness  (01/05/17)")
plt.xlabel("Latitude")
plt.ylabel("Cloudiness(%)")

# Set a grid on the plot
plt.grid()

# Save the plot and display it
plt.savefig("City Latitude vs. Cloudiness.png")
plt.show()
```
![](https://github.com/momoe711/Whats-the-Weather-Like/blob/master/Images/City%20Latitude%20vs.%20Cloudiness.png)

* Wind Speed (mph) vs. Latitude
```
Latitude = weather_data['Lat']
Wind_Speed  = weather_data['Wind Speed']

x_axis = Latitude
y_axis = Wind_Speed

# Build the scatter plots for each city types
plt.scatter(x_axis, y_axis, marker="o", facecolors="blue", edgecolors="black",
            s=10, alpha=0.75, linewidth=1)

# Add labels to the x and y axes
plt.title("City Latitude vs. Wind Speed (01/05/17)")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (%)")

# Set a grid on the plot
plt.grid()

# Save the plot and display it
plt.savefig("City Latitude vs. Wind Speed.png")
plt.show()

```
![](https://github.com/momoe711/Whats-the-Weather-Like/blob/master/Images/City%20Latitude%20vs.%20Wind%20Speed.png)

Your final notebook must:

* Randomly select **at least** 500 unique (non-repeat) cities based on latitude and longitude.
* Perform a weather check on each of the cities using a series of successive API calls.
* Include a print log of each city as it's being processed with the city number and city name.
* Save both a CSV of all data retrieved and png images for each scatter plot.

## Considerations

* The city data is generated based on random coordinates; as such, the outputs will not be an exact match each time the code is run.

* You may want to start this assignment by refreshing yourself on the [geographic coordinate system](http://desktop.arcgis.com/en/arcmap/10.3/guide-books/map-projections/about-geographic-coordinate-systems.htm).

* Next, spend the requisite time necessary to study the OpenWeatherMap API. Based on your initial study, you should be able to answer  basic questions about the API: Where do you request the API key? Which Weather API in particular will you need? What URL endpoints does it expect? What JSON structure does it respond with? Before you write a line of code, you should be aiming to have a crystal clear understanding of your intended outcome.

* A starter code for Citipy has been provided. However, if you're craving an extra challenge, push yourself to learn how it works: [citipy Python library](https://pypi.python.org/pypi/citipy). Before you try to incorporate the library into your analysis, start by creating simple test cases outside your main script to confirm that you are using it correctly. Too often, when introduced to a new library, students get bogged down by the most minor of errors -- spending hours investigating their entire code -- when, in fact, a simple and focused test would have shown their basic utilization of the library was wrong from the start. Don't let this be you!

* Part of our expectation in this challenge is that you will use critical thinking skills to understand how and why we're recommending the tools we are. What is Citipy for? Why would you use it in conjunction with the OpenWeatherMap API? How would you do so?

* In building your script, pay attention to the cities you are using in your query pool. Are you getting coverage of the full gamut of latitudes and longitudes? Or are you simply choosing 500 cities concentrated in one region of the world? Even if you were a geographic genius, simply rattling 500 cities based on your human selection would create a biased dataset. Be thinking of how you should counter this. (Hint: Consider the full range of latitudes).
