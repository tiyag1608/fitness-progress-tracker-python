🏋️ Fitness Progress Tracking System (Python)

A command-line based fitness tracking application developed using Python, designed to
help users track workouts, monitor daily weight changes, calculate BMI, and visualize
fitness progress over time.

This project was developed as part of a B.Tech CSE (Semester I) Python Case Study and
demonstrates the practical application of core Python concepts in a real-world scenario.


📌 Project Overview

The Fitness Progress Tracking System helps users maintain fitness records in a structured,
day-wise format instead of date-wise tracking. The system minimizes repeated data entry,
stores data persistently using CSV files, and provides meaningful insights using graphs.


✨ Key Highlights

- Clean and menu-driven command line interface
- One-time user profile setup (name, height, initial weight)
- Day-based tracking system (Day 1, Day 2, Day 3...)
- Automatic BMI calculation using stored daily weight
- Graphical visualization of fitness progress
- Persistent data storage using CSV files


🚀 Features

🔹 User Profile Management
- User name and height are entered only once
- Initial weight recorded at the start of Day 1
- Prevents redundant input of static information

🔹 Day-Based Fitness Tracking
- Fitness data organized by logical days instead of dates
- User manually starts a new day
- Weight is recorded once at the start of each day

🔹 Workout Logging
- Log multiple workouts per day
- Capture workout type, duration, and calories burned
- Calories validated using Python decorators

🔹 BMI Calculation
- BMI calculated using the current day’s stored weight
- BMI category derived using a lambda function
- No repeated weight input required

🔹 Data Visualization
- Weight Progress Graph (Day vs Weight)
- Calories Burned Per Day (Bar Chart)
- Moving Average Chart for calorie trends using NumPy

🔹 Persistent Storage
- Workout and weight data stored in CSV files
- Files are auto-created and updated
- Data persists across multiple program runs


🧠 Technologies & Concepts Used

- Python (Core)
- Object-Oriented Programming (OOP)
- Decorators for validation
- Lambda Functions
- Pandas for data handling
- NumPy for numerical analysis
- Matplotlib for data visualization
- CSV File Handling


📁 Project Structure

Fitness_Progress_System/
|
|-- fitness_main.py        # Main menu-driven application
|-- fitness_user.py        # FitnessUser class & core logic
|-- fitness_utils.py       # Utilities (decorators & lambda)
|
|-- workouts.csv           # Workout logs (auto-generated)
|-- weights.csv            # Daily weight records (auto-generated)
|
|-- weight_trend.png       # Weight progress graph
|-- calories_bar.png       # Calories burned per day
|-- weekly_progress.png    # Moving average calorie graph


▶️ How to Run the Project

1️⃣ Install Required Libraries
pip install pandas matplotlib numpy

2️⃣ Run the Program
python fitness_main.py

3️⃣ Use the Menu Options to:
- Add workouts
- Start a new day
- Check BMI
- Generate progress charts


🎓 Academic Relevance

This project is ideal for B.Tech CSE Semester I students, Python case study submissions,
and beginners who want to understand real-world applications of Python, including data
persistence and visualization techniques.


📌 Future Scope

- Graphical User Interface (GUI) using Tkinter
- Weekly and monthly fitness summaries
- Export reports as PDF
- Multi-user support
- Cloud-based data storage
