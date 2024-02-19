from sqlalchemy import create_engine

# Create an engine to connect to the PostgreSQL database
db = create_engine("postgresql:///chinook")

# Define the SQL query to check primary key constraints
query = (
    "SELECT constraint_name, column_name, constraint_type "
    "FROM information_schema.table_constraints tc "
    "JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) "
    "WHERE tc.table_name = 'artist' AND tc.table_schema = 'public';"
)

# Establish a connection and execute the query
with db.connect() as connection:
    result = connection.execute(query)

    # Fetch and print the retrieved rows
    for row in result:
        print(row)
