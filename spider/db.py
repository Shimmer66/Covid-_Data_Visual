import pymysql

# 数据库连接


config = {
    'host': '127.0.0.1'
    , 'user': 'root'
    , 'password': ' '  #MYSQLPASSWORD
    , 'database': 'Covid'
    , 'charset': 'utf8'
    , 'port': 3306  # 注意端口为int 而不是str
}