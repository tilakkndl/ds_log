import data_load
filepath = "data/file-append.txt"
status, content = data_load.load_text_data(filepath)
print(f'{status = }, {content = }')
