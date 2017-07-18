import logging
# logging.basicConfig(level=logging.DEBUG)
import requests
from bs4 import BeautifulSoup
from  Scraper import Extract

"""
Main scraper methods
These are to scrape actor and movie pages for further links
They call the Extract methods to get more specific information that is then passed to Main
"""


def scrape_actor(url):
    """
    Scrapes the actor page to find the filmography
    Iterates through the filmography and returns links to movies that are sent to Extract for further processing
    :param url: URL of actor page to be scraped
    """
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')

    head = soup.find(id='Filmography')
    if head is not None:
        logging.info('Filmography has been found')
        children = head.find_next('ul')
        a = children.findAll('a')

        for child in a:
            logging.debug('In Loop')
            if child.has_attr('href'):
                logging.info('Scraping actor https://en.wikipedia.org' + child['href'])
                actor_data = Extract.get_actor_details(url)
                if ('/wiki/' not in child['href']) or (actor_data == 0):
                    logging.error('Not a wikipedia link')
                    return 0
                if actor_data is not 0:
                    logging.error("Got movie data")
                    actor_data.append("https://en.wikipedia.org" + child['href'])
                    print(actor_data)
                    return actor_data
                else:
                    logging.error("Couldn't get movie data")
                    return 0

    logging.error('Filmography has not been found')
    return 0


def scrape_movie(url):
    """
    Scrapes the movie page to find the cast
    Iterates through the cast and returns links to actors that are sent to Extract for further processing
    :param url: URL of movie page to be scraped
    """
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')

    head = soup.find(id='Cast')
    if head is not None:
        logging.info('Cast has been found')
        children = head.find_next('ul')
        a = children.findAll('a')

        for child in a:
            logging.debug('In Loop')
            if child.has_attr('href'):
                logging.info('Scraping actor https://en.wikipedia.org' + child['href'])
                movie_data = Extract.get_movie_details(url)
                if ('/wiki/' not in child['href']) or (movie_data == 0):
                    logging.error('Not a wikipedia link')
                    return 0
                if movie_data is not 0:
                    logging.error("Got actor data")
                    movie_data.append("https://en.wikipedia.org" + child['href'])
                    print(movie_data)
                    return movie_data
                else:
                    logging.error("Couldn't get actor data")
                    return 0

    logging.error('Cast has not been found')
    return 0

if scrape_actor("https://en.wikipedia.org/wiki/Matt_Damon") == 0:
    logging.critical("What are you feeding me")

if scrape_movie("https://en.wikipedia.org/wiki/Million_Dollar_Baby") == 0:
    logging.critical("What are you feeding me")
