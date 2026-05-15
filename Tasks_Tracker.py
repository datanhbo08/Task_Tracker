tasks = []

#Axuliary
def displayTasks(all_tasks):
  print('\nYour Tasks: ')
  if len(all_tasks) <= 0:
    print(f'\nYou Have No Task!')
  else:
    for index, task in enumerate(all_tasks):
      print(f'{index + 1}: {task}')

def NewOperation(all_tasks):
  operation = input("press 'A' to add a new task\npress 'E' to Edit a Task\npress 'R' to remove the task\npress 'F' to quit aplication\n")

  if operation =='A':
    AddTask(all_tasks)
  elif operation =='E':
    EditTask(all_tasks)
  elif operation =='R':
    RemoveTask(all_tasks)
  elif operation =='F':
    return 
  else:
    NewOperation(all_tasks)

#removeTask function
def RemoveTask(all_tasks):
  task_number = input("enter number of task you want ot remove: ")
  all_tasks.remove(all_tasks[int(task_number)-1])

  print(f'\nItem{task_number} removed!')

  displayTasks(all_tasks)
  NewOperation(all_tasks)

#add Task function
def AddTask(all_tasks):
  new_task = input("add a task: ")
  all_tasks.append(new_task)

  displayTasks(all_tasks)
  NewOperation(all_tasks)

#Edit Task Function
def EditTask(all_tasks):
  task_number = input("Task number you wabt to edit: ")

  new_task = input('Edit Task: ')
  all_tasks[int(task_number)-1] = new_task

  print(f'Item {task_number} edited!')

  displayTasks(all_tasks)
  NewOperation(all_tasks)


#task application
AddTask(tasks)
