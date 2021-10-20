'''
I am here to see if the documentation of a module works!
'''
from bs4 import BeautifulSoup  # type: ignore
import requests
x = 'I have changed again'
y = 'Y am I here?'


def get_html(url: str) -> BeautifulSoup:
    """
    Get the HTML of a URL

    Parameters
    ----------
    url : str
        The URL to get the HTML of

    Returns
    -------
    str
        The HTML of the URL
    """
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text, 'html.parser')
    else:
        return None


if __name__ == '__main__':
    get_html('https://www.google.com')
    
    def addition(a, b):
        return a + b

    addition(10,2)
