#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Conectando no Servidor de Banco de Dados PostgreSQL """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Conectando no Banco de Dados PostgreSQL...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('A versão do banco de dados é:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('A conexão com o Banco de Dados PostgreSQL foi fechada.')


if __name__ == '__main__':
    connect()

