"""
Lesson 9 Assignments: Scraping, APIs, and Flask Integration
============================================================

Synchronized topics:
- BeautifulSoup scraping
- Selenium for dynamic pages
- API requests and JSON parsing
- Flask route integration

Important:
- This file is intentionally scaffold-only.
- Implement the TODO blocks yourself.
"""


# =============================
# Assignment 1: BeautifulSoup Scraper
# =============================
"""
Goal:
- Extract top 5 headlines from a public site (example: Hacker News).

Pseudo-code:
1. Send a GET request.
2. Parse HTML with BeautifulSoup.
3. Select headline elements with CSS selectors.
4. Print first 5 headline titles.
"""


def scrape_headlines():
    """
    Scrape top headlines from a static webpage.
    """
    # TODO: Import requests and BeautifulSoup.
    # TODO: Fetch page HTML.
    # TODO: Parse and print top headlines.
    pass


# =============================
# Assignment 2: Selenium Scraper
# =============================
"""
Goal:
- Scrape dynamically rendered content (for example quotes.toscrape.com/js/).
"""


def scrape_dynamic_content():
    """
    Use Selenium to scrape a JavaScript-rendered page.
    """
    # TODO: Configure WebDriver.
    # TODO: Open target page.
    # TODO: Extract and print 5 items.
    # TODO: Close browser.
    pass


# =============================
# Assignment 3: Public API Consumer
# =============================
"""
Goal:
- Consume one public API and print at least 3 useful fields.
"""


def fetch_api_data():
    """
    Fetch and summarize JSON data from a public API.
    """
    # TODO: Send API request and parse JSON.
    # TODO: Extract key fields and print formatted output.
    # TODO: Handle request exceptions.
    pass


# =============================
# Assignment 4: Mini Flask App
# =============================
"""
Goal:
- Build a Flask app with:
  - '/' route for home page
  - '/data' route showing API or scraping results
"""


def build_flask_app():
    """
    Scaffold for the Flask integration assignment.
    """
    # TODO: Create Flask app and define required routes.
    # TODO: Return rendered output for both endpoints.
    pass


# =============================
# Assignment 5 (Bonus): Dashboard
# =============================
"""
Goal:
- Visualize scraped/API data in Flask using matplotlib or plotly.
"""


def build_dashboard_extension():
    """
    Add charting to the Flask app as an optional bonus.
    """
    # TODO: Generate chart from collected data.
    # TODO: Render chart in HTML template.
    pass


if __name__ == "__main__":
    # TODO: Choose one assignment function to run while developing.
    pass
