import psycopg2
from psycopg2 import sql
from video_game import VideoGame

class GameShop:
    def __init__(self, connection):
        self.connection = connection

    def add_video_game(self, video_game, connection):
        with self.connection.cursor() as cursor:
            insert_query = sql.SQL("INSERT INTO users (id, title, genre, release_year, developer, price) VALUES (%s, %s, %s, %s, %s, %s)")
            cursor.execute(insert_query, (video_game.id, video_game.title, video_game.genre, video_game.release_year, video_game.developer, video_game.price))
            print("The game has been successfully added.")
            connection.commit()

    def view_all_video_games(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()

            print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format("ID", "Title", "Genre", "Release Year", "Developer", "Price"))
            print("-----------------------------------------------------------------------------------------------------------")

            for row in rows:
                print("{:<5} {:<25} {:<20} {:<20} {:<25} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    def update_video_game(self, video_game_id, new_title, new_genre, new_release_year, new_developer, new_price, connection):
        with self.connection.cursor() as cursor:
            update_query = sql.SQL(
                "UPDATE users SET title = %s, genre = %s, release_year = %s, developer = %s, price = %s WHERE id = %s")
            cursor.execute(update_query,
                           (new_title, new_genre, new_release_year, new_developer, new_price, video_game_id))
            if cursor.rowcount == 0:
                print("No video game found with that ID.")
            else:
                print("The game has been successfully updated.")
            connection.commit()

    def delete_video_game(self, video_game_id, connection):
        with self.connection.cursor() as cursor:
            delete_query = sql.SQL("DELETE FROM users WHERE id = %s")
            cursor.execute(delete_query, (video_game_id,))
            if cursor.rowcount == 0:
                print("No video game found with that ID.")
            else:
                print("The game has been successfully deleted.")
            connection.commit()