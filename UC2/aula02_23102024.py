#pip install sqlalchemy pymysql(instalar)
#
#(código no arquivo .py)
#
from sqlalchemy import create_engine
import pandas as pd

host='localhost'

user='root'

password='senac%40123'

database='mulherestech'

engine=create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df=pd.read_sql('alunos',con=engine)
print(df)