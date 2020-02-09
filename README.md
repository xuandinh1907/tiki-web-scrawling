# Tiki Web scraping
---
## Introduction : we scrawl data of all products , save them in our database and then reload onto our table - form tiki version
---
### Firstly we have to scrawl all sub - categorie links

### Secondly we need to qualify minimum sub - categories (that mean they don't have child categorie any more)

- **The idea is we join categories table with itself where parent_id match with cat_id.To implement this, we use sql command**
 
 *SELECT a.* FROM categories as a LEFT JOIN categories as b ON a.id = b.parent_id WHERE b.id IS NULL ;

- **After we have result arrar, we move to next step**

### Thirdly we scrawl all data and save them in database
- **The idea is for every min - categorie we scrawl all pages.**
- **To execute this,we put a while_loop with condition produtc_items != [].To activate we put product_items =[page_1].Right after while_loop,we put empty lists like titles,prices,images,reviews,stars.This makes sure we just insert new page data.Right before end loop , we increase page by 1 unit to prepare for next loop **

    *product_items = [page_1_data]
    
    *while product_items != [] :
    
    *titles, images, prices , reviews ,stars = [], [], [] , [] , []
    
    *scrawling main part*
    
    *Insert into database*
    
    *increase page number*
    
- **But the milestone here is the way we track process.We continue sql command to track in pg webpage.We usually refresh page and watch if distinct_cat_id number and id number really go up**

 *SELECT COUNT(DISTINCT cat_id),COUNT(id) FROM tiki ;

### Finally we reload from database and display in table - form 
