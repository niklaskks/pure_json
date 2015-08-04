# pure_json
Upload json data into `Pure Data` projects via api.

## Getting started
1. Clone this repo
1. Either
 1. Create a virtualenv with python3 as interpreter and then ```pip install -r requirements.txt``` **or**
 2. Install package `requests` for your python3 interpreter
1. Put **json file** into created directory
1. Get your **auth_token** from ax semantics
1. Find or create your appropriate content project and remember its **number**
1. Open `cfg.py` and set up the variables:

 ```python
 auth_token = '1234567890abcdef1234567890abcdef12345678'
 file_name = 'this_is.json'
 content_project_id = 99999999999999
 ```
1. Save that file
1. Execute `upload-file.py` in your preferred fashion (cli, from IDE, make executable and double-click...)
 - Mind that this tool requires python3!

## Tips and Tricks

**auth_token** should consist of 40 hexadecimal characters.

**content_project_id** always is a number, not a string.

**file_name** should only contain the name of the file and *not* its path. This file must reside in the same directory as `upload.py`.

