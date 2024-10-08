from sqlalchemy import create_engine

# Replace with your PostgreSQL connection parameters
db_user = 'myuser'
db_password = 'mypassword'
db_host = '0.0.0.0'  # or the IP address of your Docker container if remote
db_port = '5432'
db_name = 'mydatabase'
db_schema = 'raw'

# SQLAlchemy connection string for PostgreSQL
db_url = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}/{db_schema}'

# Create the SQLAlchemy engine
engine = create_engine(db_url)
