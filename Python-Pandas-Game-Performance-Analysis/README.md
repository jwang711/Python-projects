## Heroes of Pymoli 

### Background

![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-Game-Performance-Analysis/images/Fantasy.jpg)

After landing a job as Lead Analyst for an independent gaming company, you've been assigned the task of analyzing the data for their most recent fantasy game Heroes of Pymoli.

Like many others in its genre, the game is free-to-play, but players are encouraged to purchase optional items that enhance their playing experience. As a first task, the company would like you to generate a report that breaks down the game's purchasing data into meaningful insights.

### Observable Trends 
 * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

 * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).


### Objectives

[Final report](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/HeroesOfPymoli/HeroesOfPymoli_Copy.ipynb) should include each of the following:

### Player Count
* Total Number of Players

```python
# Make a reference to the books.csv file path
file_one = "Resources/purchase_data.csv"
# Import the purchase_data.csv file as a DataFrame
file_one_df = pd.read_csv(file_one)
file_one_df.head()
# Display the total number of players
total_players = file_one_df.SN.nunique()
summary_table = pd.DataFrame({"Total Players": [total_players]})

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Player%20Count.png)

### Purchasing Analysis (Total)
* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue

```python
# Run basic calculations to obtain number of unique items, average price, etc.
Create a summary data frame to hold the results
number_unique_items = file_one_df['Item ID'].nunique()
number_purchase = file_one_df['Purchase ID'].count()
average_price = file_one_df['Price'].mean()
total_revenue = file_one_df['Price'].sum()
summary_table = pd.DataFrame({"Number of Unique Items": [number_unique_items], 
              "Average Price": [average_price], 
              "Number of Purchases": [number_purchase], 
              "Total Revenue": [total_revenue]})

summary_table["Average Price"] = summary_table["Average Price"].map("${:.2f}".format)
summary_table["Total Revenue"] = summary_table["Total Revenue"].map("${:.2f}".format)

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Purchasing%20Anaysis%20(Total).png)

### Gender Demographics
* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed

```python
num_gender = file_one_df.groupby("Gender").nunique()['SN']
percentage_of_players = "{:.2f}%".format(num_gender / total_players * 100)
summary_table = pd.DataFrame({"Percentage of Players": percentage_of_players, "Total Count": num_gender})
summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Gender%20Demographics.png)


### Purchasing Analysis (Gender)
* The below each broken by gender
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Average Purchase Total per Person by Gender
  
```python
counts_gender = file_one_df.groupby('Gender').count()['Price']

average_purchase_price = file_one_df.groupby('Gender').mean()['Price']

total_purchase_price = file_one_df.groupby('Gender').sum()['Price']

avg = total_purchase_price / num_gender

summary_table = pd.DataFrame({"Purchase Count": counts_gender,
             "Average Purchase Price": average_purchase_price,
             "Total Purchase Value": total_purchase_price,
             "Avg Total Purchase per Person": avg})
             
summary_table["Average Purchase Price"] = summary_table["Average Purchase Price"].map("${:.2f}".format)
summary_table["Total Purchase Value"] = summary_table["Total Purchase Value"].map("${:.2f}".format)
summary_table["Avg Total Purchase per Person"] = summary_table["Avg Total Purchase per Person"].map("${:.2f}".format)

summary_table
```
![](https://github.com/bigbluey/Pandas-Pandas-Pandas/blob/master/Images/Purchasing%20Analysis%20(Gender).png)

### Age Demographics
* The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)
  * Total Count
  * Percentage of Players
 
```python
# Establish bins for ages
# Categorize the existing players using the age bins. Hint: use pd.cut()

bins = [4.99, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 44.99]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

file_one_df["AgeRange"] = pd.cut(file_one_df["Age"], bins, labels=group_names)
file_one_df

# Calculate the numbers and percentages by age group

age_group = file_one_df.groupby('AgeRange').nunique()["SN"]
percentage_group = age_group / total_players *100

# Create a summary data frame to hold the results
summary_table = pd.DataFrame({"Total Count": age_group,
             "Percentage of Players": percentage_group,
             })
             
summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Age%20Demographics.png)

### Purchasing Analysis (Age)
* The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Average Purchase Total per Person by Age Group

```python
#purchase count,
agepurchase_count = file_one_df.groupby('AgeRange').count()['Purchase ID']
#avg. purchase price
average_purchase_price = file_one_df.groupby('AgeRange').mean()['Price']
#purchase total per person
total_purchase_price = file_one_df.groupby('AgeRange').sum()['Price']
#avg. purchase total per person
avg = total_purchase_price / age_group
file_one_df["avg_purchase_per_person"] = avg

summary_table = pd.DataFrame({"Purchase Count": agepurchase_count,
             "Average Purchase Price": average_purchase_price,
             "Total Purchase Value": total_purchase_price,
             "Avg Total Purchase per Person": avg})

summary_table["Average Purchase Price"] = summary_table["Average Purchase Price"].map("${:.2f}".format)
summary_table["Total Purchase Value"] = summary_table["Total Purchase Value"].map("${:.2f}".format)
summary_table["Avg Total Purchase per Person"] = summary_table["Avg Total Purchase per Person"].map("${:.2f}".format)

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Purchasing%20Analysis%20(Age).png)

### Top Spenders
* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  * SN
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value

```python
#purchase count,
SNpurchase_count = file_one_df.groupby('SN').nunique()['Purchase ID']
# avg. purchase price
average_purchase_price = file_one_df.groupby('SN').mean()['Price']
# #purchase total per person
total_purchase_price = file_one_df.groupby('SN').sum()['Price']

summary_table = pd.DataFrame({"Purchase Count": SNpurchase_count,
             "Average Purchase Price": average_purchase_price,
             "Total Purchase Value": total_purchase_price,
             })
             
summary_table["Average Purchase Price"] = summary_table["Average Purchase Price"].map("${:.2f}".format)
summary_table["Total Purchase Value"] = summary_table["Total Purchase Value"].map("${:.2f}".format)

summary_table.sort_values(by=['Total Purchase Value'], ascending=False).head()
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Top%20Spenders.png)

### Most Popular Items
* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value

```python
organized_data = file_one_df[["Item ID","Item Name","Price"]]
organized_data.head()

organized1_data = organized_data.groupby(["Item ID", "Item Name"])
organized1_data

purchasecount = organized1_data["Price"].count()
totalprice = organized1_data["Price"].sum()
itemprice = totalprice / purchasecount

summary_table = pd.DataFrame({"Purchase Count": purchasecount,
             "Item Price": totalprice / purchasecount,
             "Total Purchase Value": organized1_data["Price"].sum(),
             })
             
summary_table["Item Price"] = summary_table["Item Price"].map("${:.2f}".format)
summary_table["Total Purchase Value"] = summary_table["Total Purchase Value"].map("${:.2f}".format)
summary_table.sort_values(by=['Purchase Count'], ascending=False).head()
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Most%20Popular%20Items.png)

### Most Profitable Items
* Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value
  
```python
organized_data = file_one_df[["Item ID","Item Name","Price"]]
organized_data.head()

organized1_data = organized_data.groupby(["Item ID", "Item Name"])
organized1_data

purchasecount = organized1_data["Price"].count()
totalprice = organized1_data["Price"].sum()
itemprice = totalprice / purchasecount

summary_table = pd.DataFrame({"Purchase Count": purchasecount,
             "Item Price": totalprice / purchasecount,
             "Total Purchase Value": organized1_data["Price"].sum(),
             })

summary_table["Item Price"] = summary_table["Item Price"].map("${:.2f}".format)
summary_table["Total Purchase Value"] = summary_table["Total Purchase Value"].map("${:.2f}".format)

summary_table.sort_values(by=['Total Purchase Value'], ascending=False).head()
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Most%20Profitable%20Items.png)
