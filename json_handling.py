import json
import os

def get_last_created_at(json_filename):
    '''
    Takes as input the STRING name of json_file imported into the /json_data folder.

    Returns the STRING of the last "created_at" element in the "follows" list. Returns true or false for whether or
    not there is a next page available to press the "load more" button to reach.

    The last "created_at" element is used to define the URL for the next load page request.
    '''
    working_directory = os.getcwd()
    file_path = working_directory + "\\json_data\\" + json_filename
    json_data = open(file_path)
    jdata = json.load(json_data)
    last_created_at = jdata['data']['follows'][-1]['created_at']
    has_next_page = jdata['paginated_meta']['follows']['has_next_page']
    return last_created_at, has_next_page

print(get_last_created_at('following.json'))


