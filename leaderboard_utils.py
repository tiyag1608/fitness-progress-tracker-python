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

def get_badge_by_rank(rank): 
    if rank == 1:
        return "🥇 Gold"
    elif rank == 2:
        return "🥈 Silver"
    elif rank == 3:
        return "🥉 Bronze"
    else:
        return "-"