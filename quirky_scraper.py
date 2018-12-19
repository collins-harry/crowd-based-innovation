import urllib.request
from urllib.request import Request
from bs4 import BeautifulSoup
from time import sleep
import json
import random
import requests

def main():
    urls = [
        'https://dashboard.quirky.com/login',
        'https://webhook.site/da5b6b99-7583-49d4-b2d9-c4ce8149d977',
        'https://dashboard.quirky.com/'
        ]

    payload = {
        'username': 'subscribesuhaib@gmail.com',
        'password': 'harryisagirl'
    }

    # response = one_method(urls[1], payload)
    post = two_method(urls[1], payload)
    
    print(f'\npost.text: {post.text}')
    # display_response(response)
    display_response(post)
    
    
def display_response(response):
    print(f'\nheader: {response.headers}')
    print(f'\ncontent: {response.content}')
    print(f'\ncookies: {response.cookies}')
    print(f'\njson: {response.json}')
    
def one_method(url, payload):
    r = requests.post(
            url, 
            auth = (payload['username'], payload['password'])
            )
    return r

def two_method(url, payload):
    with requests.Session() as session:
        post = session.post(url, data=payload)
        # r = session.get(REQUESTURL)
        return post



def cookie_creator():
    ''' manually creates a cookie '''
    section1 = '__cfduid='
    cfduid = 'd6d05af6e570bb84fb588c75246e70e351544454308'
    section2 = '; _quirky_auth='
    auth = 'VTJGc2RHVmtYMS9MbjJGdzBtay9BZWpJQVhja2Y0c2tWeVUyOFJWMXcxSkZ0dlgwaWJPaUNKUWpwV3BZCndKZzZIQ2huNlJienhwRGtCR0tCY0JNTlB3PT0%3D' 
    section3 = '; _quirky_user=1352112; _ga=GA1.2.2144556413.1544622507; _gid=GA1.2.1646086641.1544983294; _quirky_v2_production_session='
    cookie_end = 'UVJiUXZlWUN0aHRBdGlVQ3hTWThyUXYyUHBKeFBSbE1SMDc3RnIwbzJKc3hIeU9SZFI4b1NjSFNDNG5qVHhIVi92dmpEZ3RPK2ttUzZWaVNnd2VFVVBlMUVjK2dML3kzSUpGd1Z1T2ZjdEdoNFBNUUtrQWU0dGd3UVI2a09HOFcyNXJOaU4wbW95UmJvLzZIMlZlRUJySkE0VDN5N0E4dkp6TEwzTEFKUzVPZkVHbEJMaTk5MUM5VGJOTVErajFDVVlDZUtLcjI5RWhJUDRSNFY4YXp5a1grdjFhT1pYWHF2YVdQQ2xTZWVuc282Z1I4aWhaQ3BKLzlucU5kUStTYi0tWFh5Zk9sblN1bXl2YkI2ZXFPYTNsdz09--46825b69a981e1a66aea1c3fc2f4f23919cb4966'
    cookie = section1+cfduid+section2+auth+section3_cookie_end
    return cookie

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
    section1 = 'http://invent.quirky.com/api/v1/user_profile/'
    user_id = str(user_id)
    section2 = '/following?paginated_options%5Bfollows%5D%5Buse_cursor%5D=true&paginated_options%5Bfollows%5D%5Bper_page%5D=12&paginated_options%5Bfollows%5D%5Border_column%5D=created_at&paginated_options%5Bfollows%5D%5Border%5D=desc'
    if ending == None:
        ending = ''
    else:
        section3 = '&paginated_options%5Bfollows%5D%5Bcursor%5D='
        ending = section3 + ending
    url = section1 + user_id + section2 + ending
    return url

def get_page(url, cookie=''):
    '''
    returns the page json for a given url
    
    PARAMETERS
    ----------
    url: output of the 'make url' function
    '''
    headers = {'cookie': cookie}
    #r = requests.get(url)
    print(r)
    print('=========headers=========\n', r.headers)
    print('=========text=========\n', r.text)
    print('=========json=========\n', r.json)

if __name__ == '__main__':
    main()

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
