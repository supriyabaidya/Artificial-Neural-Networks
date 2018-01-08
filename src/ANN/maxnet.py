'''
Created on 02-Jan-2018

@author: Supriya Baidya
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
version 2.5 (final release)
 
 MAXNET :
 The MAXNET is a simplest artificial neural net that works on the principle of competition. It is fully connected network with symmetric interconnections and self-loops.
THere is no need to train MAXNET because all weights are fixed. While the self-loops have the weight 1, other interconnection paths have same inhibitory weights '-delta'  ,where 'delta' has to satisfy the condition
0<'delta'<(1/'m') , m being size of the MAXNET

In MAXNET Clustering, The given pattern X=[x_0,x_1, . ... ..  ,x_m] is to be clustered.

 Algorithm of MAXNET is given below along with the python code.
 '''
def winner_takes_all(my_list):  # 'winner_takes_all' is the method/def for "winner takes all" strategy , this method is used in main algorithm
    array=[]
    for i in range(0,len(my_list)):
        if my_list[i]>0:
            array.append(i)
    return array

print('----------------------------------MAXNET----------------------------------')
#### storing every Output to a file
output_file=open('maxnet_output.txt', 'w')
print('----------------------------------MAXNET----------------------------------\n',file=output_file)

# Before Starting the main Algorithm of ADALINE, some environment requirement must be CHECKED,like,python compiler version,primary memory of the system etc,and if the system doesn't meet the requirement, the program will terminate showing proper message to user.

###BEGIN : CHECKING Environment
#### TODO write "checking" code here

## BEGIN : import statements for CHECKING
import subprocess
import socket
import sys
import msvcrt
## END : import statements for CHECKING

required_python_version=(3,6,4)
installed_python_version=sys.version_info   #sys.version_info gives the installed python version

if installed_python_version[0]>=required_python_version[0] and installed_python_version[1]>=required_python_version[1] and installed_python_version[2]>=required_python_version[2]: # python version checking
    print('Installed python version is : ',installed_python_version[0],'.',installed_python_version[1],'.',installed_python_version[2])
    print('Installed python version is : ',installed_python_version[0],'.',installed_python_version[1],'.',installed_python_version[2],file=output_file)
    print('Required python version is : 3.6.4')
    print('Required python version is : 3.6.4',file=output_file)
    print('Hence the python compiler meet the system requirement.\n')
    print('Hence the python compiler meet the system requirement.\n',file=output_file)
else:
    print('Installed python version is : ',installed_python_version)
    print('Installed python version is : ',installed_python_version,file=output_file)
    print('Required python version is : 3.6.4 .')
    print('Required python version is : 3.6.4 .',file=output_file)
    print('Please install python version 3.6.4 or above.')
    print('Please install python version 3.6.4 or above.',file=output_file)
    print('Exiting .....')
    print('Exiting .....',file=output_file)
    print('Press any key to exit .')
    print('Press any key to exit .',file=output_file)
    msvcrt.getch()    # getch() is used to hold(for user to read the instruction before exit) the console(output) window on the screen after the whole program run is completed till the user enters a key from keyboard
    sys.exit()


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

######update 'psutil' checking######
try:
    import psutil
except ImportError: # checking 'psutil' package is present or not
    if is_connected_to_internet():  # checking the internet connection is present or not
        print('psutil is not present , so installing it.....')
        print('psutil is not present , so installing it.....',file=output_file)
        subprocess.call('python.exe -m pip install psutil',shell=True)  # installing the 'psutil' package
    else:
        print('please connect to internet to install psutil \nWithout psutil library,can not check total physical memory of the system.\nAfter installing psutil manually or connecting to internet Re-run it .')
        print('please connect to internet to install psutil \nWithout psutil library,can not check total physical memory of the system.\nAfter installing psutil manually or connecting to internet Re-run it .',file=output_file)
        print('\nPress any key to exit .')
        print('\nPress any key to exit .',file=output_file)
        msvcrt.getch()    # getch() is used to hold(for user to read the instruction before exit) the console(output) window on the screen after the whole program run is completed till the user enters a key from keyboard
        sys.exit()
    
else:
    print('\'psutil\' is present there , so continuing to memory check....\n')
    print('\'psutil\' is present there , so continuing to memory check....\n',file=output_file)
######updated 'psutil' checking######

available_system_memory = int(psutil.virtual_memory().available / (1024 ** 2)) # calculating the available system memory
print('Available system memory is :',available_system_memory,'M')
print('Available system memory is :',available_system_memory,'M',file=output_file)

required_system_memory=100   # required system memory is 100 M (assumption)
if available_system_memory>required_system_memory:
    print('Hence the system memory meet the requirement.\n')
    print('Hence the system memory meet the requirement.\n',file=output_file)
else:
    print('The system memory does not meet the requirement.\n')
    print('The system memory does not meet the requirement.\n',file=output_file)
    print('\nPress any key to exit .')
    print('\nPress any key to exit .',file=output_file)
    msvcrt.getch()    # getch() is used to hold(for user to read the instruction before exit) the console(output) window on the screen after the whole program run is completed till the user enters a key from keyboard
    sys.exit()

###END : CHECKING Environment

#BEGIN : main MAXNET Algorithm and Code (variables name used in code are single quoted in Algorithm and superscript i of X is written as X_i) :

# step 1. Initialize the net inputs to the cluster units
#                For i = 1 To m Do y_in_i=x_i

###BEGIN : step 1.
#### TODO write "Initialization" code here

## BEGIN : taking input file name
# Giving hint to user about file structure of input data
print('The input file structure of input data is given below for example :\n')
print('The input file structure of input data is given below for example :\n',file=output_file)
print('BEGIN : file structure')
print('BEGIN : file structure',file=output_file)
print('    m=4\n\
    delta=0.2\n\
    x=0.5,0.8,0.3,0.6')
print('    m=4\n\
    delta=0.2\n\
    x=0.5,0.8,0.3,0.6',file=output_file)
print('END : file structure\n')
print('END : file structure\n',file=output_file)
    
file_name=''
if sys.argv.__len__()==1:
    print('Usage : maxnet.py [input_file_name]\n\
    \'input_file_name\' is optional , you can give the \'input_file_name\' here \n')
    print('Usage : maxnet.py [input_file_name]\n\
    \'input_file_name\' is optional , you can give the \'input_file_name\' here \n',file=output_file)
    file_name=input('Enter the \'input_file_name\' now :')  # taking the 'input_file_name' to 'file_name' manually
else:
    file_name=sys.argv[1]   # storing the 'input_file_name' to 'file_name' from command line argument

## END : taking input file name 

## BEGIN : taking input from input file for Initialization
import traceback

def input_from_file(filename):  # method/function for taking input from input file , which is used later
    global m,delta,x
    
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
                    sys.exit()
                break
            line_number+=1
            word=line.split('=')
            
            if line_number==1:
                m=int(word[1])
            if line_number==3:
                x=word[1].split(',')
                for i in range(x.__len__()):  # 'i' is the iterator through x for converting each pattern to float 
                    x[i]=float(x[i])
            if line_number==2:
                delta=float(word[1])
                        
        f.close();    
    except FileNotFoundError:
        traceback.print_exc()
        print('Press any key to exit .')
        msvcrt.getch()
        sys.exit()
    except EOFError:
        traceback.print_exc()
        print('Press any key to exit .')
        msvcrt.getch()
        sys.exit()
    except FloatingPointError:
        traceback.print_exc()
        print('Press any key to exit .')
        msvcrt.getch()
        sys.exit()
    except IOError:
        traceback.print_exc()
        print('Press any key to exit .')
        msvcrt.getch()
        sys.exit()
    except PermissionError:
        traceback.print_exc()
        print('Press any key to exit .')
        msvcrt.getch()
        sys.exit()
    except ValueError:
        traceback.print_exc()
        print('Press any key to exit .')
        msvcrt.getch()
        sys.exit()

#END : taking input from file


# BEGIN : variable declaration
m=0     # m ->size of MAXNET
delta=0 # delta ->weights
y_in=[] # y_in -> list of inputs
x=[]    # x -> list of patterns

epoch=0     # for Iteration/epoch counting purpose
# END : variable declaration

input_from_file(file_name)  # Calling the function/def input_from_file(filename) , for taking input from file

#BEGIN : Printing variables after input has taken from input file
print('\nIn this program , size of MAXNET  is assumed : ',m)
print('\nIn this program , size of MAXNET  is assumed : ',m,file=output_file)
print('weights : ',delta)
print('weights : ',delta,file=output_file)
print('list of patterns : ',x,'\n')
print('list of patterns : ',x,'\n',file=output_file)

#END : Printing variables after input has taken from input file

## END : taking input from input file for Initialization

y_in=x      #Initialize the net inputs to the cluster units,             For i = 1 To m Do y_in_i=x_i

###END : step 1.

# step 2. Compute Activation for each cluster unit,
#                For i = 1 To m Do y_out_i = f(y_in_i) = y_in_i      , if y_in_i >=0
#                                                                      = 0            ,otherwise

###BEGIN : step 2.
while True:
    epoch+=1    # epoch increasing by 1
    y_out=[]
    for i in range(0,m):    # for each unit i
        if y_in[i]>=0:
            y_out.append(y_in[i])
        else:
            y_out.append(0)
    
    print ('epoch -> ',epoch,' | y_out -> ',y_out)
    print ('epoch -> ',epoch,' | y_out -> ',y_out,file=output_file)
###END : step 2.

# step 3. CHECKING terminating condition
###BEGIN : step 3.
#### TODO write "CHECKING" code here
    if len(winner_takes_all(y_out))==1:
        print ('winner is unit : ',winner_takes_all(y_out)[0]+1)       # '+1' as the index is always stated from 0
        print ('winner is unit : ',winner_takes_all(y_out)[0]+1,file=output_file)
        break
###END : step 3.

# step 4. Update net input to each cluster unit, Y_in_i = Y_out_i - delta * sum(Y_out_i) , i = 1 to 'm'

###BEGIN : step 4.
#### TODO write "Compute the net input" code here
    for i in range(0,m):    # for each unit i
        y_in[i]=y_out[i]-(sum(y_out)-y_out[i])*delta
###END : step 4.

###END : main ADALINE Algorithm and Code

output_file.close()

# Hold the console after completion if the whole program
print('\nGenerated output file is : \'maxnet_output.txt\'  \n\nPress any key to exit .')
msvcrt.getch()    # getch() is used to hold(for user to read the console before exit) the console(output) window on the screen after the whole program run is completed till the user enters a key from keyboard
