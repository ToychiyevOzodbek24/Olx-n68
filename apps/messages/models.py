messages_query = """
                 CREATE TABLE IF NOT EXISTS messages
                 (
                     id         SERIAL PRIMARY KEY,
                     from_user  INTEGER REFERENCES users (id),
                     to_user    INTEGER REFERENCES users (id),
                     message    TEXT NOT NULL,
                     is_read    BOOLEAN   DEFAULT FALSE,
                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 ) \
                 """


