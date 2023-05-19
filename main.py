import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from random import randint
from urllib.parse import urljoin



def google_search(company_name):
    """Performs a Google search for the given company name."""
    try:
        query = urllib.parse.quote_plus(company_name)
        url = f'https://www.google.com/search?q={query}&ie=utf-8&oe=utf-8'
    except urllib.error.URLError as err:
        print(f'Error: {err}')
    else:
        return url



def get_twitter_profile_link(company_name):
    try:
        company = company_name + ' Company Twitter link'
        search_url = f"https://www.google.com/search?q={company}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find('div', class_='yuRUbf')
        link = result.find('a')['href']
        if 'twitter.com' in link:
            return link
        else:
            return "Twitter Link Not Found"
    except AttributeError as e:
        return "Twitter Link Not Found"
    except Exception as e:
        return "Error"
    

def get_twitter_handle(twitter_profile_url):
    ''' This function takes a Twitter profile URL and returns the handle of the user '''
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(twitter_profile_url)
        state = ""
        while state != "complete":
            print("Coming soon! Still loading")
            time.sleep(randint(2, 5))
            state = driver.execute_script("return document.readyState")
        result = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserName"]').text.split('\n')
        driver.quit()
        return  result[1]
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

def write_handles(filename, handles):
    try:
        with open(filename, "w") as file:
            for handle in handles:
                file.write(f"{handle}")
    except Exception as e:
        print(f"An Error occured: {e}")
        
