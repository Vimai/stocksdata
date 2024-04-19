CREATE DATABASE local_db
    WITH
    OWNER = postgres;

\connect local_db;

CREATE SCHEMA stocksdata;

CREATE TABLE stocksdata.stocks (
    id SERIAL PRIMARY KEY,
    status VARCHAR(255),
    "from" DATE,
    symbol VARCHAR(255),
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume INTEGER,
    amount INTEGER,
    afterHours FLOAT,
    preMarket FLOAT,
    performance JSONB
);

INSERT INTO stocksdata.stocks
    (status, "from", symbol, open, high, low, close, volume, amount, afterHours, preMarket, performance)
VALUES
    (
    'OK',
    '2023-01-09',
    'AAPL',
    130.465,
    133.41,
    129.89,
    130.15,
    70790813,
    100,
    129.85,
    129.6,
    '{"growth": 5.5, "period": "1 year"}'
    );
