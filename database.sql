CREATE TABLE IF NOT EXISTS customer (
  customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  address_line1 VARCHAR(255) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(2) NOT NULL,
  postal_code VARCHAR(10) NOT NULL,
  country VARCHAR(50) NOT NULL
--   UNIQUE (address_line1, city, state, postal_code, country)
);


CREATE TABLE IF NOT EXISTS customer_contact (
  customer_id INT NOT NULL ,
  phone_number VARCHAR(15),
  email VARCHAR(30),
  PRIMARY KEY(customer_id, phone_number),
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
  UNIQUE(customer_id, email)
);


CREATE TABLE IF NOT EXISTS distributor(
    distributor_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  address_line1 VARCHAR(255) NOT NULL UNIQUE,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(2) NOT NULL,
  postal_code VARCHAR(10) NOT NULL,
  country VARCHAR(50) NOT NULL,
  UNIQUE (address_line1, city, state, postal_code, country)
);



CREATE TABLE IF NOT EXISTS distributor_contact (
  distributor_id INT NOT NULL,
  phone_number VARCHAR(15) UNIQUE,
  email VARCHAR(30) UNIQUE,
  PRIMARY KEY (distributor_id,phone_number),
  FOREIGN KEY (distributor_id) REFERENCES distributor(distributor_id) ON DELETE CASCADE,
  UNIQUE(distributor_id,email)
);


INSERT INTO customer (name, address_line1, city, state, postal_code, country) VALUES
('John Doe', '123 Main St.', 'Anytown', 'CA', '12345', 'USA'),
('Jane Smith', '456 Maple Ave.', 'Springfield', 'MA', '67890', 'USA'),
('Michael Brown', '789 Elm St.', 'Metropolis', 'NY', '09876', 'USA'),
('Emily Jones', '1011 Oak Blvd.', 'Hometown', 'TX', '23456', 'USA'),
('David Miller', '1213 Pine Dr.', 'Sunnyville', 'FL', '56789', 'USA'),
('Sarah Anderson', '1415 Elm St.', 'Suburbia', 'IL', '45678', 'USA'),
('William Davis', '1617 Cherry Ave.', 'Rustbelt', 'OH', '34567', 'USA'),
('Elizabeth Wilson', '1819 Walnut St.', 'Boomtown', 'AZ', '21345', 'USA'),
('Richard Wright', '2021 Birch Ln.', 'Quietville', 'MN', '09873', 'USA'),
('Jennifer Garcia', '2223 Spruce Ct.', 'Hustletown', 'NV', '12340', 'USA');





INSERT INTO customer_contact (phone_number, email, customer_id) VALUES
('555-123-4567', 'john.doe@example.com', 1),
('555-555-5555', 'jane.smith@example.com', 2),
('555-345-6789', 'alice.johnson@example.com', 3),
('555-234-5678', 'michael.brown@example.com', 4),
('555-987-6543', 'emily.clark@example.com', 5),
('555-123-1234', 'david.walker@example.com', 6),
('555-789-0123', 'sarah.williams@example.com', 7),
('555-456-7890', 'richard.miller@example.com', 8),
('555-098-7654', 'jennifer.davis@example.com', 9),
('555-678-5432', 'charles.taylor@example.com', 10);



Select * from customer_contact;
SELECT * from customer;


-- Inserting data into distributor table
INSERT IGNORE INTO distributor (name, address_line1, city, state, postal_code, country) VALUES
('ABC Distributors', '123 Main Street', 'Cityville', 'CA', '12345', 'USA'),
('XYZ Wholesalers', '456 Elm Avenue', 'Townsville', 'NY', '54321', 'USA'),
('Global Imports Inc.', '789 Oak Lane', 'Villageton', 'TX', '67890', 'USA'),
('Sunrise Distributing', '101 Pine Road', 'Ruralville', 'CA', '11111', 'USA'),
('Moonlight Trading', '202 Cedar Street', 'Suburbia', 'NY', '22222', 'USA'),
('Star Distributors', '303 Maple Drive', 'Metropolis', 'TX', '33333', 'USA'),
('Ocean Distributors', '404 Ocean Avenue', 'Coastal City', 'CA', '44444', 'USA'),
('Mountain Suppliers', '505 Hillside Boulevard', 'Peakville', 'NY', '55555', 'USA'),
('Valley Distributors', '606 Valley Road', 'Lowland', 'TX', '66666', 'USA'),
('City Distributing Co.', '707 Broadway', 'Urbania', 'CA', '77777', 'USA');


-- Inserting data into distributor_contact table
INSERT IGNORE INTO distributor_contact (distributor_id, phone_number, email) VALUES
(1, '123-456-7890', 'abc@example.com'),
(2, '234-567-8901', 'xyz@example.com'),
(3, '345-678-9012', 'global@example.com'),
(4, '456-789-0123', 'sunrise@example.com'),
(5, '567-890-1234', 'moonlight@example.com'),
(6, '678-901-2345', 'star@example.com'),
(7, '789-012-3456', 'ocean@example.com'),
(8, '890-123-4567', 'mountain@example.com'),
(9, '901-234-5678', 'valley@example.com'),
(10, '012-345-6789', 'city@example.com');

SELECT * FROM distributor;
SELECT * FROM distributor_contact;



CREATE TABLE IF NOT EXISTS product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    distributor_id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    description VARCHAR(100),
    quantity INT NOT NULL,
    price INT NOT NULL,
    Category VARCHAR(20) NOT NULL,
    FOREIGN KEY (distributor_id) REFERENCES distributor(distributor_id) ON DELETE CASCADE
);

INSERT INTO product (distributor_id, name, description, quantity, price, Category)VALUES
(1, 'Product 1', 'Description for Product 1', 100, 50, 'Category 1'),
(1, 'Product 2', 'Description for Product 2', 80, 70, 'Category 2'),
(2, 'Product 3', 'Description for Product 3', 120, 40, 'Category 1'),
(2, 'Product 4', 'Description for Product 4', 90, 60, 'Category 3'),
(3, 'Product 5', 'Description for Product 5', 110, 55, 'Category 2'),
(3, 'Product 6', 'Description for Product 6', 95, 65, 'Category 1'),
(4, 'Product 7', 'Description for Product 7', 105, 45, 'Category 3'),
(4, 'Product 8', 'Description for Product 8', 85, 75, 'Category 2'),
(5, 'Product 9', 'Description for Product 9', 125, 35, 'Category 1'),
(5, 'Product 10', 'Description for Product 10', 100, 50, 'Category 3');

SELECT * from product;

CREATE TABLE IF NOT EXISTS Feedback (
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    review TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    PRIMARY KEY(product_id,customer_id)    
);

INSERT INTO Feedback (product_id, customer_id, review) VALUES
(1, 1, 'Great product! Highly recommended.'), -- John Doe reviews Product 1
(2, 2, 'Excellent quality. Will buy again.'), -- Jane Smith reviews Product 2
(3, 3, 'Impressed with the functionality.'), -- Michael Brown reviews Product 3
(4, 4, 'Good value for money.'), -- Emily Jones reviews Product 4
(5, 5, 'Fast shipping. Very satisfied.'), -- David Miller reviews Product 5
(6, 6, 'Beautiful design. Love it!'), -- Sarah Anderson reviews Product 6
(7, 7, 'Works perfectly. Exactly as described.'), -- William Davis reviews Product 7
(8, 8, 'Great customer service. Happy with the purchase.'), -- Elizabeth Wilson reviews Product 8
(9, 9, 'Highly impressed with the quality.'), -- Richard Wright reviews Product 9
(10, 10, 'Exactly what I needed. Thank you!'); -- Jennifer Garcia reviews Product 10

SELECT * from Feedback;



-- Step 4: Create Weak Entity Set - Cart
CREATE TABLE IF NOT EXISTS cart (
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    distributor_id INT NOT NULL,
    INDEX cart_idx (product_id, customer_id, distributor_id), -- Define the index on the referenced columns
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (distributor_id) REFERENCES product(distributor_id),
    PRIMARY KEY(customer_id,product_id)
);


-- Inserting data into Cart table
INSERT INTO cart (customer_id, product_id, quantity, distributor_id)
VALUES
    (1, 1, 2, 1), -- John Doe adds 2 quantity of Product 1 from Distributor 1 to the cart
    (2, 2, 1, 1), -- Jane Smith adds 1 quantity of Product 3 from Distributor 2 to the cart
    (3, 3, 3, 2), -- Michael Brown adds 3 quantity of Product 5 from Distributor 3 to the cart
    (4, 4, 2, 2), -- Emily Jones adds 2 quantity of Product 7 from Distributor 4 to the cart
    (5, 5, 1, 3), -- David Miller adds 1 quantity of Product 9 from Distributor 5 to the cart
    (6, 6, 2, 3), -- Sarah Anderson adds 2 quantity of Product 2 from Distributor 6 to the cart
    (7, 7, 1, 4), -- William Davis adds 1 quantity of Product 4 from Distributor 7 to the cart
    (8, 8, 3, 4), -- Elizabeth Wilson adds 3 quantity of Product 6 from Distributor 8 to the cart
    (9, 9, 2, 5), -- Richard Wright adds 2 quantity of Product 8 from Distributor 9 to the cart
    (10, 10, 1, 5); -- Jennifer Garcia adds 1 quantity of Product 10 from Distributor 10 to the cart

SELECT * from cart;


CREATE TABLE IF NOT EXISTS inventory (
    distributor_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (distributor_id, product_id) REFERENCES product(distributor_id, product_id) ON DELETE CASCADE,
    PRIMARY KEY(distributor_id,product_id)
);

INSERT INTO inventory (distributor_id, product_id, quantity)
SELECT distributor_id, product_id, quantity FROM product;


SELECT * from inventory;


CREATE TABLE IF NOT EXISTS transaction (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    distributor_id INT NOT NULL,
    quantity INT NOT NULL,
    INDEX customer_history_idx (transaction_id,product_id, customer_id),
    INDEX distributor_history_idx (transaction_id,product_id, distributor_id),
    date_added DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id, customer_id, distributor_id) REFERENCES cart (product_id, customer_id, distributor_id) ON DELETE CASCADE,
    UNIQUE(transaction_id,product_id,customer_id,distributor_id)

    -- INDEX cart_idx (product_id, customer_id, distributor_id) -- Adding this index definition to explicitly use the existing composite index
);


INSERT INTO transaction (customer_id, product_id, quantity, distributor_id) VALUES
(1, 1, 2, 1), -- John Doe adds 2 quantity of Product 1 from Distributor 1 to the cart
(2, 2, 1, 1), -- Jane Smith adds 1 quantity of Product 3 from Distributor 2 to the cart
(3, 3, 3, 2), -- Michael Brown adds 3 quantity of Product 5 from Distributor 3 to the cart
(4, 4, 2, 2), -- Emily Jones adds 2 quantity of Product 7 from Distributor 4 to the cart
(5, 5, 1, 3), -- David Miller adds 1 quantity of Product 9 from Distributor 5 to the cart
(6, 6, 2, 3), -- Sarah Anderson adds 2 quantity of Product 2 from Distributor 6 to the cart
(7, 7, 1, 4), -- William Davis adds 1 quantity of Product 4 from Distributor 7 to the cart
(8, 8, 3, 4), -- Elizabeth Wilson adds 3 quantity of Product 6 from Distributor 8 to the cart
(9, 9, 2, 5), -- Richard Wright adds 2 quantity of Product 8 from Distributor 9 to the cart
(10, 10, 1, 5); -- Jennifer Garcia adds 1 quantity of Product 10 from Distributor 10 to the cart


SELECT * from transaction;



CREATE TABLE IF NOT EXISTS customer_history(
    transaction_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY (transaction_id, product_id, customer_id) REFERENCES transaction(transaction_id,product_id,customer_id),
    PRIMARY KEY(transaction_id,product_id,customer_id)
);

INSERT INTO customer_history (customer_id, product_id, quantity, transaction_id) VALUES
(1, 1, 2,1), -- John Doe adds 2 quantity of Product 1 from Distributor 1 to the cart
(2, 2, 1,2), -- Jane Smith adds 1 quantity of Product 3 from Distributor 2 to the cart
(3, 3, 3,3), -- Michael Brown adds 3 quantity of Product 5 from Distributor 3 to the cart
(4, 4, 2,4), -- Emily Jones adds 2 quantity of Product 7 from Distributor 4 to the cart
(5, 5, 1,5), -- David Miller adds 1 quantity of Product 9 from Distributor 5 to the cart
(6, 6, 2,6), -- Sarah Anderson adds 2 quantity of Product 2 from Distributor 6 to the cart
(7, 7, 1,7), -- William Davis adds 1 quantity of Product 4 from Distributor 7 to the cart
(8, 8, 3,8), -- Elizabeth Wilson adds 3 quantity of Product 6 from Distributor 8 to the cart
(9, 9, 2,9), -- Richard Wright adds 2 quantity of Product 8 from Distributor 9 to the cart
(10, 10, 1,10);

SELECT * FROM customer_history;

CREATE TABLE IF NOT EXISTS distributor_history(
    transaction_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    distributor_id INT NOT NULL,
    FOREIGN KEY (transaction_id, product_id, distributor_id) REFERENCES transaction(transaction_id,product_id,distributor_id),
    PRIMARY KEY(transaction_id,product_id,distributor_id)
);

INSERT INTO distributor_history (distributor_id, product_id, quantity, transaction_id) VALUES
(1, 1, 2,1), -- John Doe adds 2 quantity of Product 1 from Distributor 1 to the cart
(1, 2, 1,2), -- Jane Smith adds 1 quantity of Product 3 from Distributor 2 to the cart
(2, 3, 3,3), -- Michael Brown adds 3 quantity of Product 5 from Distributor 3 to the cart
(2, 4, 2,4), -- Emily Jones adds 2 quantity of Product 7 from Distributor 4 to the cart
(3, 5, 1,5), -- David Miller adds 1 quantity of Product 9 from Distributor 5 to the cart
(3, 6, 2,6), -- Sarah Anderson adds 2 quantity of Product 2 from Distributor 6 to the cart
(4, 7, 1,7), -- William Davis adds 1 quantity of Product 4 from Distributor 7 to the cart
(4, 8, 3,8), -- Elizabeth Wilson adds 3 quantity of Product 6 from Distributor 8 to the cart
(5, 9, 2,9), -- Richard Wright adds 2 quantity of Product 8 from Distributor 9 to the cart
(5, 10, 1,10);

SELECT * FROM distributor_history;


-- 1. Retrieve the names of customers who have purchased products with a price higher than $60
SELECT c.name
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM transaction t
    JOIN product p ON t.product_id = p.product_id
    WHERE t.customer_id = c.customer_id
    AND p.price > 60
);


-- 2. Retrieve the names and addresses of distributors who have sold more than 3 products in total
SELECT d.name, d.address_line1, d.city, d.state, d.postal_code, d.country
FROM distributor d
JOIN (
    SELECT distributor_id, SUM(quantity) AS total_sold
    FROM transaction
    GROUP BY distributor_id
    HAVING total_sold > 3
) AS t ON d.distributor_id = t.distributor_id;



-- 3. Product with highest number of sales
SELECT p.name AS product_name, SUM(t.quantity) AS total_sales
FROM product p
JOIN transaction t ON p.product_id = t.product_id
GROUP BY p.product_id
ORDER BY total_sales DESC
LIMIT 1;


-- 4. Distributor with highest number of sales
SELECT d.name AS distributor_name, SUM(t.quantity) AS total_sales
FROM distributor d
JOIN transaction t ON d.distributor_id = t.distributor_id
GROUP BY d.distributor_id
ORDER BY total_sales DESC
LIMIT 1;


-- 5. Distributor with maximum stock
SELECT d.name AS distributor_name, SUM(i.quantity) AS total_stock
FROM distributor d
JOIN inventory i ON d.distributor_id = i.distributor_id
GROUP BY d.distributor_id
ORDER BY total_stock DESC
LIMIT 1;

-- 6. Reading feedback
SELECT f.*, p.name as product_name
FROM Feedback f
JOIN Product p ON f.product_id = p.product_id
WHERE p.distributor_id = 1;

-- 7. Retrieve the names and email addresses of customers who have purchased products from distributors in New York (NY)
SELECT c.name, cc.email
FROM customer c
JOIN customer_contact cc ON c.customer_id = cc.customer_id
WHERE EXISTS (
    SELECT 1
    FROM transaction t
    JOIN distributor d ON t.distributor_id = d.distributor_id
    WHERE t.customer_id = c.customer_id
    AND d.state = 'NY'
);


-- 8. Retreiving data from Product Table where Distributor_id matches the required distributor
-- then 
-- Updating product data of selected product which belongs to 1 distributor
SELECT product_id, name, description, quantity, price, Category
FROM product
WHERE distributor_id = 1;

UPDATE product
SET 
    price = 75
WHERE
    product_id = 1
    AND distributor_id = 1;

SELECT * FROM product;


-- 9. Calculate total sales for products by Category
SELECT SUM(t.quantity) AS total_sales
FROM Transaction t
JOIN Product p ON t.product_id = p.product_id
WHERE p.Category = 'Category 1';



-- 10. Retrieve the names and quantities of products purchased by customers who live in Texas (TX)
SELECT p.name, t.quantity
FROM product p
JOIN transaction t ON p.product_id = t.product_id
JOIN customer c ON t.customer_id = c.customer_id
WHERE c.state = 'TX';






-- DROP TABLE distributor_history;
-- DROP TABLE customer_history;
-- DROP TABLE transaction;
-- DROP TABLE cart;
-- DROP TABLE Feedback;
-- DROP TABLE inventory;
-- DROP TABLE product;
-- DROP TABLE customer_contact;
-- DROP TABLE customer;
-- DROP TABLE distributor_contact;
-- DROP TABLE distributor;



