from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Cassandra connection details
cassandra_ip = 'your_cassandra_node_ip'
cassandra_port = 9042
cassandra_username = 'your_cassandra_username'
cassandra_password = 'your_cassandra_password'
keyspace_name = 'sparkify'  # Replace with your keyspace name

# Data type mappings (consider adjusting based on your actual data)
postgres_to_cassandra_type_map = {
    'int': 'int',
    'text': 'text',
}

# Table creation queries in CQL
create_table_queries = [
    """CREATE TABLE IF NOT EXISTS actors (
        id {} PRIMARY KEY,
        login {}
    )""".format(postgres_to_cassandra_type_map['int'], postgres_to_cassandra_type_map['text']),
    """CREATE TABLE IF NOT EXISTS events (
        id {} PRIMARY KEY,
        type {},
        actor_id {},
        repo_id {}
    )""".format(postgres_to_cassandra_type_map['text'], postgres_to_cassandra_type_map['text'],
             postgres_to_cassandra_type_map['int'], postgres_to_cassandra_type_map['int']),
    # ... other tables
]

def connect_to_cassandra():
    """Establishes a connection to the Cassandra cluster."""
    auth_provider = PlainTextAuthProvider(username=cassandra_username, password=cassandra_password)
    cluster = Cluster([cassandra_ip], port=cassandra_port, auth_provider=auth_provider)
    session = cluster.connect(keyspace_name)
    return session

def create_tables(session):
    """Creates the required tables in Cassandra."""
    for query in create_table_queries:
        session.execute(query)

def main():
    """Connects to Cassandra, creates tables, and closes the connection."""
    session = connect_to_cassandra()
    create_tables(session)
    session.cluster.shutdown()

if __name__ == '__main__':
    main()
