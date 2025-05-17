CREATE TABLE predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match TEXT,
    outcomes TEXT,
    confidence INTEGER,
    key_factors TEXT,
    narrative TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);