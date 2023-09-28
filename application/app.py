import configmodule
from mongo import Database
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(configmodule.TestingConfig())
Database("<your_mongo_db_conn_str>").initialize()


@app.route('/')
def home():
    # How to access Mongo Data
    # mongo_data = Database.find("<collection_name>")
    return render_template('home.html')


@app.route('/page-1')
def page_1():
    return render_template('page_1.html')


@app.route('/page-2')
def page_2():
    return render_template('page_2.html')


if __name__ == "__main__":
    app.run()
