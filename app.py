from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

app.config['MYSQL_HOST'] = '10.1.1.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'myappdb'

mysql = MySQL(app)

@app.route('/')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from user_table")
    #fetching all records from database
    data=cursor.fetchall()
    data_list_loop = []
    data_list_line = []
    data_values = []
    data_keys = ["Name", "LastName", "Role"]
    print
    print(data)
    for i in range(len(data)):
       print (data[i])
       data_list_loop = data[i]
       for j in range(len(data_list_loop)):
           data_values.append(data_list_loop[j])
#       data_values.append(data_list_line)
#       data_list_line = []
    print (data_values)
    return render_template('index.html', data_values=data_values, data_keys=data_keys)

app.run(host='0.0.0.0', port=5050)
