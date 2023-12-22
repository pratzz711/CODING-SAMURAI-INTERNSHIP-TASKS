import pandas as pd

class ToDo:
    def __init__(self):
        self.tasks = []

    # Adding new task
    def addTask(self,title,description):
        id = len(self.tasks) + 1
        new_task = {"ID":id, "Title":title, "Description":description, "Status":0}
        self.tasks.append(new_task)
        print("\nTask added Successfully!\n")

    def display(self):
        if self.tasks != []:
            print("\n--------- To-Do List -----------")
            df = pd.DataFrame(self.tasks)
            # Show status acccording to boolean values
            df['Status'] = df['Status'].map({0: 'Pending', 1: 'Complete'})
            # To disable default index column
            print(df.to_string(index=False),"\n")
        else:
            print("\nTasks not found!!\n")

    def change_status(self,id):
    # if status is pending/false the change it to complete else/(True) change it to pending 
        for task in self.tasks:
            if task['ID'] == id and task['Status'] == 0:
                task['Status'] = 1
                print("\nTask marked as Completed\n")
            elif task['ID'] == id and task['Status'] == 1:
                task['Status'] = 0
                print("\nTask marked as Pending\n")
            else:
                print("Task not found")

    def delete(self,id):
        for task in self.tasks:
            if task['ID'] == id:
                self.tasks.remove(task)
                print("\nTask is Delelted\n")
                return
        print("\nTask not found\n")

    def save_tasks(self):
        with open('tasks.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task['ID']} | {task['Title']} | {task['Description']} | { task['Status'] }\n")
    
    def load_tasks(self):
        with open('tasks.txt', 'r') as file:
            for line in file:
                task_data = line.strip().split(' | ')
                ID, Title, Description, Status = task_data
                self.tasks.append({
                    'ID': int(ID),
                    'Title': Title,
                    'Description': Description,
                    'Status': int(Status)
                })
        print("\nTasks loaded successfully\n")  

    
if __name__ == "__main__":
    todoList = ToDo()

    while True:
        print("1. Add Task") 
        print("2. Display Tasks") 
        print("3. Change Status") 
        print("4. Delete Task")
        print("5. Save and Exit")
        print("6. Load Tasks")

        n = input("Enter the choice: ")

        if n == '1':
            title = input("\nEnter Title: ")
            description = input("Enter task Description: ")
            todoList.addTask(title,description)
        elif n == '2':
            todoList.display()
        elif n == '3':
            id = int(input("Enter Task ID to change status: "))
            todoList.change_status(id)
        elif n == '4':
            id = int(input("Enter Task ID to delete: "))
            todoList.delete(id)
        elif n == '5':
            todoList.save_tasks()
            print("\nTasks Saved!! \n")
            break
        elif n == '6':
            todoList.load_tasks()
        else:
            print("Invalid choice. Please enter number between 1-5")



