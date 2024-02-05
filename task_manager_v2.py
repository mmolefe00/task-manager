# start
# ===== IMPORTING LIBRARIES =====
import datetime
from datetime import date, datetime


# ===== FUNCTIONS =====
def username_list():

    # read user file
    with open("user.txt", "r") as file:
        # create empty username list
        u_list = []

        # format file data to add to username list
        for lines in file:
            temp0 = lines.strip("\n")
            temp0 = temp0.split(", ")

            # append usernames to list (temp[0])
            u_list.append(temp0[0])

    # return username list for usage
    return u_list


def password_list():
    # read user file
    with open("user.txt", "r") as file:
        # create empty password list
        p_list = []

        # format file data to add to password list
        for lines in file:
            temp = lines.strip("\n")
            temp = temp.split(", ")

            # append passwords to list (temp[1])
            p_list.append(temp[1])

    # return password list for usage
    return p_list


def task_list():
    # read task file
    with open("tasks.txt", "r") as file:

        # create empty task list
        t_list = []

        # format file data to add to task list
        for lines in file:
            temp = lines.strip("\n")

            # split lines into entries - each lists the task information & can be indexed
            temp = temp.split(", ")

            # append entries to task list
            t_list.append(temp)

    # return task list for usage.
    return t_list


def reg_user():
    # assign variable to list of usernames
    usernames = username_list()

    # append to user file
    with open("user.txt", "a") as file:

        # username input loop
        while True:
            new_username = input("\nPlease enter a new username: ").lower()

            # ensure username does not already exist.
            if new_username in usernames:
                print('Oh no! That username already exists. Please Try again.')

            else:
                # create and confirm a new password
                new_password = input("Please enter a new password: ")  # skip '.lower()' for case-sensitive password.
                confirm_password = input("Please confirm your password: ")

                # password verification
                if new_password == confirm_password:
                    # write to user.txt file
                    file.write(f"\n{new_username}, {new_password}")  # '\n' at beginning to avoid miscounting

                    # confirm registration of new user
                    print("\nNew user confirmed.")
                    break

                # confirmation fail
                else:
                    print("Your passwords do not match. Try again.")

def add_task():
    # request user input for a new entry
    print("\nPlease enter the following details: \n")
    task_user = input("Assigned to:\t\t").lower()
    # capitalize for formatting and readability
    task_title = input("Task Title:\t\t\t").capitalize()
    task_description = input("Description:\t\t").capitalize()

    # due date input
    print("Please enter the project Due Date:")
    d_year = int(input("- Year(yyyy):\t\t"))
    d_month = int(input("- Month(m):\t\t"))
    d_date = int(input("- Date(dd):\t\t\t"))

    # use datetime module and format for task entry
    y = date(d_year, d_month, d_date)
    task_due = f'{y.strftime("%d")} {y.strftime("%b")} {y.strftime("%Y")}'

    # current date
    x = date.today()
    task_current = f'{x.strftime("%d")} {x.strftime("%b")} {x.strftime("%Y")}'  # creates current automatically on behalf of user.

    # entry format
    task_entry = f"\n{task_user}, {task_title}, {task_description}, {task_due}, {task_current}, No"
    # '\n' at beginning to avoid miscounting - at end will leave blank line @ end of text file.

    # open and write to task file
    with open("tasks.txt", "a") as file:
        file.write(task_entry)

def view_all():
    # read task file
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        # start count at zero
        count = 0
        # start task summary string as empty
        all_tasks = ""

        # loop through task
        for line in tasks:
            count += 1

            # indexing file data
            temp = line.strip("\n")
            temp = temp.split(", ")

            # formatting output for readability
            task_details = f'''TASK {count}:
Task Title:\t\t{temp[1]}
Description:\t{temp[2]}
Username:\t\t{temp[0]}
Due Date:\t\t{temp[3]}
Current Date:\t{temp[4]}
Completion:\t\t{temp[5]}\n'''  # strange indenting will occur in output text if aligned in code

            # concatenate each task detail to empty task summary string
            all_tasks += "\n" + task_details

        # output all the tasks for viewer to see
        return f'\n{all_tasks}'


def mark_task(a):       # A is corresponding task number for marking (init_task_num)
    # open file for reading
    with open("tasks.txt", "r") as file:
        updated_entry = ''
        count = 0

        # loop through the lines of the file
        for line in file:
            line = line.strip("\n")  # strip newline character

            # if the line number (count) = desired task number (a-1)
            # must -1 because index in code starts at 0 not 1
            if count == a - 1:
                # replace Completion: 'No' to 'Yes'.
                new_line = line.replace("No", "Yes")

            else:
                # otherwise leave the line as the same
                new_line = line

            # update all entries in file with newline (to be written back into file) - concatenate string
            updated_entry = f'{updated_entry}{new_line}\n'

            # increase the counter to keep checking each if line num = a-1
            count += 1

    # reopen file for writing to overwrite existing text. otherwise, the updated lines will be appended to the file
    with open("tasks.txt", "w") as write_file:
        write_file.write(updated_entry)

    return


def edit_task(b):       # b = selected task number (init_task_num)
    # read task file
    with open("tasks.txt", "r") as file:
        # begin with empty strings
        updated_file = ''
        updated_entry = ''
        # count starts at 1 like lines in the file
        count = 1

        # loop through the lines of the file
        for line in file:
            line = line.strip("\n")  # strip newline character

            # if the line number (count) = desired task number (b)
            if count == b:
                # split the line into a list
                words = line.split(', ')

                # if task is not complete - edit
                if words[5] == 'No':
                    # select from submenu
                    edit_choice = input("Select one of the following:\nu - Edit username\ndd - Edit due date\n: ")

                    # change username:
                    if edit_choice == 'u':
                        username = f'{words[0]}'
                        new_user = input(f"Currently assigned to:{username}\nPlease enter a new username: ")

                        # confirmation of new assignment
                        print(f'Now Assigned to: {new_user}')

                        # formatting entry with changes
                        entry_changes = f"{new_user}, {words[1]}, {words[2]}, {words[3]}, {words[4]}, No"

                        # append changes to empty string - this will be the line in the file
                        updated_entry = updated_entry + entry_changes


                    # change due date
                    elif edit_choice == 'dd':
                        print(f'Current date: {words[3]}')
                        # this helps inform the user of the required entry format

                        print("Please enter new Due Date below:")
                        n_year = int(input("- Year(yyyy):\t\t"))
                        n_month = int(input("- Month(mm):\t\t"))
                        n_date = int(input("- Date(dd):\t\t\t"))

                        # use datetime module and format for task entry
                        y = date(n_year, n_month, n_date)
                        new_ddate = f'{y.strftime("%d")} {y.strftime("%b")} {y.strftime("%Y")}'

                        # update current date automatically
                        x = date.today()
                        update_date = f'{x.strftime("%d")} {x.strftime("%b")} {x.strftime("%Y")}'

                        # formatting entry with changes
                        entry_changes = f"{words[0]}, {words[1]}, {words[2]}, {new_ddate}, {update_date}, No"

                        # append changes to empty string - this will be the line in the file
                        updated_entry = updated_entry + entry_changes

            else:
                # keep the line the same
                updated_entry = line

            # append the entry to the string that will become the overall text file
            updated_file = updated_file + updated_entry + "\n"

            # move onto next line in the existing file
            count += 1


        # reopen file for overwriting. Otherwise, the updated lines will be appended to the file.
        with open("tasks.txt", "w") as w_file:

            # write the string of updated entries to the file.
            w_file.write(updated_file)


def view_mine(a):  # 'a' is the username input from the login process.
    while True:
        # user selection from submenu - use .lower() to ensure correct entry
        sub_menu = input('''\nSelect one of the following Options below:
        vm - view my tasks
        ed - edit a task/mark as complete
        b  - back
        : ''').lower()

        # view my tasks
        if sub_menu == 'vm':
            # open task file and read lines
            with open("tasks.txt", "r") as file:
                my_tasks = file.readlines()
                count = 0

                for line in my_tasks:
                    count += 1  # tracks entries and assigns number to each task in output

                    # indexing file data
                    temp = line.strip("\n")
                    temp = temp.split(", ")

                    # formatting output
                    if temp[0] == f"{a}":  # username input condition to only put MY tasks
                        task_details = f'''
    TASK {count}:
    Username:\t\t{temp[0]}
    Task Title:\t\t{temp[1]}
    Description:\t{temp[2]}
    Due Date:\t\t{temp[3]}
    Current Date:\t{temp[4]}
    Completion:\t\t{temp[5]}'''
                        print(task_details)

            break

        # mark a task as complete
        elif sub_menu == 'ed':
            # request and confirm task to edit
            init_task_num = int(input("\nPlease enter the number (digit) of the task you'd like to edit: "))
            confirm_num = int(input("Confirm the task number: "))

            # once confirmed
            if init_task_num == confirm_num:
                # select from submenu - mark as complete or edit task
                sm_choice = input("\nSelect one of the following:\nmc - Mark as complete\net - Edit task\n: ").lower()

                if sm_choice == 'mc':
                    # run mark_task function with selected task number as a parameter
                    mark_task(init_task_num)
                    # confirm updated status of task to user.
                    print(f"Task {init_task_num} has been marked as complete. ")

                elif sm_choice == 'et':
                    # run edit_task function with selected task number as a parameter
                    edit_task(init_task_num)
            break

        # go back
        elif sub_menu == 'b':
            break

        # display error message
        else:
            print("Sorry! You've made the wrong choice. Please try again.")


def task_overview():
    # create task overview file if not already created:
    with open('task_overview.txt', 'w') as _:
        print("\nTask Overview Report Generated in file:\ttask_overview.txt")

    with open('tasks.txt', 'r') as file:
        # assign counter variables to keep track of total & in/complete tasks
        count = 0
        complete = 0
        incomplete = 0
        overdue = 0

        for line in file:
            # increase count +1 to track total number of lines
            count += 1

            # strip and split line into list to determine if line is completed or not
            line = line.strip("\n")
            words = line.split(', ')

            # if in/complete, increase respective counter value
            if words[5] == 'Yes':
                complete += 1
            if words[5] == 'No':
                incomplete += 1

            # overdue tasks
            d_date = words[3]

            # convert dates to datetime objects and compare
            due_date = datetime.strptime(d_date, "%d %b %Y")
            curr_date = datetime.now()

            # if due date has already passed (current date bigger than due date), increase overdue counter value
            if due_date < curr_date:
                overdue += 1
        complete_percent = round((complete/count) * 100, 2)
        incomplete_percent = round((incomplete/count) * 100, 2)
        overdue_percent = round((overdue/incomplete) * 100, 2)

        # format totals in readable format
        x = date.today()
        t_overview = f'''Total Tasks:\t\t\t{count}
Completed Tasks:\t\t{complete} / {count}\t\t{complete_percent}%
Incomplete Tasks:\t\t{incomplete} / {count}\t\t{incomplete_percent}%
 - Overdue Tasks:\t\t{overdue} / {incomplete}\t\t[{overdue_percent}%]\n
<<Report Generated on {x.strftime("%d")} {x.strftime("%b")} {x.strftime("%Y")}>>
______________________________________________\n'''

    # write to task overview file
    with open('task_overview.txt', 'w') as file:
        file.write(t_overview)


def mytask_list(a):
    with open("tasks.txt", "r") as file:
        count = 0
        my_tasks = []
        for line in file:
            count += 1  # tracks entries and assigns number to each task in output

            # indexing file data
            temp = line.strip("\n")
            temp = temp.split(", ")

            # formatting output
            if temp[0] == f"{a}":  # username input condition to only put MY tasks
                task_details = f'''
TASK {count}:
Username:\t\t{temp[0]}
Task Title:\t\t{temp[1]}
Description:\t{temp[2]}
Due Date:\t\t{temp[3]}
Current Date:\t{temp[4]}
Completion:\t\t{temp[5]}\n'''
                my_tasks.append(task_details)
        return my_tasks


def mytask_overview(a):
    # read task file
    with open('tasks.txt', 'r') as file:
        # assign counter variables to keep track of total & in/complete tasks
        count = 0
        complete = 0
        incomplete = 0
        overdue = 0

        # format task file
        for line in file:
            line = line.strip("\n")
            words = line.split(', ')

            # if task user = instance in username list
            if words[0] == f'{a}':
                # increase count +1 to track total number of lines
                count += 1

                # if in/complete, increase respective counter value
                if words[5] == 'Yes':
                    complete += 1
                if words[5] == 'No':
                    incomplete += 1

                # overdue tasks
                d_date = words[3]

                # convert dates to datetime objects and compare
                due_date = datetime.strptime(d_date, "%d %b %Y")
                curr_date = datetime.now()

                # if due date has already passed (current date bigger than due date), increase overdue counter value
                if due_date < curr_date:
                    overdue += 1

        # to avoid zero division error
        if count > 0:
            complete_percent = round((complete / count) * 100, 2)
            incomplete_percent = round((incomplete / count) * 100, 2)
        else:
            complete_percent = 0
            incomplete_percent = 0


        # to avoid zero division error
        if incomplete > 0:
            overdue_percent = round((overdue/incomplete) * 100, 2)
        else:
            overdue_percent = 0

        # format totals in readable format
        t_overview = f'''- Completed Tasks:\t\t{complete} / {count}\t\t{complete_percent}%
- Incomplete Tasks:\t\t{incomplete} / {count}\t\t{incomplete_percent}%
- Overdue Tasks:\t\t{overdue} / {incomplete}\t\t{overdue_percent}%\n\n'''

        # return t_overview for each user
        return t_overview


def user_overview():
    # create user_overview file in case not already created
    with open('user_overview.txt', 'w') as _:       # "_" is placeholder because no variable is used
        print("User Overview Report Generated in file:\tuser_overview.txt")

    # functions 'username_list' and 'task_list' return lists
    # therefore: use 'len' to get the total number of users and tasks
    total_users = len(username_list())
    total_tasks = len(task_list())

    # format database overview
    u_overview = f'''Total Registered Users:\t\t{total_users}
Total Database Tasks:\t\t{total_tasks}\n

=== INDIVIDUAL USER REPORTS: ===\n'''

    # functions 'username_list' and 'mytask_list' return lists
    # therefore: loop and index lists to get stats of tasks assigned to user
    user_overviews = ''
    for i in username_list():
        tasks_per_user = len(mytask_list(i))
        database_percent = (tasks_per_user / total_tasks) * 100

        # use user-specific task report function (mytask_overview) in formatted output
        individual_overview = f'''USER: {i.capitalize()}
Tasks in Database:\t\t{tasks_per_user} / {total_tasks}\t\t{database_percent}%
{mytask_overview(i)}'''

        # append to empty string
        user_overviews = user_overviews + individual_overview + "\n"

    # write to user_overview file
    with open('user_overview.txt', 'w') as file:
        x = date.today()
        file.write(f'''=== USER OVERVIEW: ===
{u_overview}{user_overviews}<<Report Generated on {x.strftime("%d")} {x.strftime("%b")} {x.strftime("%Y")}>>
______________________________________________''')


def disp_users():
    print("=== USER OVERVIEW: ===\n")
    # functions 'username_list' and 'task_list' return lists
    # therefore: use 'len' to get the total number of users and tasks
    total_users = len(username_list())
    total_tasks = len(task_list())

    # format database overview
    u_overview = f'''Total Registered Users:\t\t{total_users}
Total Database Tasks:\t\t{total_tasks}\n

=== INDIVIDUAL USER REPORTS: ===\n'''
    print(u_overview)

    # functions 'username_list' and 'mytask_list' return lists
    # therefore: loop and index lists to get stats of tasks assigned to user
    user_overviews = ''
    for i in username_list():
        tasks_per_user = len(mytask_list(i))
        database_percent = (tasks_per_user / total_tasks) * 100

        # use user-specific task report function (mytask_overview) in formatted output
        individual_overview = f'''USER: {i.capitalize()}
Tasks in Database:\t\t{tasks_per_user} / {total_tasks}\t\t{database_percent}%
{mytask_overview(i)}'''

        # append to empty string
        user_overviews = user_overviews + individual_overview + "\n"

    # output
    x = date.today()
    print(f'''{user_overviews}<<Report Generated on {x.strftime("%d")} {x.strftime("%B")} {x.strftime("%Y")}>>>>
______________________________________________''')


def disp_tasks():
    print("\n=== TASK OVERVIEW: ===\n")

    with open('tasks.txt', 'r') as file:
        # assign counter variables to keep track of total & in/complete tasks
        count = 0
        complete = 0
        incomplete = 0
        overdue = 0

        for line in file:
            # increase count +1 to track total number of lines
            count += 1

            # strip and split line into list to determine if line is completed or not
            line = line.strip("\n")
            words = line.split(', ')

            # if in/complete, increase respective counter value
            if words[5] == 'Yes':
                complete += 1
            if words[5] == 'No':
                incomplete += 1

            # overdue tasks
            d_date = words[3]

            # convert dates to datetime objects and compare
            due_date = datetime.strptime(d_date, "%d %b %Y")
            curr_date = datetime.now()

            # if due date has already passed (current date bigger than due date), increase overdue counter value
            if due_date < curr_date:
                overdue += 1
        complete_percent = round((complete / count) * 100, 2)
        incomplete_percent = round((incomplete / count) * 100, 2)
        overdue_percent = round((overdue / incomplete) * 100, 2)

        # format totals in readable format
        t_overview = f'''Total Tasks:\t\t\t{count}
Completed Tasks:\t\t{complete} / {count}\t\t{complete_percent}%
Incomplete Tasks:\t\t{incomplete} / {count}\t\t{incomplete_percent}%
- Overdue Tasks:\t\t{overdue} / {incomplete}\t\t[{overdue_percent}%]\n
Report Completed on: {curr_date}
______________________________________________\n'''
        print(t_overview)


def stats():
    # print heading
    print("\n====== STATISTICS: =====")

    # run task and user over_view functions
    disp_tasks()
    disp_users()


# ===== GREETING AND PROMPT =====
greeting = "Welcome To Task Manager!"
prompt = '''For all your small business task management needs.

LOGIN:'''
print(greeting)
print(prompt)

# ===== USER LOGIN AND VERIFICATION =====
while True:
    # create  variables for lists returned from functions that can be indexed.
    u_names = username_list()
    p_words = password_list()

    # username inputs
    u_name_input = input("Enter your username: ").lower()
    p_word_input = input("Enter your password: ")

    # === verification ===

    # incorrect username and/or password
    if u_name_input not in u_names or p_word_input not in p_words:
        print(f"\nError: Incorrect Username or Password.\n")

    # correct admin login response - Access Granted
    elif u_name_input == "admin" and p_word_input == "adm1n":
        print("\nWelcome Admin! Let's get started!")
        break

    # correct user login response option
    elif u_name_input in u_names:
        u = u_names.index(u_name_input)  # to get position in username list
        p = p_words.index(p_word_input)  # to get position in password list

        if u != p:
            # if username in list and password input does not correspond to username
            print(f"\nError: Incorrect Username or Password.\n")
        elif u == p:
            # if username in list and password input corresponds to username - Access Granted
            print(f"\nWelcome {u_name_input.capitalize()}. You have been logged in successfully!")
            break

    # assurance
    else:
        print(f"\nError: Incorrect Username and/or Password.\n")


# ===== MAIN MENU =====
while True:

    # === MENU OUTPUT DIFFERENTIATION ===

    # admin main menu
    if u_name_input == "admin":
        menu = input('''\n\n=== MAIN MENU: ===\n\nSelect one of the following Options below:
    r - Register a new user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

    # user main menu
    else:
        menu = input('''\n\n=== MAIN MENU: ===\n\nSelect one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()


    # === MENU SELECTION ===

    # admin only - new user registration
    if menu == 'r' and u_name_input == 'admin':
        # run reg_user function
        reg_user()
        pass


    # Assigning a new task
    elif menu == 'a':
        # run add_task function
        add_task()

        # confirm new task addition
        print('\nNew task added.')
        pass


    # view all tasks
    elif menu == 'va':
        # run and print the view all - otherwise printing inside function returns none value
        print(view_all())
        pass


    # view my tasks
    elif menu == 'vm':
        # run view_mine function with the current user's username as a parameter
        view_mine(u_name_input)
        pass


    # admin only - generate reports
    elif menu == 'gr' and u_name_input == 'admin':
        # run overview functions to generate reports
        task_overview()
        user_overview()


    # admin only - statistics
    elif menu == 'ds' and u_name_input == "admin":
        # run stats function
        stats()
        pass


    # exit
    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()


    # error message
    else:
        print("\nYou have made a wrong choice, please Try again.")

# end
