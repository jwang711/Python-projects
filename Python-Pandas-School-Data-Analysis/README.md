## Background
 
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/education.jpg)
 
In your latest role, you've become the Chief Data Scientist for your city's school district. In this capacity, you'll be helping the school board and mayor make strategic decisions regarding future school budgets and priorities.

As a first task, you've been asked to analyze the district-wide standardized test results. You'll be given access to every student's math and reading scores, as well as various information on the schools they attend. Your responsibility is to aggregate the data to and showcase obvious trends in school performance.

## Observable Trends

As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (

As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).

As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school.

## Objectives
[Final Report](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/PyCitySchools_starter_Copy.ipynb) should include each of the following:

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
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/District%20Summary.png)

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
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/Top%20Performing%20Schools%20(By%20Passing%20Rate).png)

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
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/Bottom%20Performing%20Schools%20(By%20Passing%20Rate).png)

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
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/%20Math%20Scores%20by%20Grade.png)



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
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/Reading%20Score%20by%20Grade.png)
 
 
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
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/Scores%20by%20School%20Spending.png)
    
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
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/Scores%20by%20School%20Size.png)
 
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
![](https://github.com/jwang711/python-projects/blob/master/Python-Pandas-School-Data-Analysis/images/Scores%20by%20School%20Type.png)
