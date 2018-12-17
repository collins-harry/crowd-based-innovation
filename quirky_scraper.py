import urllib.request
from urllib.request import Request
from bs4 import BeautifulSoup
from time import sleep
import json
import random
import requests

def get_json(url):
    # payload = {
    #     "username": "<USER NAME>",
    #     "password": "<PASSWORD>",
    #     "csrfmiddlewaretoken": "<CSRF_TOKEN>"
    # }
    current_json = requests.get(url)
    data = current_json.json()
    with open('data.json','w') as f:
        json.dump(data, f)




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
print(url)
get_json(url)

# APPROACH 1 !!!

# client = requests.session()
# # Retrieve the CSRF token first
# csrf = client.get(url).cookies['csrftoken']
#
# login_data = {'username': 'subscribesuhaib@gmail.com', 'password': 'harryisagirl', 'csrfmiddlewaretoken': csrf, 'next': '/'}
# r = client.post(url, data=login_data, headers=dict(Referer=url))
# print(r.status_code)

# APPROACH 2 !!!

# import requests
# from bs4 import BeautifulSoup
#
# client = requests.Session()
# headers = {'User-Agent': 'Mozilla/5.0'}
#
# soup = BeautifulSoup(client.get(url).text, "html.parser")
# csrf = soup.find(name="authentication_token")
# print(csrf)

# APPROACH 3 !!!

# #This URL will be the URL that your login form points to with the "action" tag.
# POSTLOGINURL = 'https://dashboard.quirky.com/login'
#
# #This URL is the page you actually want to pull down with requests.
# REQUESTURL = url
#
# payload = {
#     'username': 'subscribesuhaib@gmail.com',
#     'pass': 'harryisagirl'
# }
#
# with requests.Session() as session:
#     post = session.post(POSTLOGINURL, data=payload)
#     r = session.get(REQUESTURL)
#     print(session.cookies)
#     print(r.text)   #or whatever else you want to do with the request data!