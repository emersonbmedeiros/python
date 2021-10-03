import psycopg2
from psycopg2 import Error
from config import config

try:
    # busca a conexao com o banco de dados postgres
    params = config()
    connection = psycopg2.connect(**params)

    cursor = connection.cursor()
    # sql responsavel por criar a tabela
    create_table_query = '''CREATE TABLE auditoria
          (so text,
          origem text,
          espaco_livre text,
          sensor_cpu real,
          sensor_ram real,
          pub_date character varying,
          pub_time real); '''
    # executa o comando para criar a nova tabela
    cursor.execute(create_table_query)
    connection.commit()
    print("Tabela Criada com Sucesso no PostgreSQL ")
    # retorna erro em caso de problemas de conexao
except (Exception, Error) as error:
    print("Erro ao Conectar no PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("A conexao com o PostgreSQL foi fechada")
