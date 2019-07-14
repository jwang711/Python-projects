# Pandas-Pandas-Pandas

## Heroes of Pymoli - Background

![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Fantasy.jpg)

After landing a job as Lead Analyst for an independent gaming company, you've been assigned the task of analyzing the data for their most recent fantasy game Heroes of Pymoli.

Like many others in its genre, the game is free-to-play, but players are encouraged to purchase optional items that enhance their playing experience. As a first task, the company would like you to generate a report that breaks down the game's purchasing data into meaningful insights.


## Objectives

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

## Observable Trends 
 * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

 * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).

 
 ## Academy of Py -Background
 
 ![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/education.jpg)
 
 In your latest role, you've become the Chief Data Scientist for your city's school district. In this capacity, you'll be helping the school board and mayor make strategic decisions regarding future school budgets and priorities.

As a first task, you've been asked to analyze the district-wide standardized test results. You'll be given access to every student's math and reading scores, as well as various information on the schools they attend. Your responsibility is to aggregate the data to and showcase obvious trends in school performance.

[Final Report](https://github.com/momoe711/Pandas-Pandas-Pandas/tree/master/PyCitySchools) should include each of the following:

### District Summary
* Create a high leve snapshot (in table form) of the district's key metrics, including :
  * Total Schools
  * Total Students
  * Total Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate ( Average of the above two)

```python
Total_schools = school_data.school_name.nunique()
Total_students = student_data['Student ID'].count()
Total_budget = school_data.budget.sum()
ave_math_score = student_data.math_score.mean()
ave_reading_score = student_data.reading_score.mean()
overall_passing_rate = (ave_math_score + ave_reading_score) / 2
percentage_Passing_Math = student_data[student_data['math_score']>= 70]['math_score'].count() / Total_students *100
percentage_Passing_Reading = student_data[student_data['reading_score']>= 70]['reading_score'].count() / Total_students *100
                                      
summary_table = pd.DataFrame({
    
    "Total Schools": [Total_schools],
    "Total Students": [Total_students],
    "Total Budget": [Total_budget],
    "Average Math Score": [ave_math_score],
    "Average Reading Score": [ave_reading_score],
    "% Passing Math": [percentage_Passing_Math],
    "% Passing Reading":[percentage_Passing_Reading],
    "Overall Passing Rate": [overall_passing_rate]

})

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/District%20Summary.png)

### School Summary
* Create an overview table that summarizes key metrics about each school, including:
  * School Name
  * School Type
  * Total School Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate ( Average of the above two)

### Top Performing Schools (By Passing Rate)
* Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
  * School Name
  * School Type
  * Total Students
  * Total School Budget
  * Per Student Budget
  * Average Math Score
  * Average Reading Score
  * % Passing Math
  * % Passing Reading
  * Overall Passing Rate ( Average of the above two)
  
```python
School_Type = school_data_complete.groupby(['school_name'])['type'].first()
Total_Students = school_data_complete.groupby(['school_name']).size()
Total_School_Budget = school_data_complete.groupby(['school_name'])['budget'].first()
Per_Student_Budget = Total_School_Budget / Total_Students
average_math_score = school_data_complete.groupby(['school_name'])['math_score'].mean()
average_reading_score = school_data_complete.groupby(['school_name'])['reading_score'].mean()

percentage_Passing_Math = (school_data_complete[school_data_complete['math_score']>= 70].groupby(['school_name']).size() / Total_Students) *100
percentage_Passing_Reading = (school_data_complete[school_data_complete['reading_score']>= 70].groupby(['school_name']).size()/ Total_Students) *100


overall_passing_rate = (percentage_Passing_Math + percentage_Passing_Reading) / 2

summary_table = pd.DataFrame({
    
    "School Type": School_Type,
    "Total Students": Total_Students,
    "Total School Budget": Total_School_Budget,
    "Per Student Budget": Per_Student_Budget,
    "Average Math Score": average_math_score,
    "Average Reading Score": average_reading_score,
    "% Passing Math": percentage_Passing_Math,
    "% Passing Reading": percentage_Passing_Reading,
    "Overall Passing Rate": overall_passing_rate
})

summary_table.sort_values(by=['Overall Passing Rate'], ascending=True).head()


overall_passing_rate = (percentage_Passing_Math + percentage_Passing_Reading) / 2

summary_table = pd.DataFrame({
    
    "School Type": School_Type,
    "Total Students": Total_Students,
    "Total School Budget": Total_School_Budget,
    "Per Student Budget": Per_Student_Budget,
    "Average Math Score": average_math_score,
    "Average Reading Score": average_reading_score,
    "% Passing Math": percentage_Passing_Math,
    "% Passing Reading": percentage_Passing_Reading,
    "Overall Passing Rate": overall_passing_rate
})

summary_table.sort_values(by=['Overall Passing Rate'], ascending=False).head()
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Top%20Performing%20Schools%20(By%20Passing%20Rate).png)

### Bottom Performing Schools (By Passing Rate)
 * Create a table that highlights the bottom 5 performing schools based on Overall Pasing Rate. Include all of the same metrics as above.

```python
School_Type = school_data_complete.groupby(['school_name'])['type'].first()
Total_Students = school_data_complete.groupby(['school_name']).size()
Total_School_Budget = school_data_complete.groupby(['school_name'])['budget'].first()
Per_Student_Budget = Total_School_Budget / Total_Students
average_math_score = school_data_complete.groupby(['school_name'])['math_score'].mean()
average_reading_score = school_data_complete.groupby(['school_name'])['reading_score'].mean()

percentage_Passing_Math = (school_data_complete[school_data_complete['math_score']>= 70].groupby(['school_name']).size() / Total_Students) *100
percentage_Passing_Reading = (school_data_complete[school_data_complete['reading_score']>= 70].groupby(['school_name']).size()/ Total_Students) *100


overall_passing_rate = (percentage_Passing_Math + percentage_Passing_Reading) / 2

summary_table = pd.DataFrame({
    
    "School Type": School_Type,
    "Total Students": Total_Students,
    "Total School Budget": Total_School_Budget,
    "Per Student Budget": Per_Student_Budget,
    "Average Math Score": average_math_score,
    "Average Reading Score": average_reading_score,
    "% Passing Math": percentage_Passing_Math,
    "% Passing Reading": percentage_Passing_Reading,
    "Overall Passing Rate": overall_passing_rate
})

summary_table.sort_values(by=['Overall Passing Rate'], ascending=True).head()
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Bottom%20Performing%20Schools%20(By%20Passing%20Rate).png)

### Math Scores by Grade
 * Create a table that lists the average Math Score for students of each grade level(9th, 10th,11th,12th) at each school.
 
```python
ave_m_score_9th = student_data[student_data['grade'] == '9th'].groupby(['school_name'])['math_score'].mean()

ave_m_score_10th = student_data[student_data['grade'] == '10th'].groupby(['school_name'])['math_score'].mean()

ave_m_score_11th = student_data[student_data['grade'] == '11th'].groupby(['school_name'])['math_score'].mean()

ave_m_score_12th = student_data[student_data['grade'] == '12th'].groupby(['school_name'])['math_score'].mean()

summary_table = pd.DataFrame({
    
    "9th": ave_m_score_9th,
    "10th": ave_m_score_10th,
    "11th": ave_m_score_11th,
    "12th": ave_m_score_12th
})

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/%20Math%20Scores%20by%20Grade.png)



### Reading Scores by Grade
 * Create a table that lists the average Reading Score for students of each grade level(9th, 10th,11th,12th) at each school.

```python

ave_r_score_9th = student_data[student_data['grade'] == '9th'].groupby(['school_name'])['reading_score'].mean()

ave_r_score_10th = student_data[student_data['grade'] == '10th'].groupby(['school_name'])['reading_score'].mean()

ave_r_score_11th = student_data[student_data['grade'] == '11th'].groupby(['school_name'])['reading_score'].mean()

ave_r_score_12th = student_data[student_data['grade'] == '12th'].groupby(['school_name'])['reading_score'].mean()

summary_table = pd.DataFrame({
    
    "9th": ave_r_score_9th,
    "10th": ave_r_score_10th,
    "11th": ave_r_score_11th,
    "12th": ave_r_score_12th
})

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Reading%20Score%20by%20Grade.png)
 
 
### Scores by School Spending
 * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
    * Average Math Score
    * Average Reading Score
    * % Passing Math
    * % Passing Reading
    * Overall Passing Rate (Average of the above two)

```python

# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]

school_data_complete["Spending Ranges (Per Student)"] = pd.cut(school_data_complete['budget']/school_data_complete['size'], spending_bins, labels=group_names)

# calculate total students by spending ranges
students_by_budgetrange = school_data_complete.groupby(['Spending Ranges (Per Student)']).size()

# Average Math Score
average_math_score = school_data_complete.groupby(['Spending Ranges (Per Student)']).mean()['math_score']

# Average Reading Score
average_reading_score = school_data_complete.groupby(['Spending Ranges (Per Student)']).mean()['reading_score']

# % Passing Math
number_passing_math = school_data_complete[school_data_complete['math_score'] >= 70].groupby(['Spending Ranges (Per Student)']).size()

percentage_passing_math = (number_passing_math / students_by_budgetrange) * 100

# % Passing Reading
number_passing_reading = school_data_complete[school_data_complete['reading_score'] >= 70].groupby(['Spending Ranges (Per Student)']).size()

percentage_passing_reading = (number_passing_reading / students_by_budgetrange) * 100

# Overall Passing Rate (Average of the above two)
overall_passing_rate = (percentage_passing_math + percentage_passing_reading) /2

summary_table = pd.DataFrame({
    
    "Average Math Score": average_math_score,
    "Average Reading Score": average_reading_score,
    "% Passing Math": percentage_passing_math,
    "% Passing Reading": percentage_passing_reading,
    "% Overall Passing Rate": overall_passing_rate,
})

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Scores%20by%20School%20Spending.png)
    
### Scores by School Size
 * Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium,large).

```python

# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

school_data_complete["School size"] = pd.cut(school_data_complete['size'], size_bins, labels=group_names)

# calculate total students by school size
students_by_size = school_data_complete.groupby(['School size']).size()

# Average Math Score
average_math_score = school_data_complete.groupby(['School size']).mean()['math_score']

# Average Reading Score
average_reading_score = school_data_complete.groupby(['School size']).mean()['reading_score']

# % Passing Math
number_passing_math = school_data_complete[school_data_complete['math_score'] >= 70].groupby(['School size']).size()

percentage_passing_math = (number_passing_math / students_by_size) * 100

# % Passing Reading
number_passing_reading = school_data_complete[school_data_complete['reading_score'] >= 70].groupby(['School size']).size()

percentage_passing_reading = (number_passing_reading / students_by_size) * 100

# Overall Passing Rate (Average of the above two)
overall_passing_rate = (percentage_passing_math + percentage_passing_reading) /2

summary_table = pd.DataFrame({
    
    "Average Math Score": average_math_score,
    "Average Reading Score": average_reading_score,
    "% Passing Math": percentage_passing_math,
    "% Passing Reading": percentage_passing_reading,
    "% Overall Passing Rate": overall_passing_rate,
})

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Scores%20by%20School%20Size.png)
 
### Scores by School Type
 * Repeat the above breakdown, but this time group schools based on school type (Charter vs. DIstrict).

```python

# calculate total students by school type
totalstudents_bytype = school_data_complete.groupby(['type']).size()

# Average Math Score
average_math_score = school_data_complete.groupby(['type']).mean()['math_score']

# Average Reading Score
average_reading_score = school_data_complete.groupby(['type']).mean()['reading_score']

# % Passing Math
number_passing_math = school_data_complete[school_data_complete['math_score'] >= 70].groupby(['type']).size()

percentage_passing_math = (number_passing_math / totalstudents_bytype) * 100

# % Passing Reading
number_passing_reading = school_data_complete[school_data_complete['reading_score'] >= 70].groupby(['type']).size()

percentage_passing_reading = (number_passing_reading / totalstudents_bytype) * 100

# Overall Passing Rate (Average of the above two)
overall_passing_rate = (percentage_passing_math + percentage_passing_reading) /2

summary_table = pd.DataFrame({
    
    "Average Math Score": average_math_score,
    "Average Reading Score": average_reading_score,
    "% Passing Math": percentage_passing_math,
    "% Passing Reading": percentage_passing_reading,
    "% Overall Passing Rate": overall_passing_rate,
})

summary_table
```
![](https://github.com/momoe711/Pandas-Pandas-Pandas/blob/master/Images/Scores%20by%20School%20Type.png)

## Observable Trends

As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (

As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).

As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school.

