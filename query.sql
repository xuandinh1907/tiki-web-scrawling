SELECT COUNT(DISTINCT cat_id),COUNT(id) FROM tiki;
SELECT * FROM CATEGORIES WHERE PARENT_ID = 21 ;
SELECT * FROM TIKI ORDER BY ID DESC;

CREATE TABLE tiki (
    id SERIAL PRIMARY KEY,
    cat_id INT,
    parent_id INT,
    titles TEXT,
    prices INT,
    images TEXT,
    reviews INT,
    stars INT
);

SELECT a.* FROM categories as a LEFT JOIN categories as b ON a.id = b.parent_id WHERE b.id IS NULL ORDER BY a.id LIMIT 5 OFFSET 10;

SELECT * FROM tiki WHERE cat_id = 1;

SELECT t.titles,c.name,t.images,t.prices,t.reviews,t.stars FROM tiki as t JOIN categories as c ON t.cat_id = c.id;
