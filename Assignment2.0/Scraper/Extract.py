import logging
# logging.basicConfig(level=logging.INFO)
import requests
import re
from bs4 import BeautifulSoup

"""
Extract methods
These are to scrape actor and movie pages for specific information
They return a dict with the name first and year/age second
"""


def get_actor_details(url):
    """
    Scrapes the actor page to find the age and name
    Returns a dict with the name as the first elemet and age as the second
    :param url: URL of actor page to be scraped
    """
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    logging.info('Soup has been cooked')

    head = soup.find('span', class_='fn')
    if head is not None:
        logging.info('Name is found')
        name = head.contents[0]
    else:
        logging.info('Name is not found')
        return 0

    head = soup.find('span', class_='noprint ForceAgeToShow')
    if head is not None:
        logging.info('Age is found')
        head = head.contents[0]
        # http://stackoverflow.com/questions/11339210/how-to-get-integer-values-from-a-string-in-python
        age = int(re.search(r'\d+', head).group())
    else:
        logging.info('Age is not found')
        age = 50

    data_set = [name, age]

    logging.info('Data has been sent')
    return data_set


def get_movie_details(url):
    """
    Scrapes the movie page to find the name and year
    Returns a dict with the name as the first element and the year as the second
    :param url: URL of actor page to be scraped
    """
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    logging.info('Soup has been cooked')

    head = soup.find('th', class_='summary')
    if head is not None:
        logging.info('Name is found')
        name = head.contents[0]
    else:
        logging.info('Name is not found')
        return 0

    head = soup.find('span', class_='bday dtstart published updated')
    if head is not None:
        logging.info('Year is found')
        head = head.contents[0]
        # http://stackoverflow.com/questions/11339210/how-to-get-integer-values-from-a-string-in-python
        year = int(re.search(r'\d+', head).group())
    else:
        logging.info('Age is not found')
        year = 50

    data_set = [name, year]

    logging.info('Data has been sent')
    return data_set

# get_actor_details("https://en.wikipedia.org/wiki/Morgan_Freeman")
# get_movie_details("https://en.wikipedia.org/wiki/Invictus_(film)")
