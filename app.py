# Simple Todo app
import json

todos = [] #create a sheet where our todos will be added
users = [] #create a sheet where user data will be added
current_user = None #current user not

def load_data(filename): #create a function that will help us save data
    try:
        with open(filename, 'r') as f: #create a json file
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): #if it gives an error let it be ignored
        return []

def save_data(filename, data): #we create functions that will allow us to collect our data
    with open(filename, 'w') as f:  #create a json file
        json.dump(data, f)

def register_user(username, password): #create functions that will allow us to register a user
    for user in users: #if the user is in 'users' let him do nothing
        if user['username'] == username:
            return None
    new_user = {'username': username, 'password': password, 'todos': []} #the user creates his login and password
    users.append(new_user) #user data is added to 'users'
    save_data('Todo.json', users) #add user data to 'Todo.json'
    return new_user

def login_user(username, password): #we create functions that will allow us to log into our current account
    for user in users: #if the user is in 'users' 
        if user['username'] == username and user['password'] == password: #the user sets his login and password
            return user
    return None

def add_task(task, user): #create a function that will allow us to add to the sheet Todo
    user['todos'].append(task)
    save_data('Todo.json', users) 

def remove_task(index, user): #create a function that will allow us to delete Todo from a sheet
    if 1 <= index <= len(user['todos']) + 1:
        user['todos'].pop(index-1)
        save_data('Todo.json', users)


def show_todo(user): #create a function that will allow us to view all Todos in a sheet
    for index,todo in enumerate(user['todos']): #number all todos
        print(f"{index+1}: {todo}")


def main(): #create a function that will display all the work for us
    global users, current_user
    users = load_data('Todo.json') #save all users in a file Todo.json
    print('\nToDo App\n')

    while True:
        

        if not current_user: #if there is no user, options>
            print()
            print('1. Register')    #registration
            print('2. Login')  #log into the system
            print('3. Exit')   #log out
            print()
            choice = input('Enter your choice: ') #let the user choose one of the options

            if choice == '1':  #if the user selects 1 option
                username = input('Enter username: ') #usertel must enter username
                password = input('Enter password: ') #usertel must enter password
                user = register_user(username, password) #user is registered
                if user: 
                    print('Registration succesfull!')
                    current_user = user 
                else: #if the user is already registered, let him print the bottom inscription
                    print()
                    print('Username already exists!')
                    
            elif choice == '2': #if the user selects 2 option
                username = input('Enter username: ') #usertel must enter username
                password = input('Enter password: ')  #usertel must enter password
                user = login_user(username,password) 
                if user: #if the user is found let it display the bottom inscription
                    print()
                    print(f"Loged in as {user['username']}")
                    current_user = user
                else: #if the user is not found, let him ask to register
                    print('Please register!') 
            elif choice == '3': #if the user selects 3 option
                print('Bye.') 
                break    
            else:
                print('Try again!')
        else:
            print()
            print('1.Add Todo.')
            print('2.Remove Todo.')
            print('3.Show Todo.')
            print('4.Quit.')
            print('5.Logout.')
            print()
            choice = input('Select: ') #let the user choose one of the options
            print()

            if choice == '1': #if the user selects 1 option
               todo = input('Enter your Todo: ') #user creates a Todo
               add_task(todo,current_user)
              
            elif choice == '2': #if the user selects 2 option
                index = int(input('Enter index:')) #user deletes current Todo
                remove_task(index,current_user)
               
            elif choice == '3': #if the user selects 3 option
                show_todo(current_user) #see all Todo
            elif choice == '4': #if the user selects 4 option
                print('Quit!')  #leave the system
                break
            elif choice == '5': #if the user selects 5 option
                current_user = None #log out
                print('Logout succesfull!')
                continue
            else:
                print('Try again!')
main() #we call a function that will run the program we wrote
