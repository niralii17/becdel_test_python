
# Project Title


# Bechdel and Mako Mori Test Analysis

## Project Overview

This project involves analyzing Bollywood movies using the Bechdel Test and the Mako Mori Test to assess the representation of female characters. The analysis is conducted using a dataset that includes movie names, ratings, and test results. The report provides insights into the percentage of movies passing each test, identifies top and bottom-rated movies, and examines trends based on the year of release

## Dataset
- Movie_Name: Name of the movie
- Rating: Rating of the movie
- Bechdel_test: Result of the Bechdel Test
- The_Mako_Mori_Test: Result of the Mako Mori Test
- year: Release year of the movie

## Key Insights

1. **Bechdel Test Analysis:**
   - **Percentage of Movies Passing Bechdel Test:**
     - **Yes:** 70.15%
     - **No:** 29.85%
   - **Top 5 Highest-Rated Movies Passing the Bechdel Test:**
     - Movies are sorted based on ratings, with the highest-rated ones being highlighted.
   - **Bottom 5 Lowest-Rated Movies Failing the Bechdel Test:**
     - Movies are sorted based on ratings, with the lowest-rated ones being highlighted.

2. **Mako Mori Test Analysis:**
   - **Percentage of Movies Passing Mako Mori Test:**
     - **Yes:** 26.87%
     - **No:** 73.13%
   - **Top 5 Highest-Rated Movies Passing the Mako Mori Test:**
     - Movies are sorted based on ratings, with the highest-rated ones being highlighted.
   - **Bottom 5 Lowest-Rated Movies Failing the Mako Mori Test:**
     - Movies are sorted based on ratings, with the lowest-rated ones being highlighted.

3. **Yearly Analysis:**
   - Users can input a specific year to filter the dataset and analyze the percentage of movies passing each test for that year.


### Code Walkthrough

1. **Loading Data:**
   ```python
   df = pd.read_csv("path/to/Movies_project1.csv")
   ```

2. **Data Cleaning:**
   - Remove rows with missing movie names.
   - Reset the DataFrame index.
   - Standardize the `Bechdel_test` and `The_Mako_Mori_Test` columns by stripping and capitalizing the values.

3. **Bechdel Test Statistics:**
   ```python
   yes_count = df[df['Bechdel_test'] == 'Yes'].shape[0]
   no_count = df[df['Bechdel_test'] == 'No'].shape[0]
   yes_percentage = (yes_count / total_responses) * 100
   no_percentage = (no_count / total_responses) * 100
   ```

4. **Mako Mori Test Statistics:**
   ```python
   yes_count = df[df['The_Mako_Mori_Test'] == 'Yes'].shape[0]
   no_count = df[df['The_Mako_Mori_Test'] == 'No'].shape[0]
   yes_percentage = (yes_count / total_responses) * 100
   no_percentage = (no_count / total_responses) * 100
   ```

5. **Top and Bottom Movies:**
   - Sort by rating and identify the top 5 and bottom 5 movies based on test results.

6. **Yearly Filtering:**
   - Filter data based on a user-provided year and calculate percentages for the Bechdel and Mako Mori Tests.

### Instructions for Use

1. **Data Preparation:**
   - Ensure the dataset `Movies_project1.csv` is correctly formatted and located at the specified path.

2. **Execution:**
   - Run the script to perform data cleaning, calculate test statistics, and display results for both Bechdel and Mako Mori Tests.
   - Input a specific year when prompted to analyze data for that year.

### Dependencies

- Python 3.x
- Pandas library (`pip install pandas`)

### Future Enhancements

- Integration of additional movie metrics such as box office performance and genre.
- Enhanced visualization of results using graphical libraries.
