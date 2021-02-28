from connection import Connect
from preprocess_data import Preprocess_Data

session = Connect()
df = Preprocess_Data()


def table_1():
    query_1 = 'CREATE TABLE IF NOT EXISTS music_history'
    query_1 = query_1 + '(session_id INT,item_session INT, song_title TEXT, artist_name TEXT, song_length FLOAT, PRIMARY KEY(session_id,item_session))'
    session.execute(query_1)
    query_1 = "INSERT INTO music_history(session_id,item_session,song_title,artist_name,song_length)"
    query_1 = query_1 + 'VALUES(%s,%s,%s,%s,%s)'
    len_=len(df['artist'])
    for i in range(len_):
        session.execute(query_1,(df.iloc[i][8],df.iloc[i][3],df.iloc[i][9],df.iloc[i][0],df.iloc[i][5]))


def table_2():
    query_2 = 'CREATE TABLE IF NOT EXISTS user_choice'
    query_2 = query_2 + '(user_id INT,item_session INT, session_id INT, first_name TEXT, last_name TEXT, artist_name TEXT,song_name TEXT, PRIMARY KEY(user_id,session_id,item_session))'
    session.execute(query_2)
    query_2 = "INSERT INTO user_choice(user_id,item_session,session_id,first_name,last_name,artist_name,song_name)"
    query_2 = query_2 + 'VALUES(%s,%s,%s,%s,%s,%s,%s)'
    len_=len(df['artist'])
    for i in range(len_):
        session.execute(query_2,(df.iloc[i][10],df.iloc[i][3],df.iloc[i][8],df.iloc[i][1],df.iloc[i][4],df.iloc[i][0],df.iloc[i][9]))

def table_3():
    query_3 = 'CREATE TABLE IF NOT EXISTS music_history_app'
    query_3 = query_3 + '(session_id INT,item_session INT, song_title TEXT, artist_name TEXT, song_length FLOAT,first_name TEXT,last_name TEXT, PRIMARY KEY(song_title))'
    session.execute(query_3)
    query_3 = "INSERT INTO music_history_app(session_id,item_session,song_title,artist_name,song_length,first_name,last_name)"
    query_3 = query_3 + 'VALUES(%s,%s,%s,%s,%s,%s,%s)'
    len_=len(df['artist'])
    for i in range(len_):
        session.execute(query_3,(df.iloc[i][8],df.iloc[i][3],df.iloc[i][9],df.iloc[i][0],df.iloc[i][5],df.iloc[i][1],df.iloc[i][4]))


 