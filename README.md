# pure_json
Convert and upload data into `ATML3Developer` and `Pure Data` projects via the API.

Source files can be json, csv or xslx.

## Getting Started
1. Clone this repo
1. Either
 1. Create a virtualenv with python3 as interpreter and then ```pip install -r requirements.txt``` **or**
 2. Install all packages named in `requirements.txt`

## Upload Data
1. Put your **json file** into the `upload` directory
1. Get your **auth_token** from ax semantics
1. Find or create your appropriate content project and remember its **number**
1. Open `upload/cfg.py` and set up the variables:

 ```python
 auth_token = '1234567890abcdef1234567890abcdef12345678'
 file_name = 'this_is.json'
 content_project_id = 99999999999999
 ```
1. Save that file
1. Execute `uploader/upload-file.py` in your preferred fashion (cli, from IDE, make executable and double-click...)
 - Keep in mind that this tool requires python3!

## Convert .xslx to .json
1. Put your **xslx file** into the `json_extractor` directory
2. Open `json_extractor/config.py` and set the required variables to map .xslx column names to key names.
  1.  map the one field that is your unique identifier to the field "uid"
  2.  map the one field that names your item to the field "name" (to identify the item in lists)
  3.  you can extract list fields (e.g. value1~value2~value3) in xlsx with `splitfied` command into a json dict by specifying the separator
  4.  you can extract key-value lists in fields (e.g. key1:value1~key1:value2~key3:value3) in xlsx with `splitdata` command into a json dict by specifying both separators
3. Set the `IMPORT_UNCONFIGURED` variable to `False` to only import fields specified in the `LAYOUT` dict.
4. Run `excel_extractor.py /path/to/file.xslx`

## Tips and Tricks

**auth_token** should consist of 40 hexadecimal characters.

**content_project_id** always is a number, not a string.

**file_name** should only contain the name of the file and *not* its path. This file must reside in the same directory as `upload.py`.

