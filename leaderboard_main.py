from participant_class import Participant, Leaderboard
from leaderboard_utils import update_message, log_action
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


lb = Leaderboard()

# Emoji constants (just for using, logic same)
SUCCESS = "✅"
ERROR = "❌"
TROPHY = "🏆"
FIRE = "🔥"
STAR = "⭐"
HEART = "❤️"
CHART = "📊"
EXIT = "👋"


@update_message
def add_participant():
    name = input(f"{HEART} Enter Participant Name: ")
    age = int(input("Enter Age: "))
    start_date = datetime.now().strftime("%Y-%m-%d")
    p = Participant(name, age, start_date)
    lb.add_participant(p)
    log_action(f"Added participant {name}")
    print(f"{SUCCESS} Participant added successfully!")


@update_message
def update_points():
    name = input("Enter Participant Name: ")
    if name not in lb.participants:
        print(f"{ERROR} Participant not found!")
        return
    pts = int(input(f"{STAR} Enter Points Earned: "))
    lb.participants[name].update_points(pts)
    lb.save_data()
    log_action(f"Updated {name} with {pts} points")
    print(f"{SUCCESS} Points updated! Total Points: {lb.participants[name].points}")


@update_message
def remove_participant():
    name = input("Enter Participant Name to remove: ")
    lb.remove_participant(name)
    log_action(f"Removed participant {name}")
    print(f"{SUCCESS} Participant removed successfully!")


@update_message
def view_leaderboard():
    print(f"\n{TROPHY} LIVE LEADERBOARD {TROPHY}")
    lb.show_leaderboard()


def generate_charts():
    if not lb.participants:
        print(f"{ERROR} No data available")
        return

    print(f"{CHART} Generating Charts...")

    df = pd.DataFrame(
        [(p.name, p.points) for p in lb.participants.values()],
        columns=["Name", "Points"]
    )

    # ----- Bar Chart – Top 5 -----
    df_top5 = df.sort_values("Points", ascending=False).head(5)
    print("\n[DEBUG] Top 5 data:")
    print(df_top5)

    df_top5.plot(
        kind="bar", x="Name", y="Points", title=f"{TROPHY} Top 5 Participants"
    )
    plt.tight_layout()
    plt.show()

    # ----- Pie Chart – Performance Distribution -----
    bins = [0, 50, 100, 200, 1000]
    labels = ["Beginner", "Intermediate", "Advanced", "Elite"]

    df["Level"] = pd.cut(df["Points"], bins=bins, labels=labels)
    print("\n[DEBUG] Level counts:")
    print(df["Level"].value_counts())

    print("\nLevel ranges (based on Points):")
    print("0–50   → Beginner")
    print("51–100 → Intermediate")
    print("101–200 → Advanced")
    print("201+   → Elite")
    
    df["Level"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        title="Performance Distribution"
    )
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

    # ----- Line Chart – Points Trend -----
    df_line = df.sort_values("Points", ascending=False)

    df_line.plot(
        kind="line",
        x="Name",
        y="Points",
        marker="o",
        title="Points Trend by Participant"
    )
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ===== MAIN LOOP =====
while True:
    print("\n" + "="*60)
    # Show leaderboard ONLY when menu loads (not after every action)
    print(f"{TROPHY} Current Leaderboard {TROPHY}")
    lb.show_leaderboard()
    print("="*60)
    
    print(f"""
1. {HEART} Add Participant
2. {STAR} Update Points
3. 🗑️ Remove Participant
4. {TROPHY} View Leaderboard
5. {CHART} Generate Charts
6. {EXIT} Exit
    """)
    choice = input("Enter choice: ")

    if choice == "1":
        add_participant()
    elif choice == "2":
        update_points()
    elif choice == "3":
        remove_participant()
    elif choice == "4":
        view_leaderboard()
    elif choice == "5":
        generate_charts()
    elif choice == "6":
        print(f"{EXIT} Exiting Program...")
        break
    else:
        print(f"{ERROR} Invalid choice!")
    input("\nPress Enter to continue...")


# This file acts as the main controller that integrates leaderboard logic, user interaction, decorators, logging, and data visualization.