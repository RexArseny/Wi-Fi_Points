DROP TABLE IF EXISTS points;

CREATE TABLE points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place TEXT NOT NULL,
    amount INTEGER NOT NULL,
    name TEXT NOT NULL,
    func TEXT NOT NULL
);
