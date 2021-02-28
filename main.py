from create_table import table_1,table_2,table_3
from connection import Connect
session = Connect()

print('**********Result - 1 *************')

rows=session.execute('SELECT artist_name,song_title,song_length FROM music_history WHERE session_id = 338 AND item_session = 4')
for row in rows:
    print(row)

print()

print('*************** Result - 2 *******************')
rows=session.execute('SELECT artist_name,song_name,first_name,last_name FROM user_choice WHERE user_id = 10 AND session_id = 182')
for row in rows:
    print(row)
    
print()

print('*************** Result - 3 ********************')
rows=session.execute("SELECT artist_name,song_title,song_length,first_name,last_name FROM music_history_app WHERE song_title='All Hands Against His Own'")
for row in rows:
    print(row)