import mysql.connector

con = mysql.connector.connect(host='localhost', database="dados", user='root', password='')

if con.is_connected():
    dados_info = con.get_server_info()
    print('Conectado ao servidor')
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao Banco de Dados {}', linha)
if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão encerrada!')
