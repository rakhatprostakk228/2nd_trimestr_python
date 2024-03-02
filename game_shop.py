import psycopg2
from psycopg2 import sql
from video_game import VideoGame

class GameShop:
    def __init__(self, connection):
        self.connection = connection

    def add_video_game(self, video_game):
        with self.connection.cursor() as cursor:
            insert_query = sql.SQL("INSERT INTO users (title, genre, release_year, developer, price) VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(insert_query, (video_game.title, video_game.genre, video_game.release_year, video_game.developer, video_game.price))
            print("The game has been successfully added.")
            self.connection.commit()

    def view_all_video_games(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()

            print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format("ID", "Title", "Genre", "Release Year", "Developer", "Price"))
            print("-----------------------------------------------------------------------------------------------------------")

            for row in rows:
                print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    def update_video_game(self, video_game_id, **kwargs):
        with self.connection.cursor() as cursor:
            update_query = "UPDATE users SET "
            update_query += ', '.join([f"{key} = %s" for key in kwargs.keys()])
            update_query += " WHERE id = %s"
            cursor.execute(update_query, tuple(kwargs.values()) + (video_game_id,))
            if cursor.rowcount == 0:
                print("No video game found with that ID.")
            else:
                print("The game has been successfully updated.")
            self.connection.commit()

    def delete_video_game(self, video_game_id):
        with self.connection.cursor() as cursor:
            delete_query = sql.SQL("DELETE FROM users WHERE id = %s")
            cursor.execute(delete_query, (video_game_id,))
            if cursor.rowcount == 0:
                print("No video game found with that ID.")
            else:
                print("The game has been successfully deleted.")
            self.connection.commit()

    def buy_game(self, video_game_id, quantity):
        with self.connection.cursor() as cursor:
            update_query = sql.SQL(
                "UPDATE users SET quantity = quantity + %s WHERE id = %s")
            cursor.execute(update_query, (quantity, video_game_id))
            if cursor.rowcount == 0:
                print("No video game found with that ID.")
            else:
                print("Successfully bought {} copies of the game.".format(quantity))
            self.connection.commit()

    def sell_game(self, video_game_id, quantity):
        with self.connection.cursor() as cursor:
            update_query = sql.SQL(
                "UPDATE users SET quantity = quantity - %s WHERE id = %s")
            cursor.execute(update_query, (quantity, video_game_id))
            if cursor.rowcount == 0:
                print("No video game found with that ID.")
            else:
                print("Successfully sold {} copies of the game.".format(quantity))
            self.connection.commit()

    def search_by_genre(self, genre):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE genre = %s", (genre,))
            rows = cursor.fetchall()

            if not rows:
                print("No games found for the given genre.")
                return

            print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format("ID", "Title", "Genre", "Release Year", "Developer", "Price"))
            print("-----------------------------------------------------------------------------------------------------------")

            for row in rows:
                print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    def search_by_release_year(self, release_year):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE release_year = %s", (release_year,))
            rows = cursor.fetchall()

            if not rows:
                print("No games found for the given release year.")
                return

            print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format("ID", "Title", "Genre", "Release Year", "Developer", "Price"))
            print("-----------------------------------------------------------------------------------------------------------")

            for row in rows:
                print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    def search_by_title(self, title):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE title ILIKE %s", ('%' + title + '%',))
            rows = cursor.fetchall()

            if not rows:
                print("No games found for the given title.")
                return

            print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format("ID", "Title", "Genre", "Release Year", "Developer", "Price"))
            print("-----------------------------------------------------------------------------------------------------------")

            for row in rows:
                print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))