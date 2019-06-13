from sqlalchemy import create_engine

uri = 'clickhouse://default:password@hello.ai:23723'

engine = create_engine(uri)
df = pd.read_sql(query, engine)
