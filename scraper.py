from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Setup driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31"
driver.get(url)

time.sleep(3)  # Wait for page to fully load

# Find all movie title elements
titles = driver.find_elements(By.CSS_SELECTOR, "a.ipc-title-link-wrapper h3")
descriptions = driver.find_elements(By.CLASS_NAME, "ipc-html-content-inner-div")

print("Total titles found:", len(titles))
print("Total descriptions found:", len(descriptions))
print("\nMovie Data:\n")

movies = []

for i in range(len(titles)):
    movie_name = titles[i].text

    if ". " in movie_name:
        movie_name = movie_name.split(". ", 1)[1]

    storyline = descriptions[i].text

    movie_data = {
        "Movie Name": movie_name,
        "Storyline": storyline
    }

    movies.append(movie_data)

print("Total movies collected:", len(movies))

import pandas as pd

df = pd.DataFrame(movies)

print(df.head())

df.to_csv("imdb_movies_2024.csv", index=False)
print("CSV file saved successfully!")