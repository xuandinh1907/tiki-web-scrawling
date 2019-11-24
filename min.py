import psycopg2
cate_links = psycopg2.connect(" dbname=mariana user=postgres password=5432 ")
cur_1 = cate_links.cursor()
cur_1.execute('SELECT t.titles,c.name,t.images,t.prices,t.reviews,t.stars FROM tiki as t JOIN categories as c ON t.cat_id = c.id;' )
notes = cur_1.fetchall()
# print(notes)
print(len(notes))