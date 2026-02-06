import sqlite3
import sys

def main():
    conn = sqlite3.connect('meal_planner', isolation_level=None)
    cursor = conn.cursor()

    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT')
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (name TEXT,
                meal_id INTEGER,
                FOREIGN KEY(meal_id) REFERENCES meals
                (rowid)
            ) STRICT
        """)
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}")
        return

    print("Meal Ingredients Database")
    print("Enter 'quit' to exit.")
    print("Add a meal: 'Meal Name:ingredient1,ingredient2")
    print("Search: Enter a meal name or ingredient name.")

    while True:
        try:
            user_input = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            break

        if user_input.lower() == 'quit':
            break

        if not user_input:
            continue

        # adding a meal
        if ':' in user_input:
            try:
                meal_name, ingredients_str = user_input.split(':', 1)
                meal_name = meal_name.strip()

                if not meal_name:
                    print('Error: Meal name cannot be empty.')
                    continue

                ingredients_lst = [
                    i.strip() for i in ingredients_str.split(',') if i.strip()
                ]

                cursor.execute("INSERT INTO meals (name) VALUES (?)", (meal_name,))
                meal_id = cursor.lastrowid

                for ingredient in ingredients_lst:
                    cursor.execute(
                    "INSERT INTO ingredients (name, meal_id) VALUES (?,?)",
                    (ingredient, meal_id)
                )
                print(f"Meal added: {meal_name}")

            except ValueError:
                print("Error: Invalid format. Use 'Meal: item1, item2'")

        # searching
        else:
            search_term = user_input
            found = False

            cursor.execute("SELECT rowid FROM meals WHERE name = ?", (search_term,))
            meal_row = cursor.fetchone()

            if meal_row:
                found = True
                target_id = meal_row[0]
                print(f"Ingredients of {search_term}:")

                cursor.execute("SELECT name FROM ingredients WHERE meal_id = ?",(target_id,))
                results = cursor.fetchall()

                for row in results:
                    print(f" {row[0]}")

            cursor.execute(
                """
                SELECT meals.name
                FROM meals
                JOIN ingredients ON meals.rowid = ingredients.meal_id
                WHERE ingredients.name = ?
                """,
                (search_term,),
            )

            ingredient_matches = cursor.fetchall()

            if ingredient_matches:
                found = True
                print(f"Meals that use {search_term}:")

                for row in ingredient_matches:
                    print(f" {row[0]}")

            if not found:
                print(f"No meals or ingredients found matching '{search_term}'.")

    conn.close()

if __name__ == '__main__':
    main()
