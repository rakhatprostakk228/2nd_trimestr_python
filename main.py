import psycopg2
from game_shop import GameShop
from video_game import VideoGame

def main():
    try:
        connection = psycopg2.connect(
            dbname="User",
            user="postgres",
            password="NuOchenHard",
            host="localhost",
            port="5432"
        )
        game_shop = GameShop(connection)

        while True:
            print("Choose an option:")
            print("1. Add video game")
            print("2. View all video games")
            print("3. Update video game")
            print("4. Delete video game")
            print("5. Exit")
            choice = int(input("Choose the number: "))

            if choice == 1:
                id = int(input("Enter free ID: "))
                title = input("Enter game title: ")
                genre = input("Enter game genre: ")
                release_year = int(input("Enter release year: "))
                developer = input("Enter game developer: ")
                price = int(input("Enter game price: "))
                video_game = VideoGame(id, title, genre, release_year, developer, price)
                game_shop.add_video_game(video_game, connection)
            elif choice == 2:
                game_shop.view_all_video_games()
            elif choice == 3:
                id = int(input("Enter the ID of the game to update: "))
                new_title = input("Enter new title: ")
                new_genre = input("Enter new genre: ")
                new_release_year = int(input("Enter new release year: "))
                new_developer = input("Enter new developer: ")
                new_price = int(input("Enter new price: "))
                game_shop.update_video_game(id, new_title, new_genre, new_release_year, new_developer, new_price, connection)
            elif choice == 4:
                id = int(input("Enter the ID of the game to delete: "))
                game_shop.delete_video_game(id, connection)
            elif choice == 5:
                print("Thanks for using this program!")
                break
            else:
                print("Invalid choice.")

    except psycopg2.Error as e:
        print("Error accessing database:", e)
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    main()