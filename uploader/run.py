
import os
import json
import requests
from collections import namedtuple

from cfg import ax_api_url, content_project_id, auth_token, DEBUG


selector = namedtuple('selector', ['name', 'uid'])


def get_data(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, mode='r') as f:
        try:
            json_doc = json.loads(f.read())
        except ValueError:
            # csv example
            import csv
            reader = csv.reader(open(file_path), delimiter=';')
            header = reader.__next__()
            json_doc = []
            for count, line in enumerate(reader):
                d = dict(zip(header, line))
                d['uid'] = str(count)
                json_doc.append(d)
    return json_doc


def proceed(file_name, max_count=None):
    """
    Uploads the file

     - open file
     - extract uid, name, pure_data
     - POST against api
    """
    data = get_data(file_name)
    for count, each_item in enumerate(data):
        if max_count and count >= max_count:
            break
        if DEBUG:
            print('uploading {}'.format(each_item))
        try:
            upload_line(each_item, count)
        except ValueError as e:
            print('Could not import one item: {}'.format(e))


def upload_line(item, count):
    """
    """
    url = ax_api_url.format(prefix='content-project', lookup=content_project_id)
    selectors = _get_selectors(item)

    payload = {
        'content_project': content_project_id,
        'name': selectors.name,
        'uid': selectors.uid,
        'pure_data': json.dumps(item),
    }
    headers = {
        'Authorization': 'Token {}'.format(auth_token),
    }
    r = requests.post(url, data=payload, headers=headers)

    if r.status_code == 201:
        print('.', end='')
    else:
        print()
        print('Error: {r.status_code}/{r.text}'.format(r=r))


def _get_selectors(data) -> selector:
    keys = data.keys()

    if 'routeid' in keys and 'start' in keys and 'destination' in keys:
        # flights
        name = '{} to {}'.format(data.get('start'), data.get('destination'))
        uid = data.get('routeid')
        return selector(name, uid)

    if 'product_id' in keys and 'product_name' in keys:
        return selector(data.get('product_name'), data.get('product_id'))

    if 'Hersteller' in keys and 'Modell' in keys:
        # kameras
        name = "{} {}".format(data.get('Hersteller'), data.get("Modell"))
        uid = data.get('uid')
        return selector(name, uid)

    raise ValueError('Cannot determine selectors from {}'.format(data))
