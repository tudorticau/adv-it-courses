import pypyodbc

mySQLServer = "172.16.5.134\SQLEXPRESS"
myDatabase = "Northwind"
myUser = "dbo"
myPass = "server.2012"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';'
                              'uid=' + myUser + ';'
                              'pwd=' + myPass + ';')

