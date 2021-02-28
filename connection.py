import cassandra
from cassandra.cluster import Cluster

def Connect():
    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
        session.execute('''CREATE KEYSPACE IF NOT EXISTS sparkifydb 
            WITH REPLICATION = {'class':'SimpleStrategy','replication_factor':1}''')
        session.set_keyspace('sparkifydb')
        return session
    except Exception as e:
        print(f'Error from connection: {e} ')

