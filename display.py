from flask import Flask, render_template
import json
import psycopg2
app = Flask(__name__)


@app.route('/')
def index():
    conn = psycopg2.connect("dbname=mariana user=postgres password=5432 ")
    cur = conn.cursor()
    cur.execute('SELECT t.titles,c.name,t.images,t.prices,t.reviews,t.stars FROM tiki as t JOIN categories as c ON t.cat_id = c.id;')
    # cur.execute('SELECT t.id,c.name,t.titles,t.prices,t.reviews,t.stars FROM tiki as t JOIN categories as c ON t.cat_id = c.id LIMIT 50;')

    products = cur.fetchall()
    

    return render_template('index.html',products=products)
    # return render_template('table.html',products=products)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 