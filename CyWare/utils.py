import requests


def process_GET_request(url):
    return requests.get(url)


def get_search_url(url, search_params):
    search_params_list = ['%s=%s' % (key, val) for key, val in search_params.iteritems()]
    search_params_str = '&'.join(search_params_list)
    if search_params_str:
        if '?' not in url:
            search_url = '{}?{}'.format(url, search_params_str)
        else:
            search_url = '{}&{}'.format(url, search_params_str)
    else:
        search_url = url
    return search_url
