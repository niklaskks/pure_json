IMPORT_UNCONFIGURED = True

LAYOUT = {
    # all columns will be imported and renamed to camelcase unless configured here
    # format: "excel_column_name": "data field name"
    "MPID": "uid",
    "Title English": "name",
    "Specification": "%splitdata ~ :",
}
