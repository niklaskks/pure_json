#!/usr/bin/env python3
import json
import re
import sys

import pandas as pd

from config import (LAYOUT, IMPORT_UNCONFIGURED)


def splitdata(row_separator, value_separator, field):
    data = {}
    try:
        pairs = field.split(row_separator)
    except AttributeError:
        return data

    for pair in pairs:
        key, value = pair.split(value_separator)
        key = normalize_key(key)
        data[key] = value.strip()
    return data


def normalize_key(key):
    key = key.strip()
    key = re.sub(r'A-Za-z0-9_', '', key)
    key = key.title()
    return key


if __name__ == '__main__':
    try:
        xslx = pd.ExcelFile(sys.argv[-1])
    except FileNotFoundError:
        sys.exit('Could not find .xslx file {}.'.format(sys.argv[-1]))

    things = []
    sheet = xslx.parse(0)

    for index, row in sheet.iterrows():
        thing = {'pure_data':{}}

        for xslx_key in row.keys():
            if xslx_key in LAYOUT.keys():
                json_key = LAYOUT[xslx_key]
                #xslx_value = row[xslx_key].values()[0]
                xslx_value = row[xslx_key]

                if json_key in ['uid', 'name']:
                    thing[json_key] = xslx_value
                elif '%splitdata' in json_key:
                    separators = json_key.split(' ')
                    thing['pure_data'].update(splitdata(
                        separators[1],
                        separators[2],
                        xslx_value
                    ))
                else:
                    thing['pure_data'][json_key] = xslx_value
            elif IMPORT_UNCONFIGURED:
                if xslx_key in ['uid', 'name']:
                    thing[xslx_key] = xslx_value
                else:
                    thing['pure_data'][xslx_key] = xslx_value

        things.append(thing)

    with open('import.json', 'w') as fp:
        json.dump(things, fp)

    sys.exit('JSON data has been saved to import.json.')