from flask import Flask, render_template
from flask.ext.mysql import MySQL

app = Flask(__name__)




mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'experimentManager'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

import experimentManager.views