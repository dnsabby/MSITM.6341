"""
Lesson 9 Examples: Web Scraping, APIs, and Flask Integration
=============================================================

Synchronization note:
- This file is aligned with `Lesson09/Exercises/exercises.py`.
"""

"""
SECTION 1: Web Scraping with BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup

# Get HTML content from a different webpage (not used in exercises)
url = "https://www.python.org/blogs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract latest blog titles
blogs = soup.select('.list-recent-posts li > a')
for i, blog in enumerate(blogs[:5]):
    print(f"{i+1}. {blog.text.strip()}")


"""
SECTION 2: Web Scraping with Selenium
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/events/python-events/")

# Get event names and locations
events = driver.find_elements(By.CSS_SELECTOR, '.event-title a')
locations = driver.find_elements(By.CSS_SELECTOR, '.event-location')

for event, location in zip(events, locations):
    print(f"{event.text} in {location.text}")

# Close browser
driver.quit()


"""
SECTION 3: Consuming Web APIs with Requests
"""
import requests
import json

# Example: Open-Meteo public API (instead of CoinGecko)
api_url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"
response = requests.get(api_url)
data = response.json()

print("Current Temperature (New York):", data['current_weather']['temperature'], "°C")
print("Wind Speed:", data['current_weather']['windspeed'], "km/h")


"""
SECTION 4: Simple Flask App Example
"""
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Welcome to the Weather Info App!</h2>"

@app.route('/weather')
def show_weather():
    data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=34.05&longitude=-118.24&current_weather=true").json()
    temp = data['current_weather']['temperature']
    return f"Current temperature in Los Angeles: {temp} °C"

if __name__ == '__main__':
    app.run(debug=True)


"""
SECTION 5: Plotting with Matplotlib for Flask
"""
import matplotlib.pyplot as plt

# Sample data: monthly visitors to a website
months = ['Jan', 'Feb', 'Mar', 'Apr']
visitors = [120, 150, 170, 130]

# Plot and save
plt.plot(months, visitors, marker='o')
plt.title("Website Visitors by Month")
plt.xlabel("Month")
plt.ylabel("Visitors")
plt.grid(True)
plt.savefig("static/visitors_trend.png")
plt.close()

# Then embed in Flask template using:
# <img src="{{ url_for('static', filename='visitors_trend.png') }}">


"""
TIPS:
- Use `.env` file + `dotenv` package for API key storage.
- Use try/except blocks to handle connection errors.
- Cache or store results to avoid rate limits during development.
- Use Flask templates to render data dynamically.
"""
