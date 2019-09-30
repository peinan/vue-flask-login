CREATE TABLE IF NOT EXISTS "authinfo"
(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(64) NOT NULL,
    password varchar(128) NOT NULL,
    jti varchar(128),
    updated_at date,
    created_at date
);
