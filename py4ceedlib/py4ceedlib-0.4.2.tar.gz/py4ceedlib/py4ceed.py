import ipywidgets as widgets
import difflib
import requests
import pandas as pd
import os
from os.path import expanduser
import subprocess
import warnings
import sys

#base_url='http://localhost:9000'
base_url='https://4ceed.illinois.edu'

warnings.filterwarnings("ignore")


# this is a pointer to the module object instance itself.
this = sys.modules[__name__]

# we can explicitly make assignments on it
this.meta_data = None

this.credentials = None

this.validated_credentials = False


def test_credentials(credentials):

    url = base_url + '/api/collections'

    response = requests.get(url, auth=credentials, verify=False)
    if response.status_code == 200:
        print("Successfully validated credentials")
        this.validated_credentials = True
    else:
        raise ValueError('Invalid credentials, please try again')
        this.validated_credentials = False
    #except:
        #pass

def get_all_spaces(credentials):
    url = base_url + '/api/spaces'
    return requests.get(url, auth=credentials, verify=False).json()

def get_all_collections(credentials):
    url = base_url + '/api/collections'
    colls = requests.get(url, auth=credentials, verify=False).json()
    detailed_colls = []
    for coll in colls:
        detailed_coll = get_collection_by_id(coll['id'],credentials)
        detailed_colls.append(detailed_coll)
    return detailed_colls

def get_collection_by_id(coll_id, credentials):
    url = base_url + '/api/collections/' + coll_id
    return requests.get(url, auth=credentials, verify=False).json()


def get_collections_for_space(space_id,credentials):
    url = base_url + '/api/spaces/'  + space_id + '/collections'
    colls = requests.get(url, auth=credentials, verify=False).json()
    detailed_colls = []
    for coll in colls:
        detailed_coll = get_collection_by_id(coll['id'],credentials)
        detailed_colls.append(detailed_coll)
    return detailed_colls


def get_datasets_for_collection(coll_id, credentials):
    url = base_url + '/api/collections/'  + coll_id + '/datasets'
    return requests.get(url, auth=credentials, verify=False).json()

def get_datasets_for_space(space_id, credentials):
    url = base_url + '/api/spaces/'  + space_id + '/datasets'
    return requests.get(url, auth=credentials, verify=False).json()

def get_files_for_dataset(dataset_id, credentials):
    url = base_url + '/api/datasets/' + dataset_id + '/files'
    return requests.get(url, auth=credentials, verify=False).json()

def get_text_metadata(file_id, file_path, credentials):
    url = base_url + '/api/files/' + file_id
    file_data = requests.get(url, auth=credentials, verify=False)
    df = parse_txt_metadata(file_data.text, file_id, file_path)
    return df

def get_template_by_dataset_id(dataset_id, credentials):
    url = base_url + '/t2c2/templates/getByDatasetId/' + dataset_id
    return requests.get(url, auth=credentials, verify=False).json()

def parse_txt_metadata(txt_data, file_id, file_path):
    metadata_dict = dict()
    if '=' in txt_data:
       return parse_another_txt_format(txt_data,file_id,file_path)
    lines = txt_data.split('\n')
    df = pd.DataFrame()
    for line in lines:
        key_value = line.split(':')
        if len(key_value) >= 2:
            attribute = key_value[0]
            value_tokens = key_value[1].split(' ')
            if len(value_tokens) >= 2:
                if value_tokens[1]:  # if second is not empty
                    try:
                        metadata_dict[attribute] = int(value_tokens[1])
                    except:
                        metadata_dict[attribute] = value_tokens[1]
    df = pd.DataFrame(metadata_dict, index=[file_path, ])
    return df

def parse_another_txt_format(txt_data, file_id, file_path):
    metadata_dict = dict()
    lines = txt_data.split('\n')
    df = pd.DataFrame()
    for line in lines:
        key_value = line.split('=')
        if len(key_value) >= 2:
            attribute = key_value[0]
            value_tokens = key_value[1].split(' ')
            if value_tokens[0]:  # if second is not empty
                try:
                    metadata_dict[attribute] = int(value_tokens[0])
                except:
                    metadata_dict[attribute] = value_tokens[0]
    df = pd.DataFrame(metadata_dict, index=[file_path, ])
    return df
########### End API calls to 4Ceed ################



def create_tree_for_collection(coll, dic_for_tree, tree_items, credentials, space=False, show_files=False):


    #if parent_coll:
       #current_coll_id = parent_coll + " " + coll['id']
    #else:
    current_coll_id = coll['id']
    if current_coll_id in dic_for_tree:
        return
    dic_for_tree[current_coll_id] = coll
    #dic_for_tree[current_coll_id]['column'] = coll_column
    dic_for_tree[current_coll_id]['datasets'] = dict()

    #if space:
    #    list_datasets = get_datasets_for_space(coll['id'], credentials)
    #else:
    #    list_datasets = get_datasets_for_collection(coll['id'], credentials)


    '''
    if show_files:
        list_files = get_files_for_dataset(dataset['id'], credentials)
        for file in list_files:
            # file_column = tree.insert(dataset_column, 3, file['id'], text=file['filename'], values = ( '              file', file['date-created']))
            file_column = tree.insert(dataset_column, 3, (coll['id'], dataset['id'], file['id']),
                                      text=file['filename'], values=('          file', file['date-created']))
            dic_for_tree[current_coll_id]['datasets'][dataset['id']]['files'][file['id']] = file
    '''

    #print(coll.keys())
    collection_accordions = []
    collection_names = []
    if space:
        # get space datasets
        list_datasets = get_datasets_for_space(coll['id'], credentials)

        # get space collections
        space_collections = get_collections_for_space(coll['id'], credentials)
        for space_coll in space_collections:
            coll_accordion = create_tree_for_collection(space_coll, dic_for_tree, tree_items, credentials)
            if coll_accordion:
                collection_accordions.append(coll_accordion)
                display_name = space_coll['name'] + u'\t\t(Collection)' #+ (20 - len(space_coll['name']) ) * ' ' + 'Space'
                #print("Display_name=", display_name)
                collection_names.append(display_name)
    else:
        # get collection datasets
        list_datasets = get_datasets_for_collection(coll['id'], credentials)

        #get child collections
        child_coll_ids = coll['child_collection_ids'] #val[val.find("(")+1:val.find(")")]
        str_child_coll_ids = child_coll_ids[child_coll_ids.find("(")+1:child_coll_ids.find(")")]
        if str_child_coll_ids:
            child_coll_ids = str_child_coll_ids.split(', ')
            for child_coll_id in child_coll_ids:
                try:
                    child_coll = get_collection_by_id(child_coll_id, credentials)
                    coll_accordion = create_tree_for_collection(child_coll, dic_for_tree, tree_items, credentials)
                    if coll_accordion:
                        collection_accordions.append(coll_accordion)
                        display_name = child_coll['name'] + u'\t\t(Collection)' # + (20 - len(child_coll['name'])) * ' ' + 'Space'
                        #print("Display_name=", display_name)
                        collection_names.append(display_name)
                except: # if not authorized to see child collection of a shared collection
                    pass

    # build the multi select widget for datasets
    dataset_info = []
    dataset_names = []
    for dataset in list_datasets:
        dic_for_tree[current_coll_id]['datasets'][dataset['id']] = dataset
        dic_for_tree[current_coll_id]['datasets'][dataset['id']]['files'] = dict()
        dataset_info.append((dataset['id'], dataset['name'], dataset['created']))
        dataset_names.append(dataset['name'])
    datasets_widget = multi_checkbox_widget(dataset_names)
    if dataset_names:
        tree_items.append( (datasets_widget, dataset_info) )

    #create accordon for current collections and datasets
    if dataset_names:
        children = collection_accordions + [datasets_widget]
    else:
        children = collection_accordions
    accordion = widgets.Accordion(children=children)
    for i in range(0, len(collection_names)):
        accordion.set_title(i, collection_names[i])
    if dataset_names:
        accordion.set_title(len(children) - 1, 'datasets')
        #coll_column = tree.insert(parent_coll, 1, (coll['id']), text=coll['name'],
        #                          values=('space', coll['created']))
    '''
    else:
        #try:
        if dataset_names:
            children = collection_accordions + [datasets_widget]
        else:
            children = collection_accordions
        accordion = widgets.Accordion(children=children)
        for i in range(0, len(collection_names)):
            accordion.set_title(i, collection_names[i])
        if dataset_names:
            accordion.set_title(len(children) - 1, 'datasets')
        '''

        #coll_column = tree.insert(parent_coll, 1, (coll['id']), text=coll['name'],
                                  #values=('collection', coll['created']))
        #except:
            #print(coll['name'], ' already exists')
            #return
    return accordion


def build_tree_view(credentials, show_files=False):
    ## Populate the ree
    dic_for_tree = dict()
    tree_items = []

    first_level_widgets = []
    first_level_names = []
    list_spaces = get_all_spaces(credentials)
    for space in list_spaces:
        #if "GaN" in space['name']:
        space_widget = create_tree_for_collection(space, dic_for_tree, tree_items, credentials, space=True, show_files=show_files)
        if space_widget:
            first_level_widgets.append(space_widget)
            first_level_names.append(space["name"] + u'\t\t(Space)')

    list_collection = get_all_collections(credentials)
    for collection in list_collection:
        coll_widget = create_tree_for_collection(collection, dic_for_tree, tree_items, credentials, show_files=show_files)
        if coll_widget:
            first_level_widgets.append(coll_widget)
            first_level_names.append(collection["name"] + u'\t\t(Collection)')
    
    accordion = widgets.Accordion(children=first_level_widgets)
    for i in range(0, len(first_level_names)):
        accordion.set_title(i, first_level_names[i])
    #accordion.set_title(len(collection_accordions) - 1, 'datasets')

    display(accordion)

    button = widgets.Button(description="Submit")
    display(button)
    #future_checked_items = asyncio.Future()
    checked_items = []

    def on_button_clicked(change):
        #see checked items

        for item in tree_items:
            widget = item[0]
            dataset_info = item[1]
            check_boxes = widget.children[0]
            for i in range (0,len(check_boxes.children)):
                if check_boxes.children[i].value:
                    checked_items.append(dataset_info[i])
        #future_checked_items.set_result(checked_items)
        #button.unobserve(on_button_clicked, 'value')
        if not checked_items:
            print("Please choose some datasets and try again")
        else:
            this.meta_data = display_data_frame(checked_items, credentials)
            display(this.meta_data)

    #@interact
    #def clicked(a=button):
        #print("Interact Button clicked.")
    #button.observe(on_button_clicked, 'value')
    #search_widget.observe(on_text_change, names='value')
    button.on_click(on_button_clicked)
    #print("Return to where I left off")
    #return future_checked_items
    '''
    multiples = widgets.SelectMultiple(
        options=['Apples', 'Oranges', 'Pears'],
        value=['Oranges'],
        #rows=10,
        description='',
        disabled=False
    )

    accordion = widgets.Accordion(children=[multiples])
    accordion.set_title(0, 'datasets')


    multi_checkbox = multi_checkbox_widget(['hello', 'world'])
    #display(widget)

    accordion2 = widgets.Accordion(children=[accordion, multi_checkbox])
    accordion2.set_title(0, 'child-collection')
    accordion2.set_title(1, 'datasets')

    accordion3 = widgets.Accordion(children=[accordion2, accordion2, accordion2])
    accordion3.set_title(0, 'space 1')
    accordion3.set_title(1, 'space 2')
    accordion3.set_title(2, 'space 3')
    display(accordion3)

    button = widgets.Button(description="Click Me!")
    display(button)

    def on_button_clicked(b):
        print("Button clicked.")

    button.on_click(on_button_clicked)
    '''
def display_data_frame(checked_items, credentials):
    meta_data_df = pd.DataFrame()

    for dataset_id, dataset_name, upload_data in checked_items:

        dataset_template = get_template_by_dataset_id(dataset_id, credentials)
        one_dataset_metadata = dict()
        for term in dataset_template[0]["terms"]:
            if '-----' not in term['default_value']:
                try:
                    one_dataset_metadata[term['key']] = float(term['default_value'])
                except:
                    one_dataset_metadata[term['key']] = term['default_value']

        df = pd.DataFrame(one_dataset_metadata, index=[dataset_name, ])
        meta_data_df = pd.concat([meta_data_df, df], axis=0, ignore_index=False)

    # fix column names
    meta_data_df.columns = meta_data_df.columns.str.strip().str.replace(u'\xa0', '_').str.replace('(', '').str.replace(
        ')', '')

    print("Done Retrieving ... ")

    return meta_data_df

def read_datasets_metadata():
    if not this.validated_credentials:
        print("Credentials are not validated, please execute py4ceed.enter_credentials() to enter your credentials")
        return
    print("Retrieving datasets ... ")
    check_items = build_tree_view(this.credentials, show_files=False)
    ###find checked items and put them in a dataframe
    '''
    checked_items = tree.get_checked()
    meta_data_df = pd.DataFrame()

    for item in checked_items:
        tokens = item.split(' ')

        dataset_id = tokens[-1]

        coll_id =""
        for id in tokens[:-1]:
            coll_id += id
        dataset_name = dic_for_tree[coll_id]['datasets'][dataset_id]['name']
        dataset_template = get_template_by_dataset_id(dataset_id, credentials)
        one_dataset_metadata = dict()
        for term in dataset_template[0]["terms"]:
            if '-----' not in term['default_value']:
                try:
                    one_dataset_metadata[term['key']] = float(term['default_value'])
                except:
                    one_dataset_metadata[term['key']] = term['default_value']


        df = pd.DataFrame(one_dataset_metadata, index=[dataset_name, ])
        meta_data_df = pd.concat([meta_data_df, df], axis=0, ignore_index=False)

    #fix column names
    meta_data_df.columns = meta_data_df.columns.str.strip().str.replace(u'\xa0', '_').str.replace('(', '').str.replace(')', '')

    print("Done Retrieving ... ")

    root.destroy()
    return meta_data_df
    '''
def get_metadeta():
    return this.meta_data

def multi_checkbox_widget(descriptions):
    """ Widget with a search field and lots of checkboxes """
    #search_widget = widgets.Text()
    options_dict = {description: widgets.Checkbox(description=description, value=False) for description in descriptions}
    options = [options_dict[description] for description in descriptions]
    options_widget = widgets.VBox(options, layout={'overflow': 'scroll'})
    #multi_select = widgets.VBox([search_widget, options_widget])
    multi_select = widgets.VBox([options_widget])

    # Wire the search field to the checkboxes
    def on_text_change(change):
        search_input = change['new']
        if search_input == '':
            # Reset search field
            new_options = [options_dict[description] for description in descriptions]
        else:
            # Filter by search field using difflib.
            close_matches = difflib.get_close_matches(search_input, descriptions, cutoff=0.0)
            new_options = [options_dict[description] for description in close_matches]
        options_widget.children = new_options

    #search_widget.observe(on_text_change, names='value')
    return multi_select

# Example of using the widget

def enter_credentials():
    email = widgets.Text(
        value='',
        description='Email:',
        disabled=False
    )

    password = widgets.Password(description='Password:')


    def on_cred_button_clicked(change):
        # test that credentials works
        credentials = (email.value, password.value)
        test_credentials(credentials)
        this.credentials = credentials


    display(email)
    display(password)

    button = widgets.Button(description="Submit")
    display(button)

    button.on_click(on_cred_button_clicked)


def save_notebook(filename, save_as=''):

    #get home directory
    home = expanduser("~")

    #append ipynb if not there
    if '.ipynb' not in filename:
        filename += '.ipynb'

    #check outputfile name
    if save_as:
        if '.ipynb' not in filename:
            save_as += '.ipynb'
    else:
        save_as = filename

    #find notebook path
    notebook_path = ''
    for r, d, f in os.walk(home):
        for files in f:
            if files == filename:
                notebook_path = os.path.join(r, files)

    if not notebook_path:
        print("Could not find ", filename)

    # read contents
    with open(notebook_path, 'r') as content_file:
        content = content_file.read()

    #convert to .html
    subprocess.call(["jupyter", "nbconvert", notebook_path, "--to", "html"])
    html_notebook_path = os.path.dirname(notebook_path) + '/' + filename.replace('ipynb','html')

    #read contents of html
    with open(html_notebook_path, 'r') as content_file:
        htmlcontent = content_file.read()



    data = dict()
    data["notebookName"] = save_as
    data["htmlNotebookContent"] = htmlcontent
    data["notebookContent"] = content

    url = base_url + '/api/notebook/submit'
    resp = requests.post(url, data, auth=this.credentials, verify=False)
    print(resp)
    print(resp.json())




