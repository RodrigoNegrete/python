-- CREATE DB
sqlite3 full_stack_trading_app.db


-- CREATE TABLES
CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY,
    symbol TEXT not NULL UNIQUE,
    company TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS stock_price (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER,
    date NOT NULL,
    open NOT NULL,
    high NOT NULL,
    low NOT NULL,
    close NOT NULL,
    adjusted_close NOT NULL,
    volume NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stock (id)
);


--INSERT
-- use '' for TEXT
-- use "" for Values
INSERT INTO stock (symbol, company) VALUES ('AAPL', 'Apple');
INSERT INTO stock (symbol, company) VALUES ('MSFT', 'Microsoft');
INSERT INTO stock (symbol, company) VALUES ('TSLA', 'Tesla');
INSERT INTO stock (symbol, company) VALUES ('AMD', 'Advanced Micro Devices');

-- SELECT
SELECT * FROM stock;
SELECT id FROM stock;
SELECT id, symbol FROM stock;
SELECT company FROM stock WHERE symbol = 'TSLA';
-- get everything that starts with A
SELECT company FROM stock WHERE symbol LIKE 'A%';
-- get anything containing icro
SELECT company FROM stock WHERE company LIKE '%icro%';
-- limit number of results
SELECT * FROM stock LIMIT 3;
-- other
SELECT * FROM stock WHERE id = 2;
SELECT * FROM stock ORDER BY company DESC;
-- count
SELECT COUNT (*) FROM stock;
SELECT COUNT (*) FROM stock WHERE id = 2;

-- UPDATE
UPDATE stock SET company = 'Apple Inc.' WHERE id = 1;

-- DELETE 
DELETE FROM stock WHERE id = 3;

-- RECREATE RECORD
INSERT INTO stock (id, symbol, company) VALUES ("3", 'TSLA', 'Tesla'); 