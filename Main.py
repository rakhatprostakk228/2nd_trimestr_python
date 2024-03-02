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
            print("5. Buy video game")
            print("6. Sell video game")
            print("7. Search games by genre")
            print("8. Search games by release year")
            print("9. Search games by title")
            print("10. Exit")
            choice = int(input("Choose the number: "))

            if choice == 1:
                title = input("Enter game title: ")
                genre = input("Enter game genre: ")
                release_year = int(input("Enter release year: "))
                developer = input("Enter game developer: ")
                price = int(input("Enter game price: "))

                video_game = VideoGame(None, title, genre, release_year, developer, price)
                game_shop.add_video_game(video_game)

            elif choice == 2:
                game_shop.view_all_video_games()

            elif choice == 3:
                id = int(input("Enter the ID of the game to update: "))
                update_fields = {}
                for field in ['title', 'genre', 'release_year', 'developer', 'price']:
                    value = input(f"Enter new {field}: ")
                    update_fields[field] = value
                game_shop.update_video_game(id, **update_fields)

            elif choice == 4:
                id = int(input("Enter the ID of the game to delete: "))
                game_shop.delete_video_game(id)

            elif choice == 5:
                id = int(input("Enter the ID of the game to buy: "))
                quantity = int(input("Enter the quantity to buy: "))
                game_shop.buy_game(id, quantity)

            elif choice == 6:
                id = int(input("Enter the ID of the game to sell: "))
                quantity = int(input("Enter the quantity to sell: "))
                game_shop.sell_game(id, quantity)

            elif choice == 7:
                genre = input("Enter genre to search: ")
                game_shop.search_by_genre(genre)

            elif choice == 8:
                release_year = int(input("Enter release year to search: "))
                game_shop.search_by_release_year(release_year)

            elif choice == 9:
                title = input("Enter title to search: ")
                game_shop.search_by_title(title)

            elif choice == 10:
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