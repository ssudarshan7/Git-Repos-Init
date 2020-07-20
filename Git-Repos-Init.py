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
    os.system("cd "+prj_path + prj_name + " && git remote add " +repos+" " + statement + " && git push -u "+repos+ " master")

    
    
#process


if selection == 1:#windows
    #folder create 
    os.system(file_statement)
    print("folder created\n")

    #git initialise
    os.system(init_statement)

    #file create
    c_opt = str(input("Do you want to create a file (Y|N): "))
    if str.lower(c_opt) == 'y':
        while c_opt =='y':   
            os.system("cls")
            file_name = str(input("File name: "))
            os.system("cd " + prj_path + prj_name +"/ && cd. > " + file_name) #create a empty file
            c_opt = str(input("\n Do you want to create one more file? (Y|N): ")) 

    e = 'y'
    git_status = "cls" + "&& cd " + prj_path + prj_name +"&& git status"
    git_commit = "cd " + prj_path + prj_name +" && git commit "+ file_name +" -m " 
    git_log = "cd " + prj_path +prj_name +" && git log"
    os.system(git_status) # list the files
    
    while e == 'y':
        info = str(input("Enter the file name to add: "))
        os.system("cd " + prj_path + prj_name + "&& git add " + info)
        e = str(input("Do u want to add one more file (Y|N): "))
    
    #Push to remote
    if opt == 'y':
        os.system("cls")
        os.system(git_status)
        print("Project has been created and files as beed added")

        #git commit

        commit_msg = input("Enter the commit mssg: ")
        os.system(git_commit +'"'+commit_msg +'"') 
        print(git_commit +'"'+commit_msg +'"')
        os.system(git_status)
        os.system(git_log)

        print("\n\n Pushing the repos\n\n")
        
        push(push_code)

    elif opt =='n':
        os.system("cls")
        os.system(git_status)
        print("Project has been created and files as beed added")  
        o = input("Do you want to commit it now(Y|N): ")
        str.lower(o)

        #git commit 

        if o == 'y':
            commit_msg = input("Enter the commit mssg: ")
            os.system(git_commit +'"'+commit_msg +'"') 
            print(git_commit +'"'+commit_msg +'"')
            os.system(git_status)
            os.system(git_log)



elif selection == 2:#linux
    #folder create
    os.system(file_statement)
    print("folder created\n")

    #git initialise
    os.system(init_statement)
    #file create
    c_opt = str(input("Do you want to create a file (Y|N): "))
    if str.lower(c_opt) == 'y':
     while c_opt =='y':   
        os.system("clear")
        file_name = str(input("File name: "))
        os.system("touch " + prj_path + prj_name +"/" + file_name) #create a empty file
        c_opt = str(input("\n Do you want to create one more file? (Y|N): "))

    e = 'y'
    git_status = "clear" + "&& cd " + prj_path + prj_name +"&& git status"
    git_commit = "cd " + prj_path + prj_name +" && git commit "+ file_name +" -m " 
    git_log = "cd " + prj_path +prj_name +" && git log"
    os.system(git_status) # list the files
    while e == 'y':
        info = str(input("Enter the file name to add: "))
        os.system("cd " + prj_path + prj_name + "&& git add " + info)
        e = str(input("Do u want to add one more file (Y|N): "))
          
    #Push to remote
    if opt == 'y':
        os.system("clear")
        os.system(git_status)
        print("Project has been created and files as beed added")

        #git commit

        commit_msg = input("Enter the commit mssg: ")
        os.system(git_commit +'"'+commit_msg +'"') 
        print(git_commit +'"'+commit_msg +'"')
        os.system(git_status)
        os.system(git_log)

        print("\n\n Pushing the repos\n\n")
        
        push(push_code)
        
    elif opt =='n':
        os.system("clear")
        os.system(git_status)
        print("Project has been created and files as beed added")  
        o = input("Do you want to commit it now(Y|N): ")
        str.lower(o)

        #git commit 

        if o == 'y':
            commit_msg = input("Enter the commit mssg: ")
            os.system(git_commit +'"'+commit_msg +'"') 
            print(git_commit +'"'+commit_msg +'"')
            os.system(git_status)
            os.system(git_log)



          
else:
    print("Error")


