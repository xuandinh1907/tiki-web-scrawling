import requests
import psycopg2
from bs4 import BeautifulSoup

cate_links = psycopg2.connect(" dbname=mariana user=postgres password=5432 ")
cur_1 = cate_links.cursor()
cur_1.execute('SELECT a.* FROM categories as a LEFT JOIN categories as b ON a.id = b.parent_id WHERE b.id IS NULL ORDER BY a.id;')
notes = cur_1.fetchall()

conn = psycopg2.connect(" dbname=mariana user=postgres password=5432 ")
cur = conn.cursor()




for note  in notes[450:] :
  j = 1
  BASE_URL = note[2]

  response = requests.get(BASE_URL)
  soup = BeautifulSoup(response.text)    

  product_items = soup.find_all('div', class_='product-item')
  while product_items != [] :
    titles, images, prices , reviews ,stars = [], [], [] , [] , []

    for i in range(len(product_items)):
      try:
        titles.append(product_items[i].find('p',class_='title').text.strip())
        prices.append(int(product_items[i].find('span',class_='final-price').text.strip().split()[0].replace('đ','').replace('.','')))
        images.append(product_items[i].img['src'])
        reviews.append(int(product_items[i].find('p',class_='review').text.strip('()').replace(' nhận xét','')))
      except:
        reviews.append(0)
      
      try:
        s = product_items[i].find('span',class_='rating-content').span['style'] 
        st = s.replace('width:','').replace('%','')
        stars.append(round(int(st)/100*5,1))
      except :
        stars.append(0)

    for i in range(len(titles)) :
      query = f"INSERT INTO tiki (cat_id,parent_id,titles,prices,images,reviews,stars) VALUES (%s,%s,%s,%s,%s,%s,%s);"
      val = (note[0],note[3],titles[i],prices[i],images[i],reviews[i],stars[i])
      cur.execute(query,val)
      conn.commit()
    

    j += 1
    response = requests.get(BASE_URL+"&page="+str(j))
    soup = BeautifulSoup(response.text)    

    product_items = soup.find_all('div', class_='product-item')


conn.close()