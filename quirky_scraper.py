import urllib.request
from urllib.request import Request
from bs4 import BeautifulSoup
from time import sleep
import json
import random
import requests

def get_json(url):
    current_json = requests.get(url)
    with open('data.json','w') as f:
        json.dump(current_json.content, f)




def make_url(user_id, ending=None):
    '''
    returns url for a page in followers or following of the user profile. 

    PARAMETER
    ----------
    user_id: the user whoes page you are on
    ending: leave blank for first page, for other pages insert the last
        relationship's created_by attribute
    '''
    section1 = 'https://invent.quirky.com/api/v1/user_profile/'
    user_id = str(user_id)
    section2 = '/following?paginated_options%5Bfollows%5D%5Buse_cursor%5D=true&paginated_options%5Bfollows%5D%5Bper_page%5D=12&paginated_options%5Bfollows%5D%5Border_column%5D=created_at&paginated_options%5Bfollows%5D%5Border%5D=desc'
    if ending == None:
        ending = ''
    else:
        section3 = '&paginated_options%5Bfollows%5D%5Bcursor%5D='
        ending = section3 + ending

    url = section1 + user_id + section2 + ending
    return url


url = make_url('164569')
get_json(url)
