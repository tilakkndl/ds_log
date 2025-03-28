import os
def load_text_data(filepath:str):
    '''
    Load data from the given file path.
    '''
    print(f'Loading data from {filepath = }')
    # try:
    #     with open(filepath, 'r') as f:
    #         data = f.read()
    #     return data
    # except FileNotFoundError:
    #     print(f'File not found: {filepath}')
    #     return None
    
    if not os.path.exists(filepath):
        print(f'File not found: {filepath}')
        content = ""
        status = False
        # return None
    else:
        with open(filepath, 'r') as f:
                data = f.read()
                status = True
                content = data
    return content, status