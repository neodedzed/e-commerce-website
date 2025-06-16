CREATE TABLE user (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
address TEXT NOT NULL,
phone TEXT
);


CREATE TABLE product (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
quantity INTEGER NOT NULL
);


CREATE TABLE orders(
id INTERGER PRIMARY KEY,
user_id INTEGER,
status TEXT,
order_date TEXT,
FOREIGN KEY(user_id) REFERENCES user(id)
);


CREATE TABLE order_items(
order_id INTEGER,
product_id INTEGER,
unit_price INTEGER,
quantity INTEGER,
FOREIGN KEY (order_id) REFERENCES orders(id),
FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE payments (
id INTEGER PRIMARY KEY,
order_id INTEGER,
amount INTEGER,
status TEXT,
FOREIGN KEY (order_id) REFERENCES orders(id)
);
