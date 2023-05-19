import pytest

from main import google_search, get_twitter_profile_link, get_twitter_handle,write_handles


def test_google_search():
    output = 'https://www.google.com/search?q=amazon&ie=utf-8&oe=utf-8'
    input = google_search("amazon")
    
    assert isinstance(input, str)
    assert input == output

def test_get_twitter_profile_link():
    output = 'https://twitter.com/amazon'
    input = get_twitter_profile_link("amazon")
    assert isinstance(input, str)
    assert input == output
    
def test_get_twitter_handle():
    twitter_profile_url = "https://twitter.com/amazon"
    input = get_twitter_handle(twitter_profile_url)
    output = '@amazon'
    assert isinstance(input, str)
    assert input == output

def test_write_handles():
    # Test to ensure write_handles writes a file with the correct content
    filename = "handles.txt"
    handles = ["@amazon", "@lyft", "@airbnb"]
    write_handles(filename, handles)
    with open(filename, "r") as file:
        content = file.read()
    assert content == "@amazon@lyft@airbnb"
