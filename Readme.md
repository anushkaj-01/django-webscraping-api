# Scraping Application

This is a web scraping application built using Django and Selenium. It allows users to scrape data from dynamic websites and store the scraped data in a PostgreSQL database. This README provides instructions on how to set up and run the scraping application.

## Dependencies

- Python 3.x
- Django
- Selenium
- Chrome WebDriver
- PostgreSQL

## Installation

1. Clone the repository:

    git clone <repository-url>
    cd <repository-directory>

2. Install Python 3.x: Follow the instructions on the [official Python website](https://www.python.org/) to install Python.

3. Install dependencies listed in `requirements.txt`:

    pip install -r requirements.txt

4. Download and install Chrome WebDriver:

    pip install webdriver-manager

5. Set up PostgreSQL: Install PostgreSQL and create a new database. Update the database settings in `settings.py` with your PostgreSQL database connection details.

6. Run database migrations:

    python3 manage.py makemigrations
    python3 manage.py migrate

## Usage

1. Start the Django development server:

    python3 manage.py runserver

2. Access the scraping endpoints:

   - `http://127.0.0.1:8000/scrapeMovies/`: Scrapes movie data from https://www.scrapethissite.com/pages/ajax-javascript/ and saves it to the PostgreSQL database.

   - `http://127.0.0.1:8000/scrapeHockeyTeams/`: Scrapes hockey team data from https://www.scrapethissite.com/pages/forms/ and saves it to the PostgreSQL database.
     
   Access through browser,postman or any api testing tool

3. View scraped data:
   - Access the Django admin interface at `http://127.0.0.1:8000/admin/`.
   - Log in with the superuser account created during migration to view and manage scraped data.

   If haven't create using:

    python3 manage.py createsuperuser
