from sqlalchemy.orm import sessionmaker
# Utilizado para abstrair uma Tabela e suas Colunas
from sqlalchemy import Column, Integer, String, Float
# Utilizado para abstrair um Schema
from sqlalchemy.orm import declarative_base, mapped_column
from sqlalchemy import create_engine, URL
import psycopg2
from dotenv import load_dotenv, find_dotenv
import os


# Inicializa as variáveis de ambiente do .env
load_dotenv()

"""
Inicialmente, precisamos criar nossa engine.
Para tal, devemos fornecer uma URI contendo o
dialeto, o banco a ser utilizado e a auth.    
Por exemplo, podemos utilizar um dialeto PostgreSQL
com algum driver para se comunicar com o Postgre.
Sintaxe:
dialect+driver://username:password@host:port/database
Podemos também utilizar o URL.create para cria-la.
"""

uri = URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=os.getenv('PORT'),
    database=os.getenv('DATABASE')
)
engine = create_engine(uri)

"""
Com a engine configurada, agora podemos
criar nosso primeiro "Schema" da tabela Produtos,
utilizando o ORM do SQLAlchemy.
"""


Base = declarative_base()


class Produtos(Base):
    __tablename__ = 'dim_products'
    product_id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    product_name = mapped_column(String(50), nullable=False)
    unitary_price = mapped_column(Float())


Base.metadata.create_all(engine)

"""
Com nossa tabela criada, podemos criar
nossos primeiros registros a serem
inseridos na tabela.
"""

p1 = Produtos(
    product_name='Processor AMD Ryzen 5 5600X @ 4.2 GHz',
    unitary_price=899.90
)

p2 = Produtos(
    product_name='Processor AMD Ryzen 9 5950X @ 4.9 GHz',
    unitary_price=2799.90
)

"""
Por fim, podemos criar uma sessão que 
executará a Query abstraida e realizará
o commit no banco
"""


Session = sessionmaker(bind=engine)

try:
    with Session() as session:
        session.add(p1)
        session.add(p2)
        session.commit()

except Exception as e:
    print(e)
