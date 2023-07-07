#declaring variables
Pass = 0
Defer = 0
Fail = 0
progress = 0
module_trailer = 0
module_retriever = 0
student_ID=()
exclude = 0
replay = True  # the loop(replay) will continue until the user enter 'q'(replay==False)
range_1 = (0, 20, 40, 60, 80, 100, 120)
list_final = []
output_0=[]
main_list = []
student_ID_List_Final=[]
dict={}
replay2 = True
reloop=True

while reloop==True:
    while True :
        print('''\nEnter 1 for the student part
Enter 2 for the staff part
Enter 3 to quit''')
        try:    
            choice = int(input('Enter your choice : '))
            if choice == 1: #chooes the option "student"
                while True:
                    try:
                        Pass = int(input("Please enter marks at Pass : "))  # getting the pass mark
                        if Pass in range_1:  # analysis if the pass mark belongs to the required range
                            Defer = int(input("Please enter marks at Defer : "))  # getting defer mark
                            if Defer in range_1:  # analysis if the pass mark belongs to the required range
                                Fail = int(input("Please enter marks at Fail : "))  # getting fail mark
                                if Fail in range_1:  # analysis if the pass mark belongs to the required range
                                    total = Pass + Defer + Fail
                                    if total == 120:  # analysis if total equals to 120
                                        if Pass == 120 and Defer == 0 and Fail == 0:  # validation of "Progress"
                                            print("Progress")   
                                        elif Pass == 100 and Defer == 20 and Fail == 0 or Pass == 100 and Defer == 0 and Fail == 20:  # validation of "Progress(module trailer)"
                                            print("Progress(module trailer)")                
                                        elif Fail in (0, 20, 40, 60):  # validation of "Do not Progress-module retriever"
                                            print("Do not Progress-module retriever")    
                                        elif Fail in (80, 100, 120):  # validation of "Exclude"
                                            print("Exclude")
                                        break
                                    else:
                                        print("Your total incorrect!!! Please enter again...")
                                        continue       
                                else:
                                    print("You are out of` range! Please enter again...")
                                    continue    
                            else:
                                print("You are out of range! Please enter again...")
                                continue   
                        else:
                            print("You are out of range!!! Please enter again...")
                            continue
                    except ValueError:
                        print("Integer required")
                        continue   #send to the beginning of the while loop
    #staff section
            elif choice == 2: #choose the option "staff"
                while replay == True:
                    try:  # check whether the user has entered an integer
                        student_ID = str(input("Please enter your student_ID : w"))
                        if len(student_ID)==7:
                            while replay2 == True:
                                try:
                                    Pass = int(input("Please enter marks at Pass : "))  # getting the pass mark
                                    if Pass in range_1:  # analysis if the pass mark belongs to the required range
                                        Defer = int(input("Please enter marks at Defer : "))  # getting defer mark
                                        if Defer in range_1:  # analysis if the pass mark belongs to the required range
                                            Fail = int(input("Please enter marks at Fail : "))  # getting fail mark
                                            if Fail in range_1:  # analysis if the pass mark belongs to the required range
                                                total = Pass + Defer + Fail
                                                if total == 120:  # analysis if total equals to 120
                                                    if Pass == 120 and Defer == 0 and Fail == 0:  # validation of "Progress"
                                                        print("Progress")
                                                        list_final = ("Progress - ", Pass, ',', Defer, ',', Fail)
                                                        progress = progress + 1
                                                    elif Pass == 100 and Defer == 20 and Fail == 0 or Pass == 100 and Defer == 0 and Fail == 20:  # validation of "Progress(module trailer)"
                                                        print("Progress(module trailer)")
                                                        list_final = ("Progress(module trailer) - ", Pass, ',', Defer, ',', Fail)
                                                        module_trailer = module_trailer + 1
                                                    elif Fail in (0, 20, 40, 60):  # validation of "Do not Progress-module retriever"
                                                        print("Do not Progress-module retriever")
                                                        list_final = ("Do not Progress-module retriever - ", Pass, ',', Defer, ',', Fail)
                                                        module_retriever = module_retriever + 1
                                                    elif Fail in (80, 100, 120):  # validation of "Exclude"
                                                        print("Exclude")
                                                        list_final = ("Exclude - ", Pass, ',', Defer, ',', Fail)
                                                        exclude = exclude + 1
                                                    #dictionary
                                                    student_ID_List_Final.append(student_ID) 
                                                    output_0=list(list_final)
                                                    dict[student_ID]=output_0 #1=element([student_ID]),2=value(output)
                                                    replay2 = False
                                                else:
                                                    print("Your total incorrect!!! Please enter again...")
                                                    continue
                                            else:
                                                print("You are out of range! Please enter again from the begenning...")
                                                replay2 = True
                                                continue
                                        else:
                                            print("You are out of range! Please enter again from the begenning...")
                                            replay2 = True
                                            continue
                                    else:
                                        print("You are out of range!!! Please enter again from the begenning...")
                                        replay2 = True
                                        continue
                                except ValueError:
                                    print("Integer required ")
                                    replay2 = True
                        else:
                            print("Invalid ID number!!! Please enter again...")
                            continue
                        replay2 = False
                        replay = False
                    except ValueError:
                        print("Please enter the correct value !!! ")
                        continue
                    main_list.append(list_final) #append list_final to main list
                
                    f = open('file_created.txt', 'a') # creating text file0
                    f.write(''.join(map(str, list_final)))
                    f.write('\n')
                    f.close() # end of the text file
                
                    print("Do you need to run it again ?")  # asking for another turn
                    while True:
                        replay = input("Enter 'q' to quit or 'y' to continue : ")  # getting the value to do continue or quit
                        replay = replay.lower()  # change uppercase to lowercase if an uppercase entered
                        if replay == 'y':  # continue the program
                            replay2 = True
                            replay = True
                            break
                        elif replay == 'q':  # quit the program
                            replay2 = False 
                            replay = False
                            print("Histogram")  # printing "Histogram"
                            print("Progress", progress, " : ", end="")
                            for i in range(progress):
                                print("*", end="")
                            print()  # keep a seperate line(line break)
                            print("Trailer", module_trailer, " : ", end="")
                            for i in range(module_trailer):
                                print("*", end="")
                            print()  # keep a seperate line(line break)
                            print("Retriever", module_retriever, " : ", end="")
                            for i in range(module_retriever):
                                print("*", end="")
                            print()  # keep a seperate line(line break)
                            print("Excluded", exclude, " : ", end="")
                            for i in range(exclude):
                                print("*", end="")
                            print()# keep a seperate line(line break)
                            f_count = progress + module_trailer + module_retriever + exclude  # getting the final total count
                            print(f_count, "outcomes in total.")
                            print()
                            for i in range(len(main_list)):
                                print(*main_list[i])
                            break  # end the program
                        else:
                            print("Please Enter 'q' or 'y'")
                print()
                print("...DICTIONARIES...")  #dictionary
                x=0
                for x in range(len(student_ID_List_Final)):
                    y=str(student_ID_List_Final[x])
                    final_0=dict.get(y)
                    print(y, " : ", *final_0, end="") #print dictionary
                break          
    
            elif choice == 3: #choose the option "3"
                exit() #exit the program
            else:
                print("Entered value is invalid")
        except ValueError:
            print("Integer required..." )
            
            
            
'''
refernces 
https://stackoverflow.com/questions/21517024/how-to-join-values-of-map-in-python
https://www.w3schools.com/python/python_dictionaries.asp
https://www.w3schools.com/python/python_file_write.asp
https://stackoverflow.com/questions/68848991/in-python-3-5-how-are-triple-quotes-considered-comments-by-the-ide
'''
