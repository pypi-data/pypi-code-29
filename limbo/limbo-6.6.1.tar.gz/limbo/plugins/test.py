
FIRST=True
def create_database(server):
    server.query('''
        CREATE TABLE IF NOT EXISTS wiw_endpoints
            (room text, url text, format text)''')
    server.query('''
        INSERT INTO wiw_endpoints(room, url, format)
        VALUES (?, ?, ?)''', 'foo', 'bar', 'asdf')
    FIRST=False

def on_message(msg, server):
    if FIRST:
        create_database(server)
    rows = server.query('''SELECT url, format FROM wiw_endpoints''')
    print(rows)
