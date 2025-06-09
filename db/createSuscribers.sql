
-- Query to Create suscriber Table.

CREATE TABLE IF NOT EXISTS suscribers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT (datetime('now'))
);
