import numpy as np
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

df = pd.DataFrame({'name' : ['User P', 'User Q', 'User R']})
print(df)

df.to_sql('users', con=engine)
engine.execute("SELECT * FROM users").fetchall()


df1 = pd.DataFrame({'name' : ['User S', 'User T']})
df1.to_sql('users', con=engine, if_exists='append')
engine.execute("SELECT * FROM users").fetchall()


df1.to_sql('users', con=engine, if_exists='replace',
           index_label='id')
engine.execute("SELECT * FROM users").fetchall()

df = pd.DataFrame({"X": [2, None, 3]})
print(df)


from sqlalchemy.types import Integer
df.to_sql('integers', con=engine, index=False,
          dtype={"X": Integer()})

engine.execute("SELECT * FROM integers").fetchall()


