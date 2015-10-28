#!/usr/bin/env python3

from cfg import file_name, auth_token, content_project_id
from check import setup
from run import proceed


if __name__ == '__main__':
    try:
        setup(file_name, auth_token, content_project_id)
        proceed(file_name)
    except AssertionError as e:
        print(e)
