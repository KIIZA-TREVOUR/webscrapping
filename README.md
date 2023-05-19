# Twitter Scraping

This repository contains Python code for scraping Twitter data based on company names.

## Prerequisites

You can install these dependencies by running the file requiremets.txt using pip
pip install -r requirements.txt

## Functionality
google_search(company_name)
This function performs a Google search for the given company name and returns the URL of the search results page.

get_twitter_profile_link(company_name)
This function takes a company name, performs a Google search for the company's Twitter profile link, and returns the link if found. If the link is not found or an error occurs, it returns an appropriate message.

get_twitter_handle(twitter_profile_url)
This function takes a Twitter profile URL, uses Selenium with Chrome WebDriver to retrieve the handle of the user, and returns the handle. If an exception occurs, it prints an error message and returns None.

write_handles(filename, handles)
This function takes a filename and a list of handles, and writes the handles to the specified file. If an error occurs, it prints an error message.

## Tests
To run the tests for the implemented functions, you can use the command:
pytest
This ensures that the functions are working correctly and producing the expected outputs.