import urllib.request
from urllib.request import Request
from bs4 import BeautifulSoup
from time import sleep
import json
import random
import re

initial_url = 'https://invent.quirky.com/api/v1/user_profile/765514/following?paginated_options%5Bfollows%5D%5Buse_cursor%5D=true&paginated_options%5Bfollows%5D%5Bper_page%5D=12&paginated_options%5Bfollows%5D%5Border_column%5D=created_at&paginated_options%5Bfollows%5D%5Border%5D=des'

def make_url(user_id, ending=''):
    section = 'https://invent.quirky.com/api/v1/user_profile/'
    section2 = '/following?paginated_options%5Bfollows%5D%5Buse_cursor%5D=true&paginated_options%5Bfollows%5D%5Bper_page%5D=12&paginated_options%5Bfollows%5D%5Border_column%5D=created_at&paginated_options%5Bfollows%5D%5Border%5D=des'
    url = section1 + user_id + section2 + ending
    return url

print(make_url(5657))
