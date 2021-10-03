import psycopg2
from psycopg2 import Error
from config import config

try:
    params = config()
    connection = psycopg2.connect(**params)

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE auditoria
          (so text,
          origem text,
          espaco_livre text,
          sensor_cpu real,
          sensor_ram real,
          pub_date character varying,
          pub_time real); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Tabela Criada com Sucesso no PostgreSQL ")

except (Exception, Error) as error:
    print("Erro ao Conectar no PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("A conexao com o PostgreSQL foi fechada")
