from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pymicroconnectors.config as config

service = None



def authentication():
    global service
    if service is None:
        store = file.Storage(config.get_value('sheet.auth.token'))
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(config.get_value('sheet.auth.credentials'), config.get_value('sheet.auth.scope'))
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))


def load_data(sheet_id, range) -> list:
    # Call the Sheets API
    authentication()

    result = service.spreadsheets().values().get(spreadsheetId=sheet_id,
                                                 range=range).execute()
    return result.get('values', [])


def write_data(sheet_id, range, data, value_input_option='RAW') -> list:

    authentication()

    body = {
        'values': data
    }

    service.spreadsheets().values().clear(
        spreadsheetId=sheet_id,
        range=range
    )

    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=range,
        valueInputOption=value_input_option,
        body=body
    ).execute()

    return load_data(sheet_id, range)

def init():
    authentication()