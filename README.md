# VOC-PROJECT

# Personal To-Do List Application

## 📌 Overview
A simple Python To-Do List application with file handling for persistence.  
Users can create, view, edit, delete, and categorize tasks.

## 🚀 Features
- Add tasks with title, description, and category (Work, Personal, Urgent).
- Mark tasks as completed.
- Delete tasks.
- Save tasks in a JSON file.
- Load tasks automatically when reopening the app.
- Simple Command-Line Interface (CLI).

## 🛠 Requirements
- Python 3.x installed

## ▶ Run the Application
bash
python todo.py

## 📂 Project Structure


/todo_app
 ├── todo.py        # Main application logic
 ├── tasks.json     # Task storage
 └── README.md      # Documentation


## 📸 Example Usage of output


--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 1
Enter task title: EXAM     
Enter task description: mid exams preparation
Enter task category (Work/Personal/Urgent): urgent
✅ Task added successfully!

--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 1
Enter task title: NETFLIX SERIES
Enter task description: wednesday,stranger things
Enter task category (Work/Personal/Urgent): personal
✅ Task added successfully!

--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 1
Enter task title: BUY GROCERIES
Enter task description: bread,veggies,fruits,milk,eggs,snacks
Enter task category (Work/Personal/Urgent): personal
✅ Task added successfully!

--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 2

1. EXAM [urgent] - ✘ Pending
   Description: mid exams preparation

2. NETFLIX SERIES [personal] - ✘ Pending
   Description: wednesday,stranger things

3. BUY GROCERIES [personal] - ✘ Pending
   Description: bread,veggies,fruits,milk,eggs,snacks

--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 3
1. EXAM [urgent] - ✘ Pending
   Description: mid exams preparation

2. NETFLIX SERIES [personal] - ✘ Pending
   Description: wednesday,stranger things

3. BUY GROCERIES [personal] - ✘ Pending
   Description: bread,veggies,fruits,milk,eggs,snacks
Enter task number to mark completed: 3
✅ Task marked as completed!

--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 2

1. EXAM [urgent] - ✘ Pending
   Description: mid exams preparation
2. NETFLIX SERIES [personal] - ✘ Pending
   Description: wednesday,stranger things

3. BUY GROCERIES [personal] - ✔ Completed
   Description: bread,veggies,fruits,milk,eggs,snacks

--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 4

1. EXAM [urgent] - ✘ Pending
   Description: mid exams preparation

2. NETFLIX SERIES [personal] - ✘ Pending
   Description: wednesday,stranger things

3. BUY GROCERIES [personal] - ✔ Completed
   Description: bread,veggies,fruits,milk,eggs,snacks
Enter task number to delete: 3
🗑 Task 'BUY GROCERIES' deleted!

--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 2

1. EXAM [urgent] - ✘ Pending
   Description: mid exams preparation

2. NETFLIX SERIES [personal] - ✘ Pending
   Description: wednesday,stranger things

--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 5
💾 Tasks saved. Exiting program...
