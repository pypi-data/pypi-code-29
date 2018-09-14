#!/usr/bin/env python

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

from py4ceedlib.ttkwidgets.ttkwidgets.checkboxtreeview import *
import requests
import pandas as pd
import os
from os.path import expanduser
import subprocess
import warnings

import sys
import inspect

#base_url='http://localhost:9000'
base_url='https://4ceed.illinois.edu'

warnings.filterwarnings("once")


def test_credentials(credentials):

    url = base_url + '/api/collections'

    response = requests.get(url, auth=credentials, verify=False)
    if response.status_code == 200:
        print("Successfully validated credentials")
    else:
        raise ValueError('Invalid credentials, please try again')
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

########### Building Tree #################
def build_tree_view(credentials, show_files=False):

    ## Build Tree layout
    root = Tk()
    root.title("Select Files")
    root.geometry("800x700")
    tree = CheckboxTreeview(root, show="tree", height=200)  # , selectmode = "extended"

    style = ttk.Style()
    style.configure("Treeview", font=('Calibri', 14))

    tree.column("#0", minwidth=0, width=400, stretch=NO)
    tree["columns"] = ("one", "two")
    tree.column("one", width=200)
    tree.column("two", width=200)
    tree.heading("one", text="type")
    tree.heading("two", text="date")


    def retrieve_input():
        root.quit()
        #root.destroy()

    buttonCommit = Button(root, height=1, width=10, text="Submit",
                          command=lambda: retrieve_input())
    buttonCommit.pack()


    ## Populate the ree
    dic_for_tree = dict()

    list_spaces = get_all_spaces(credentials)
    for space in list_spaces:
        #if "GaN" in space['name']:
        create_tree_for_collection(space, "", dic_for_tree, tree, credentials, space=True, show_files=show_files)

    list_collection = get_all_collections(credentials)
    for collection in list_collection:
        create_tree_for_collection(collection, "", dic_for_tree, tree, credentials, show_files=show_files)

    tree.pack()

    root.mainloop()
    return root, tree, dic_for_tree


def create_tree_for_collection(coll, parent_coll, dic_for_tree, tree, credentials, space=False, show_files=False):

    if space:
        coll_column = tree.insert(parent_coll, 1, (coll['id']), text=coll['name'],
                                  values=('space', coll['created']))
    else:
        try:
            coll_column = tree.insert(parent_coll, 1, (coll['id']), text=coll['name'],
                                      values=('collection', coll['created']))
        except:
            print(coll['name'], ' already exists')
            return

    if parent_coll:
       current_coll_id = parent_coll + " " + coll['id']
    else:
        current_coll_id = coll['id']

    dic_for_tree[current_coll_id] = coll
    dic_for_tree[current_coll_id]['column'] = coll_column
    dic_for_tree[current_coll_id]['datasets'] = dict()

    if space:
        list_datasets = get_datasets_for_space(coll['id'], credentials)
    else:
        list_datasets = get_datasets_for_collection(coll['id'], credentials)

    for dataset in list_datasets:
        dic_for_tree[current_coll_id]['datasets'][dataset['id']] = dataset
        dic_for_tree[current_coll_id]['datasets'][dataset['id']]['files'] = dict()

        dataset_column = tree.insert(coll_column, 2, (coll['id'], dataset['id']), text=dataset['name'],
                                     values=('     dataset', dataset['created']))

        if show_files:
            list_files = get_files_for_dataset(dataset['id'], credentials)
            for file in list_files:
                # file_column = tree.insert(dataset_column, 3, file['id'], text=file['filename'], values = ( '              file', file['date-created']))
                file_column = tree.insert(dataset_column, 3, (coll['id'], dataset['id'], file['id']),
                                          text=file['filename'], values=('          file', file['date-created']))
                dic_for_tree[current_coll_id]['datasets'][dataset['id']]['files'][file['id']] = file

    #print(coll.keys())
    if space:
        space_collections = get_collections_for_space(coll['id'], credentials)
        for space_coll in space_collections:
            create_tree_for_collection(space_coll, coll_column, dic_for_tree, tree, credentials)
    else:
        child_coll_ids = coll['child_collection_ids'] #val[val.find("(")+1:val.find(")")]
        str_child_coll_ids = child_coll_ids[child_coll_ids.find("(")+1:child_coll_ids.find(")")]
        if str_child_coll_ids:
            child_coll_ids = str_child_coll_ids.split(', ')
            for child_coll_id in child_coll_ids:
                try:
                    child_coll = get_collection_by_id(child_coll_id, credentials)
                    create_tree_for_collection(child_coll, coll_column, dic_for_tree, tree, credentials)
                except: # if not authorized to see child collection of a shared collection
                    pass

def read_datasets_metadata(credentials):
    print("Retrieving datasets ... ")
    root, tree,dic_for_tree = build_tree_view(credentials, show_files=False)

    ###find checked items and put them in a dataframe
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
    meta_data_df.columns = meta_data_df.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    print("Done Retrieving ... ")

    root.destroy()
    return meta_data_df


def enter_credentials():
    master = Tk()
    master.title('Enter 4ceed Credentials')
    master.geometry("350x80")
    Label(master, text="Email").grid(row=0)
    Label(master, text="Password").grid(row=1)

    def retrieve_input():
        master.quit()
        #master.destroy()

    Button(master, height=1, width=10, text="Submit",
                          command=lambda: retrieve_input()).grid(row=3,column=2)

    email_textbox = Entry(master)
    password_textbox = Entry(master, show="*")

    email_textbox.grid(row=0, column=1)
    password_textbox.grid(row=1, column=1)

    master.mainloop()

    #test that credentials works
    credentials = (email_textbox.get(), password_textbox.get())
    test_credentials(credentials)

    master.destroy()

    return credentials

def save_notebook(credentials, filename, save_as=''):

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
    resp = requests.post(url, data, auth=credentials, verify=False)
    print(resp)
    print(resp.json())


