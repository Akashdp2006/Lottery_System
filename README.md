#LuckyDraw Lottery

About the Project

LuckyDraw Lottery is a simple lottery management program made using Python. The main purpose of this project is to understand how basic Python concepts can be used to create a small real-life application.

In this program, users can register themselves, buy lottery tickets, conduct a lottery draw, and check the results.

The project mainly uses basic Python concepts like variables, lists, dictionaries, functions, loops, conditions, user input, and random number generation.

🎯 Features

1. Register Player

A user can register by entering their name. After registration, the program automatically gives them a unique Player ID.

2. Buy Lottery Ticket

Registered players can buy a lottery ticket. Each ticket contains 6 different random numbers between 1 and 50.

3. Conduct Lottery Draw

The program randomly generates 6 winning numbers. These numbers are then compared with the numbers on all the purchased tickets.

4. View Results

After the draw, users can check the results, including:

* Winning numbers
* Ticket ID
* Player name
* Number of matching numbers
* Prize amount

5. View All Tickets

This option displays all the tickets that have been purchased by the players.

# Prize Structure

| Matching Numbers |   Prize |
| ---------------- | ------: |
| 6                | ₹10,000 |
| 5                |  ₹5,000 |
| 4                |  ₹1,000 |
| 3                |    ₹100 |
| Less than 3      |      ₹0 |

## 🛠️ Technologies Used

* **Language:** Python
* **Module:** `random`
* **Interface:** Command Line / Terminal
* **External Libraries:** None

# ▶️ How to Run the Project

# Step 1: Check Python

Make sure Python is installed on your computer.

You can check it by running:

```bash
python --version
```

# Step 2: Save the Program

Save the Python code in a file named:

```text
lottery.py
```

# Step 3: Run the Program

Open the terminal in the project folder and run:

```bash
python lottery.py
```

# 📋 Main Menu

When the program starts, the following menu is displayed:

```text
================================
       LUCKYDRAW LOTTERY
================================
1. Register Player
2. Buy Lottery Ticket
3. Conduct Lottery Draw
4. View Results
5. View All Tickets
6. Exit
================================
```

The user can enter the number of the option they want to use.

# 🔄 How the Program Works

The basic flow of the program is:

```text
Start
  ↓
Register Player
  ↓
Buy Lottery Ticket
  ↓
Conduct Lottery Draw
  ↓
Generate Winning Numbers
  ↓
Compare Ticket Numbers
  ↓
Calculate Prize
  ↓
View Results
  ↓
Exit
```

# 📁 Project Structure

```text
LuckyDraw-Lottery/
│
├── lottery.py
└── README.md
```

# 🧠 Python Concepts Used

# `random.sample()`

The program uses:

```python
random.sample(range(1, 51), 6)
```

This generates 6 different random numbers between 1 and 50.

# Functions

Different parts of the program are handled using functions such as:

```text
register_player()
buy_ticket()
conduct_draw()
show_results()
view_tickets()
main()
```

Using functions makes the program easier to understand and manage.

# Lists

Lists are used to store information such as:

```text
players
tickets
winning_numbers
results
```

# Dictionaries

Dictionaries are used to keep information about players, tickets, and lottery results in an organized way.

# Conditional Statements

`if`, `elif`, and `else` are used for checking user choices, matching numbers, and deciding the prize amount.

# Loops

`while` and `for` loops are used to display the menu repeatedly and process players and tickets.

# ⚠️ Limitations

There are a few limitations in this project:

* The data is stored only while the program is running.
* All data is lost when the program is closed.
* No database or permanent file storage is used.
* There is currently no ticket purchase price.
* This lottery system is made only for learning and educational purposes.

# 🎓 Purpose of the Project

The main purpose of this project is to practice Python programming by creating a simple application based on a real-world idea.

It helps in understanding how functions, lists, dictionaries, loops, conditions, and the `random` module can work together in one project.

# 👨‍💻 Author

**Akash Deep**

**Python Project – LuckyDraw Lottery**
