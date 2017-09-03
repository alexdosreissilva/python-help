# coding=UTF-8

import os, sqlite3
from glob import glob

user_directory = os.path.expanduser('~')
files = glob(user_directory + '/.mozilla/firefox/*/places.sqlite')
if len(files) > 0:
    conn = sqlite3.connect(files[0])
    cursor = conn.execute('SELECT * FROM moz_places')

    place = cursor.fetchone()
    while place:
        print(place)
        place = cursor.fetchone()
else:
    print('Não consegui achar nenhum arquivo places.sqlite :(')
