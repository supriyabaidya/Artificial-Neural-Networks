'''
Created on 02-Jan-2018

@author: Supriya Baidya
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
version 2.7 (final release)
 
 ADALINE :
 The ADALINE (Adaptive Linear Neuron) is a single OUTPUT-UNIT neural net with several INPUT-UNITs. One of the INPUT-UNIT act as bias and is permanently fixed at '1'. An ADALINE is trained with the help of the delta, or LMS,or Widrow-Hoff learning rule.
 The learning process is presented here as Procedure ADALINE-Learning.

 Algorithm of ADALINE is given below along with the python code.
 '''

print('----------------------------------ADALINE----------------------------------')
#### storing every Output to a file
output_file=open('adaline_output.txt', 'w')
print('----------------------------------ADALINE----------------------------------\n',file=output_file)

# Before Starting the main Algorithm of ADALINE, some environment requirement must be CHECKED,like,python compiler version,primary memory of the system etc,and if the system doesn't meet the requirement, the program will terminate showing proper message to user.

###BEGIN : CHECKING Environment
#### TODO write "checking" code here

## BEGIN : import statements for CHECKING
import subprocess
import socket
import sys
import platform
try:
    import msvcrt   # msvcrt is not present any other O.S than windows
except ImportError:
    pass

## END : import statements for CHECKING

# O.S checking
print('\nO.S checking :')
print('---------------------------------------------------------')
required_os='Windows'
installed_os=platform.system()  # platform.system() gives the name of installed O.S , for eg. Windows or Linux etc

print('Installed O.S is : ',installed_os)
print('Installed O.S is : ',installed_os,file=output_file)
print('Required O.S is : ',required_os)
print('Required O.S is : ',required_os,file=output_file)

if installed_os==required_os:
    print('Hence the Installed O.S meet the system requirement.\n')
    print('Hence the Installed O.S meet the system requirement.\n',file=output_file)
else:
    print('Hence the Installed O.S does not meet the system requirement.\n\nPlease run it onWindows machine.')
    print('Hence the Installed O.S does not meet the system requirement.\n\nPlease run it onWindows machine.',file=output_file)
    output_file.close()
    sys.exit()
print('****************************************')

# python version checking
print('\nPython version checking :')
print('---------------------------------------------------------')
required_python_version=(3,6,4)
installed_python_version=sys.version_info   #sys.version_info gives the installed python version

print('Installed python version is : ',installed_python_version[0],'.',installed_python_version[1],'.',installed_python_version[2])
print('Installed python version is : ',installed_python_version[0],'.',installed_python_version[1],'.',installed_python_version[2],file=output_file)
print('Required python version is : ',required_python_version[0],'.',required_python_version[1],'.',required_python_version[2],'.')
print('Required python version is : ',required_python_version[0],'.',required_python_version[1],'.',required_python_version[2],'.',file=output_file)
    
if installed_python_version[0]>=required_python_version[0] and installed_python_version[1]>=required_python_version[1] and installed_python_version[2]>=required_python_version[2]: # python version checking
    print('Hence the python compiler meet the system requirement.\n')
    print('Hence the python compiler meet the system requirement.\n',file=output_file)
else:
    print('Please install python version 3.6.4 or above.')
    print('Please install python version 3.6.4 or above.',file=output_file)
    print('\nPress any key to exit .')
    print('\nPress any key to exit .',file=output_file)
    msvcrt.getch()    # getch() is used to hold(for user to read the instruction before exit) the console(output) window on the screen after the whole program run is completed till the user enters a key from keyboard
    output_file.close()
    sys.exit()
print('****************************************')

# Available system memory checking
print('\nAvailable system memory checking :')
print('---------------------------------------------------------')

def is_connected_to_internet(): # method for checking the internet connection
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

######previous 'psutil' checking######

# if not pkgutil.find_loader("psutil"):   # checking 'psutil' package is present or not
#     if is_connected_to_internet():  # checking the internet connection is present or not
#         print('psutil is not present , so installing it.....')
#         print('psutil is not present , so installing it.....',file=output_file)
#         subprocess.call('python.exe -m pip install psutil',shell=True)  # installing the 'psutil' package
#     else:
#         print('please connect to internet to install psutil \nWithout psutil library,can not check total physical memory of the system.\nAfter installing psutil manually or connecting to internet Re-run it .')
#         print('please connect to internet to install psutil \nWithout psutil library,can not check total physical memory of the system.\nAfter installing psutil manually or connecting to internet Re-run it .',file=output_file)
# else:
#     print('\'psutil\' is present there , so continuing to memory check....\n')
#     print('\'psutil\' is present there , so continuing to memory check....\n',file=output_file)

######previous 'psutil' checking######

######updated 'psutil' checking######
try:
    import psutil
except ImportError: # checking 'psutil' package is present or not
    if is_connected_to_internet():  # checking the internet connection is present or not
        print('psutil is not present , so installing it.....')
        print('psutil is not present , so installing it.....',file=output_file)
        subprocess.call('python.exe -m pip install psutil',shell=True)  # installing the 'psutil' package
        import psutil       # import 'psutil' after installing it
    else:
        print('please connect to internet to install psutil \nWithout psutil library,can not check total physical memory of the system.\nAfter installing psutil manually or connecting to internet Re-run it .')
        print('please connect to internet to install psutil \nWithout psutil library,can not check total physical memory of the system.\nAfter installing psutil manually or connecting to internet Re-run it .',file=output_file)
        print('\nPress any key to exit .')
        print('\nPress any key to exit .',file=output_file)
        msvcrt.getch()    # getch() is used to hold(for user to read the instruction before exit) the console(output) window on the screen after the whole program run is completed till the user enters a key from keyboard
        output_file.close()
        sys.exit()
    
else:
    print('\'psutil\' is present there , so continuing to memory check....\n')
    print('\'psutil\' is present there , so continuing to memory check....\n',file=output_file)
######updated 'psutil' checking######

required_system_memory=100   # required system memory is 100 M (assumption)
available_system_memory = int(psutil.virtual_memory().available / (1024 ** 2)) # calculating the available system memory
print('Available(free) system memory is : ',available_system_memory,'M')
print('Available(free) system memory is : ',available_system_memory,'M',file=output_file)
print('Required free system memory is : ',required_system_memory,' M')
print('Required free system memory is : ',required_system_memory,' M',file=output_file)

if available_system_memory>required_system_memory:
    print('Hence the free system memory meet the requirement.\n')
    print('Hence the free system memory meet the requirement.\n',file=output_file)
else:
    print('The free system memory does not meet the requirement.\n')
    print('The free system memory does not meet the requirement.\n',file=output_file)
    print('\nPress any key to exit .')
    print('\nPress any key to exit .',file=output_file)
    msvcrt.getch()    # getch() is used to hold(for user to read the instruction before exit) the console(output) window on the screen after the whole program run is completed till the user enters a key from keyboard
    output_file.close()
    sys.exit()
print('****************************************')

###END : CHECKING Environment

#BEGIN : main ADALINE Algorithm and Code (variables name used in code are single quoted in Algorithm and superscript i of X is written as X_i) :

# step 1. Initialize weights with small random values (0<WEIGHT_i<1)

###BEGIN : step 1.
#### TODO write "Initialization" code here

## BEGIN : taking input file name
# Giving hint to user about file structure of input data
print('The input file structure of input data is given below for example :\n')
print('The input file structure of input data is given below for example :\n',file=output_file)
print('BEGIN : file structure')
print('BEGIN : file structure',file=output_file)
print('    learning_rate=0.2 \n\
    weights=0.25,0.25,0.25 \n\
    patterns::true output\n\
     1: 1::-1\n\
     1:-1:: 1\n\
    -1: 1::-1\n\
    -1:-1::-1')
print('    learning_rate=0.2 \n\
    weights=0.25,0.25,0.25 \n\
    patterns::true output\n\
     1: 1::-1\n\
     1:-1:: 1\n\
    -1: 1::-1\n\
    -1:-1::-1',file=output_file)
print('END : file structure\n')
print('END : file structure\n',file=output_file)
    
file_name=''
if sys.argv.__len__()==1:
    print('Usage : adaline.py [input_file_name]\n\
    \'input_file_name\' is optional , you can give the \'input_file_name\' here \n')
    print('Usage : adaline.py [input_file_name]\n\
    \'input_file_name\' is optional , you can give the \'input_file_name\' here \n',file=output_file)
    file_name='adaline_input.txt'
#     file_name=input('Enter the \'input_file_name\' now :')  # taking the 'input_file_name' to 'file_name' manually
else:
    file_name=sys.argv[1]   # storing the 'input_file_name' to 'file_name' from command line argument

## END : taking input file name 

## BEGIN : taking input from input file for Initialization
import traceback

def input_from_file(filename):  # method/function for taking input from input file , which is used later
    global learning_rate,weights,patterns,true_output
    
    try:
        #BEGIN : file line counting
        f=open(filename)
        file_length=-1
        while True:
            line=f.readline()
            file_length+=1
            if len(line)==0:
                break
        
        f.close()
        #END : file line counting
        
        #BEGIN : taking input from file
        f=open(filename)
        line_number=0
        while True:
            line=f.readline()
            line=line.rstrip('\n')
            if len(line)==0:
                if line_number<file_length: # manually triggering Error , if Format of the input file is wrong
                    print('Error : Wrong Input Format of the input file \n\
                    at line ',line_number+1)    # manually giving line number of input file , for eg. if a line is left blank in input file
                    print('Error : Wrong Input Format of the input file \n\
                    at line ',line_number+1,file=output_file)
                    print('Press any key to exit .')
                    msvcrt.getch()
                    output_file.close()
                    sys.exit()
                break
            line_number+=1
            word=line.split('=')
            
            if line_number==1:
                learning_rate=float(word[1])
            if line_number==2:
                weights=word[1].split(',')
                for i in range(weights.__len__()):  # 'i' is the iterator through weights for converting each weight to float 
                    weights[i]=float(weights[i])
            
            i=0    # 'i' is the iterator through patterns for taking each pattern
            if line_number==3:
                i=line_number
            
            if line_number>3:
                word=word[0].split('::')
                pattern=word[0].split(':')
                for i in range(pattern.__len__()):  # 'i' is the iterator through patterns for converting each pattern to int 
                    pattern[i]=int(pattern[i])
                patterns.append(pattern)
                true_output.append(int(word[1]))
        
        f.close();    
    except FileNotFoundError:
        traceback.print_exc()
        print(traceback.format_exc(),file=output_file)
        print('Press any key to exit .')
        msvcrt.getch()
        output_file.close()
        sys.exit()
    except EOFError:
        traceback.print_exc()
        print(traceback.format_exc(),file=output_file)
        print('Press any key to exit .')
        msvcrt.getch()
        output_file.close()
        sys.exit()
    except FloatingPointError:
        traceback.print_exc()
        print(traceback.format_exc(),file=output_file)
        print('Press any key to exit .')
        msvcrt.getch()
        output_file.close()
        sys.exit()
    except IOError:
        traceback.print_exc()
        print(traceback.format_exc(),file=output_file)
        print('Press any key to exit .')
        msvcrt.getch()
        output_file.close()
        sys.exit()
    except PermissionError:
        traceback.print_exc()
        print(traceback.format_exc(),file=output_file)
        print('Press any key to exit .')
        msvcrt.getch()
        output_file.close()
        sys.exit()
    except ValueError:
        traceback.print_exc()
        print(traceback.format_exc(),file=output_file)
        print('Press any key to exit .')
        msvcrt.getch()
        output_file.close()
        sys.exit()

#END : taking input from file


# BEGIN : variable declaration
learning_rate=0
weights=[]  # weights->list of weights
patterns=[]    # patterns->list of patterns
true_output=[]    # true_output->list of true OUTPUT

epoch=0     # for Iteration/epoch counting purpose
terminating=False   # for terminating condition checking purpose
# END : variable declaration

input_from_file(file_name)  # Calling the function/def input_from_file(filename) , for taking input from file

#BEGIN : Printing variables after input has taken from input file
print('\nWeights : ',weights)
print('\nWeights : ',weights,file=output_file)
print('List of patterns : ',patterns)
print('List of patterns : ',patterns,file=output_file)
print('true OUTPUT : ',true_output,'\n')
print('true OUTPUT : ',true_output,'\n',file=output_file)
#END : Printing variables after input has taken from input file

## END : taking input from input file for Initialization

###END : step 1.

# step 2. Set the learning rate 'learning_rate', usually on the basis of the inequality 0.1<=number_of_input * learning_rate<=1.0 , where 'number_of_input' is the number of input units.

###BEGIN : step 2.
#### TODO write "learning rate setting" code here
print('learning_rate : ',learning_rate) # learning rate has taken from file
print('learning_rate : ',learning_rate,file=output_file)
###END : step 2.

# step 3. Do step 4 to 7 while stopping criteria is not fulfilled.
print('\nStarting iteration of ADALINE Algorithm\n')
print('\nStarting iteration of ADALINE Algorithm\n',file=output_file)
while not terminating:
    print('epoch# ',epoch+1)
    print('epoch# ',epoch+1,file=output_file)
    
    print('Iteration    X[0]        X[1]        X[2]        Y_in        T[i]        Weights[0]    Weights[1]    Weights[2]')
    print('Iteration    X[0]        X[1]        X[2]        Y_in        T[i]        Weights[0]    Weights[1]    Weights[2]',file=output_file)
#     print ('iteration    x[0]        x[1]        x[2]        y_in          t[i]        weights[0]    weights[1]    weights[2]',file=output_file)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------',file=output_file)
# step 4. For each bipolar training pair s:t, do steps 5 to 7.
    NetInput=[]
    for i in range(0,4):    #for each training pair s:t
# step 5. Set Activation for input units,
#                X_0=1,
#                X_i=S_i for i = 1 to 'number_of_input'


###BEGIN : step 5.
#### TODO write "Activation Setting for input units" code here
        x=[]
        for j in range(0,3):    # for each input unit i
            if j==0:
                x.append(1)
            else:
                x.append(patterns[i][j-1])     #Xi=Si   i=1,...,m  and j-i instead j , cause s index are 0,1 instead 1,2
###END : step 5.

# step 6. Compute the net input to the output unit, Y_in=sum(X_i * W_i) , i = 0 to 'number_of_input'

###BEGIN : step 6.
#### TODO write "Compute the net input" code here
        y_in=0
        for j in range(0,3):    # for each input unit i
            y_in+=x[j]*weights[j]
        
#         y_in=float(format(y_in,'.2f'))    # formatting up to 2 decimal
        NetInput.append(y_in);
###END : step 6.

# step 7. Adjust weights using the following formula,
#                W_i(new)=W_i(old) + 'learning_rate' * ('true_output' - Y_in) * X_i ,  i = 0 to 'number_of_input' , and 'true_output' is true output

###BEGIN : step 7.
#### TODO write "weights Adjustment" code here
        for j in range(0,3):    # for each input unit i
            weights[j]+=learning_rate*(true_output[i]-y_in)*x[j]
        
        print((i+1),'             ',x[0],'          ',x[1],'          ',x[2],'          ',format(y_in,'.2f'),'        ',true_output[i],'          ',format(weights[0],'.2f'),'          ',format(weights[1],'.2f'),'          ',format(weights[2],'.2f'))
        output_file.write(str(i+1)+'             '+str(x[0])+'          '+str(x[1])+'          '+str(x[2])+'          '+str(format(y_in,'.2f'))+'        '+str(true_output[i])+'          '+str(format(weights[0],'.2f'))+'          '+str(format(weights[1],'.2f'))+'          '+str(format(weights[2],'.2f'))+'\n')
#         print((i+1),'             )+'x[0],'          ',x[1],''+str(        ',x[2],'          ',y_in,'        ',true_output[i],'          ',weights[0],'          ',weights[1],'          ',weights[2],file=output_file)
#         print ((i+1),'          ',x[0],'          ',x[1],'          ',x[2],'        ',y_in,'        ',true_output[i],'        ',weights[0],'        ',weights[1],'        ',weights[2],file=output_file)
###END : step 7.
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------',file=output_file)
    
# step 8. Compute output (y_out) from net input
###BEGIN : step 8.
#### TODO write "Compute output (y_out)" code here
    y_out=[]
    for i in range(0,4):    # for each pattern unit i
        if NetInput[i]>0:
            y_out.append(1)
        else:
            y_out.append(-1)
    
    print('\nOutput (y_out)')
    print('\nOutput (y_out)',file=output_file)
    print(y_out)
    print(y_out,file=output_file)
    print('Target Output (t)')
    print('Target Output (t)',file=output_file)
    print(true_output)
    print(true_output,file=output_file)
###END : step 8.
    
# step 9. CHECKING terminating condition
###BEGIN : step 9.
#### TODO write "CHECKING" code here
    if y_out==true_output:
        terminating=True
    
    epoch+=1    # epoch increasing by 1
###END : step 9.

###END : main ADALINE Algorithm and Code

output_file.close();

# Hold the console after completion if the whole program
print('\nGenerated output file is : \'adaline_output.txt\'  \n\nPress any key to exit .')
msvcrt.getch()    # getch() is used to hold(for user to read the console before exit) the console(output) window on the screen after the whole program run is completed till the user enters a key from keyboard
