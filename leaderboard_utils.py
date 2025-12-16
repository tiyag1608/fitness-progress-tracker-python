from datetime import datetime

def update_message(func):
    def wrapper(*args, **kwargs):
        print("\nUpdating Leaderboard...")
        return func(*args, **kwargs)
    return wrapper


def log_action(message, logfile="leaderboard_log.txt"):
    with open(logfile, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")


# Lambda utilities
top_performers = lambda participants, n=5: sorted(
    participants, key=lambda p: p.points, reverse=True
)[:n]

# Auto badge system based on points
def get_badge(points):
    if points >= 61:
        return "🥇 Gold"
    elif points >= 41:
        return "🥈 Silver"
    elif points >= 26:
        return "🥉 Bronze"
    else:
        return "-"
