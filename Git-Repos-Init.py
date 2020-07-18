import os
import subprocess

#OS selection
def os_select():
    os.system("clear")
    print("\t\t\t\t OS SELECTION \n")
    print("Supported OS: \n 1.Windows \n 2.Linux-Debian \n")
    os_name = int(input("Enter the choice: "))
    return os_name


#data input
prj_path = str(input("\nFile path: "))
prj_name = str(input("Project Name: "))
file_statement = "mkdir " + prj_path + prj_name
init_statement = "cd " + prj_path + prj_name + " && git init"
print("Are you going to push this to Github? (Y|N): ")
opt = str(input())
str.lower(opt)
if opt == 'y':
    push_code = str(input("PUSH CODE: "))
    repos = str(input("Remote Repos Name: "))
    selection = os_select()
elif opt =='n':
    selection = os_select()
else:
   os.system("clear")
   print("ERORR")


#Git Push
def push(statement):
    print("cd "+prj_path + prj_name + " git remote add " +repos + statement + " && git push -u"+repos+ "master")

#process

if selection == 1:
    print("Windows")
elif selection == 2:
    print("Linux")
else:
    print("Error")

