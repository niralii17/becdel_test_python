# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:12:38 2024

@author: Nirali Parikh
"""


import requests
from bs4 import BeautifulSoup
import csv

# Your code continues here


# List of movies with IMDb URLs
movies = [
     'https://www.imdb.com/title/tt7098658/',
    'https://www.imdb.com/title/tt15354916/',
    'https://www.imdb.com/title/tt22086334/?ref_=nv_sr_srsg_3_tt_7_nm_1_in_0_q_dream%2520gi',
    'https://www.imdb.com/title/tt14914988/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt15576460/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt15302222/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt15281704/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt11905536/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt14295590/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt13130948/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt1187043/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_3%2520Idiots',
    'https://www.imdb.com/title/tt2338151/?ref_=nv_sr_srsg_0_tt_4_nm_4_in_0_q_PK',
    'https://www.imdb.com/title/tt5074352/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt0169102/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt0172684/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_Kuch%2520Kuch%2520Hota%2520Hai',
    'https://www.imdb.com/title/tt0248126/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt3322420/',
    'https://www.imdb.com/title/tt2631186/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt4849438/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt2395469/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt3863552/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt5935704/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt2082197/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt0871510/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt0292490/?ref_=nv_sr_srsg_0_tt_5_nm_1_in_0_q_Dil%2520Chahta%2520Hai',
    'https://www.imdb.com/title/tt1093370/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt1562872/?ref_=nv_sr_srsg_0_tt_2_nm_0_in_0_q_Zindagi%2520Na%2520Milegi%2520Dobara',
    'https://www.imdb.com/title/tt5946128/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt0986264/?ref_=nv_sr_srsg_0_tt_4_nm_1_in_0_q_Taare%2520Zameen%2520Par',
    'https://www.imdb.com/title/tt0367110/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt0238936/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt3767372/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt5286444/?ref_=nv_sr_srsg_0_tt_3_nm_5_in_0_q_Neerja',
    'https://www.imdb.com/title/tt4387040/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt8108198/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt10324144/?ref_=fn_al_tt_1',   
    'https://www.imdb.com/title/tt4635372/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt2350496/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt7725596/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt8108202/?ref_=nv_sr_srsg_0_tt_7_nm_1_in_0_q_Stree',
    'https://www.imdb.com/title/tt7098658/?ref_=nv_sr_srsg_0_tt_6_nm_2_in_0_q_Raazi',
    'https://www.imdb.com/title/tt6791730/?ref_=nv_sr_srsg_0_tt_2_nm_1_in_0_q_Tumhari%2520Sulu',
    'https://www.imdb.com/title/tt5571734/',
    'https://www.imdb.com/title/tt6108090/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt2181931/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_English%2520Vinglish',
    'https://www.imdb.com/title/tt1694542/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt2980794/?ref_=fn_al_tt_5',
    'https://www.imdb.com/title/tt0242519/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_Hera%2520Pheri',
    'https://www.imdb.com/title/tt0374887/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt1285241/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_Don%25202',
    'https://www.imdb.com/title/tt0405508/?ref_=nv_sr_srsg_0_tt_2_nm_1_in_0_q_Rang%2520De%2520Basanti',
    'https://www.imdb.com/title/tt1821480/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt2359810/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt3735246/?ref_=nv_sr_srsg_0_tt_3_nm_1_in_0_q_Bajirao%2520Mastani',
    'https://www.imdb.com/title/tt0420332/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt2178470/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt8130968/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_Badla',
    'https://www.imdb.com/title/tt6971752/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt6484982/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt2016894/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt8108200/?ref_=nv_sr_srsg_0_tt_2_nm_2_in_0_q_Sonchiriya',
    'https://www.imdb.com/title/tt4535650/?ref_=nv_sr_srsg_0_tt_6_nm_2_in_0_q_Dilwale',
    'https://www.imdb.com/title/tt7430722/',
    'https://www.imdb.com/title/tt8291224/?ref_=fn_al_tt_1',
    'https://www.imdb.com/title/tt8239946/?ref_=nv_sr_srsg_0_tt_7_nm_1_in_0_q_Tumbbad',
    'https://www.imdb.com/title/tt6527426/',
    'https://www.imdb.com/title/tt6277440/?ref_=nv_sr_srsg_0_tt_1_nm_0_in_0_q_Badrinath%2520Ki%2520Dulhania',
    
    
]

# Define a User-Agent header to mimic a web browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


csv_filename = "d:\\Movies_project1.csv"
csv_file= open(csv_filename,"w",encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Movie Name', 'Rating' ])

# Iterate over each movie and scrape IMDb page
for movie in movies:
    url = movie
    
    if url:  # Check if URL is not empty
        # Send a GET request to the URL with the headers
        response = requests.get(url, headers=headers)

        print(response, response.status_code)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the page content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the movie title
            title = soup.find('h1').text.strip() if soup.find('h1') else 'N/A'

            # Extract the number of ratings
            rating_count = soup.find('div', {'data-testid': 'hero-rating-bar__aggregate-rating__score'})
            rating_count = rating_count.text.strip() if rating_count else 'N/A'
            
            # # Extract the movie release date
            # release_date = soup.find('span', {'data-testid': 'title-details-releasedate'})
            # release_date = release_date.text.strip() if release_date else 'N/A'
            
            csv_writer.writerow([title,rating_count,release_date ])
           
            # Print the extracted information
            print(f"Title: {title}")
            print(f"Number of Ratings: {rating_count}")
            # print(f"Release Date: {release_date}")

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    else:
        print(f"No URL provided for movie: {movie['title']}")
