#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Conectando no Servidor de Banco de Dados PostgreSQL """
    conn = None
    try:
        # lendo os parametros de conexao
        params = config()

        # conectando no banco de dados
        print('Conectando no Banco de Dados PostgreSQL...')
        conn = psycopg2.connect(**params)

        # criando um cursor
        cur = conn.cursor()

        # executando uma demonstracao
        print('A versão do banco de dados é:')
        cur.execute('SELECT version()')

        # exibir a versao do servidor de banco de dados PostgreSQL
        db_version = cur.fetchone()
        print(db_version)

        # fecha a comunicacao com o PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('A conexão com o Banco de Dados PostgreSQL foi fechada.')


if __name__ == '__main__':
    connect()


