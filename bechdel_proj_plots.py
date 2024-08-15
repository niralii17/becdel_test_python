# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:07:00 2024

@author: Nirali Parikh
"""
import pandas as pd

df = pd.read_csv("C:\\Users\\Nirali Parikh\\OneDrive\\Pictures\\Documents\\python\\webscraping\\bechdel_test_project\\Movies_project1.csv")

print(df)

df.dropna(subset=['Movie_Name'], inplace=True)
print(df)

df.reset_index(drop=True, inplace=True)
print(df)  

df['Bechdel_test'] = df['Bechdel_test'].str.strip().str.capitalize()


# # Assuming the responses are in a column named 'Response'
# yes_count = df[df['Bechdel_test'] == 'Yes'].shape[0]
# no_count = df[df['Bechdel_test'] == 'No'].shape[0]
# total_responses = len(df)

# # Calculate percentages
# yes_percentage = (yes_count / total_responses) * 100
# no_percentage = (no_count / total_responses) * 100

# # Print results
# print(f"Percentage of 'Yes': {yes_percentage:.2f}%")
# print(f"Percentage of 'No': {no_percentage:.2f}%")


# # Sort the DataFrame by the 'Rating' column in descending order
# sorted_df = df.sort_values(by='Rating', ascending=False)

# # Select the top 5 highest rated movies
# top_5_movies = sorted_df.head(5)

# # Display the results
# print("Top 5 Highest Rated Movies:")
# print(top_5_movies[['Movie_Name', 'Rating' , 'Bechdel_test']])

# # Sort the DataFrame by the 'Rating' column in descending order
# sorted_df = df.sort_values(by='Rating', ascending=True)

# # Select the bottom 5 highest rated movies
# bottom_5_movies = sorted_df.head(5)

# print("Bottom 5 Least Rated Movies")
# print(bottom_5_movies[['Movie_Name', 'Rating', 'Bechdel_test']])

# input_year = int(input("Enter the year: "))

# # Filter the DataFrame based on the input year
# filtered_df = df[df['year'] == input_year].copy()  # Make a copy to avoid SettingWithCopyWarning

# # Check if there are movies from the specified year
# if filtered_df.empty:
#     print(f"No movies found for the year {input_year}.")
# else:
#     # Clean and standardize Bechdel_test column values
#     filtered_df.loc[:, 'Bechdel_test'] = filtered_df['Bechdel_test'].str.strip().str.capitalize()

#     # Calculate percentages based on the filtered dataset
#     yes_count = filtered_df[filtered_df['Bechdel_test'] == 'Yes'].shape[0]
#     no_count = filtered_df[filtered_df['Bechdel_test'] == 'No'].shape[0]
#     total_responses = len(filtered_df)

#     # Calculate percentages
#     yes_percentage = (yes_count / total_responses) * 100
#     no_percentage = (no_count / total_responses) * 100

#     # Display the movies from the specified year
#     print(f"Movies from the year {input_year}:")
#     print(filtered_df[['Movie_Name', 'Rating', 'Bechdel_test', 'year']])
    
#     # Print results
#     print(f"Percentage of 'Yes': {yes_percentage:.2f}%")
#     print(f"Percentage of 'No': {no_percentage:.2f}%")



    
# Assuming the responses are in a column named 'Response'
yes_count = df[df['The_Mako_Mori_Test'] == 'Yes'].shape[0]
no_count = df[df['The_Mako_Mori_Test'] == 'No'].shape[0]
total_responses = len(df)

# Calculate percentages
yes_percentage = (yes_count / total_responses) * 100
no_percentage = (no_count / total_responses) * 100

# Print results
print(f"Percentage of 'Yes' for The_Mako_Mori_Test: {yes_percentage:.2f}%")
print(f"Percentage of 'No' for The_Mako_Mori_Test: {no_percentage:.2f}%")

# Sort the DataFrame by the 'Rating' column in descending order
sorted_df = df.sort_values(by='Rating', ascending=False)

# Select the top 5 highest rated movies
top_5_movies = sorted_df.head(5)

# Display the results
print("Top 5 Highest Rated Movies:")
print(top_5_movies[['Movie_Name', 'Rating' , 'The_Mako_Mori_Test']])

# Sort the DataFrame by the 'Rating' column in descending order
sorted_df = df.sort_values(by='Rating', ascending=True)

# Select the bottom 5 highest rated movies
bottom_5_movies = sorted_df.head(5)

print("Bottom 5 Least Rated Movies")
print(bottom_5_movies[['Movie_Name', 'Rating', 'The_Mako_Mori_Test']])

input_year = int(input("Enter the year: "))

# Filter the DataFrame based on the input year
filtered_df = df[df['year'] == input_year].copy()

# Check if there are movies from the specified year
if filtered_df.empty:
    print(f"No movies found for the year {input_year}.")
else:
    # Calculate counts for 'Yes' and 'No' responses in the filtered DataFrame
    yes_count = filtered_df[filtered_df['The_Mako_Mori_Test'] == 'Yes'].shape[0]
    no_count = filtered_df[filtered_df['The_Mako_Mori_Test'] == 'No'].shape[0]
    total_responses = len(filtered_df)

    # Calculate percentages
    yes_percentage = (yes_count / total_responses) * 100
    no_percentage = (no_count / total_responses) * 100

    # Display the movies from the specified year
    print(f"Movies from the year {input_year}:")
    print(filtered_df[['Movie_Name', 'Rating', 'The_Mako_Mori_Test', 'year']])
    
    # Print results
    print(f"Percentage of 'Yes': {yes_percentage:.2f}%")
    print(f"Percentage of 'No': {no_percentage:.2f}%")