import sqlite3
import datetime
import matplotlib.pyplot as plt

# Database setup
def init_db():
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at DATE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            log_date DATE,
            FOREIGN KEY(habit_id) REFERENCES habits(id)
        )
    ''')
    conn.commit()
    conn.close()

# Add a new habit
def add_habit(name):
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO habits (name, created_at) VALUES (?, ?)", (name, datetime.date.today()))
    conn.commit()
    conn.close()
    print(f"Habit '{name}' added successfully!")

# Log habit completion
def log_habit(habit_id):
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()
    today = datetime.date.today()
    cursor.execute("INSERT INTO habit_logs (habit_id, log_date) VALUES (?, ?)", (habit_id, today))
    conn.commit()
    conn.close()
    print(f"Habit {habit_id} logged for today!")

# Get all habits
def get_habits():
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()
    conn.close()
    return habits

# Get habit logs
def get_habit_logs(habit_id):
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()
    cursor.execute("SELECT log_date FROM habit_logs WHERE habit_id = ?", (habit_id,))
    logs = cursor.fetchall()
    conn.close()
    return [log[0] for log in logs]

# Streak tracking
def calculate_streak(habit_id):
    logs = get_habit_logs(habit_id)
    logs = sorted([datetime.datetime.strptime(log, "%Y-%m-%d").date() for log in logs])
    
    streak = 0
    if logs:
        today = datetime.date.today()
        if logs[-1] == today:
            streak = 1
            for i in range(len(logs) - 1, 0, -1):
                if logs[i] - logs[i-1] == datetime.timedelta(days=1):
                    streak += 1
                else:
                    break
    
    return streak

# Visualize habit progress
def visualize_habit_progress(habit_id):
    logs = get_habit_logs(habit_id)
    if not logs:
        print("No logs available for this habit.")
        return
    
    dates = sorted([datetime.datetime.strptime(log, "%Y-%m-%d").date() for log in logs])
    plt.plot(dates, list(range(1, len(dates) + 1)), marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel("Days Tracked")
    plt.title("Habit Progress")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Main menu
def main():
    init_db()
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Log Habit")
        print("3. View Habits")
        print("4. View Habit Streak")
        print("5. Visualize Progress")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter habit name: ")
            add_habit(name)
        elif choice == '2':
            habits = get_habits()
            for habit in habits:
                print(f"{habit[0]}: {habit[1]}")
            habit_id = int(input("Enter habit ID to log: "))
            log_habit(habit_id)
        elif choice == '3':
            habits = get_habits()
            for habit in habits:
                print(f"{habit[0]}: {habit[1]}")
        elif choice == '4':
            habits = get_habits()
            for habit in habits:
                print(f"{habit[0]}: {habit[1]}")
            habit_id = int(input("Enter habit ID to check streak: "))
            streak = calculate_streak(habit_id)
            print(f"Current streak: {streak} days")
        elif choice == '5':
            habits = get_habits()
            for habit in habits:
                print(f"{habit[0]}: {habit[1]}")
            habit_id = int(input("Enter habit ID to visualize: "))
            visualize_habit_progress(habit_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()