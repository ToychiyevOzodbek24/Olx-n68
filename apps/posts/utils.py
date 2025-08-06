import psycopg2
from core.config import DB_NAME, DB_USER, DB_PASS, DB_HOST


class PostQueries:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST
        )
        self.cursor = self.conn.cursor()

    def get_all_posts(self):
        self.cursor.execute("SELECT id, title, description, price, is_active FROM posts ORDER BY created_at DESC")
        rows = self.cursor.fetchall()
        return [{"id": r[0], "title": r[1], "description": r[2], "price": r[3], "is_active": r[4]} for r in rows]

    def insert_post(self, title, description, price):
        try:
            self.cursor.execute(
                "INSERT INTO posts (title, description, price) VALUES (%s, %s, %s)",
                (title, description, price)
            )
            self.conn.commit()
            return True
        except:
            self.conn.rollback()
            return False

    def delete_post_by_id(self, post_id):
        self.cursor.execute("DELETE FROM posts WHERE id = %s", (post_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def update_post_by_id(self, post_id, title, description, price, is_active):
        self.cursor.execute("""
            UPDATE posts
            SET title = %s,
                description = %s,
                price = %s,
                is_active = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """, (title, description, price, is_active, post_id))
        self.conn.commit()
        return self.cursor.rowcount > 0
