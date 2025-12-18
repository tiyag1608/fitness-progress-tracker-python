from datetime import datetime

class Participant:
    def __init__(self, name, age, start_date, points=0, history=None):
        self.name = name
        self.age = age
        self.start_date = start_date
        self.points = points
        self.history = history if history else []

    def update_points(self, pts):
        if pts < 0:
            raise ValueError("Points cannot be negative")
        self.points += pts
        self.history.append((datetime.now().strftime("%Y-%m-%d"), self.points))


class Leaderboard:
    def __init__(self, filename="participants.txt"):
        self.filename = filename
        self.participants = {}
        self.load_data()

    def add_participant(self, participant):
        self.participants[participant.name] = participant
        self.save_data()

    def remove_participant(self, name):
        if name in self.participants:
            del self.participants[name]
            self.save_data()

    def update_leaderboard(self):
        # Sort participants by points (high to low)
        return sorted(self.participants.values(), key=lambda p: p.points, reverse=True)

    def show_leaderboard(self):
        ranked = self.update_leaderboard()

        if not ranked:
            print("\nNo participants available.")
            return

        print("\n🏆 LEADERBOARD 🏆")
        print("-" * 52)
        print(f"{'Rank':<6}{'Name':<12}{'Age':<6}{'Points':<9}{'Badge'}")
        print("-" * 52)

        for rank, p in enumerate(ranked, start=1):
            # Rank-based badges
            if rank == 1:
                badge = "🥇 Gold"
            elif rank == 2:
                badge = "🥈 Silver"
            elif rank == 3:
                badge = "🥉 Bronze"
            else:
                badge = "-"

            print(f"{rank:<6}{p.name:<12}{p.age:<6}{p.points:<9}{badge}")

        print("-" * 52)

    def save_data(self):
        with open(self.filename, "w") as f:
            for p in self.participants.values():
                history = ";".join([f"{d},{pt}" for d, pt in p.history])
                f.write(f"{p.name}|{p.age}|{p.start_date}|{p.points}|{history}\n")

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    name, age, date, points, history = line.strip().split("|")
                    hist = []
                    if history:
                        for h in history.split(";"):
                            d, pt = h.split(",")
                            hist.append((d, int(pt)))

                    self.participants[name] = Participant(
                        name=name,
                        age=int(age),
                        start_date=date,
                        points=int(points),
                        history=hist,
                    )
        except FileNotFoundError:
            pass

# This program uses OOP and file handling to manage participants and display a ranked leaderboard with history tracking.
