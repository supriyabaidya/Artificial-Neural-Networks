'''
Created on 02-Jan-2018

@author: Supriya Baidya
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
version 3.0 (final release)
 
 Backpropagation :

 Algorithm of Backpropagation is given below along with the python code.
 '''
import math

def inclusive_range(start_layer,end_layer):
    return range(start_layer,end_layer+1)

def input_from_file(filename):
    global layers,x,class_label,learning_rate,epsilon,weights,biases
    
    f=open(filename)
    line_number=0
    while True:
        line=f.readline()    
        line=line.rstrip('\n')
        if len(line)==0:
            break
        line_number+=1
        word=line.split('=')     
        if line_number==1:
            for i in range(len(word[1])):
                layers.append(int(word[1][i]))
     
        temp_list={}
        if line_number==2 or line_number==6 or line_number==7:
            key_value=word[1].split(',')
            for i in range(len(key_value)):
                temp=key_value[i].split(':')
                key=temp[0]
                if line_number==6:
                    key=key.rstrip(')')
                    key=key.lstrip('(')
                    key=key.split('-')
                    key=(int(key[0]),int(key[1]))
                    weights[key]=float(temp[1])
                else:
                    value=temp[1]
                    temp_list[int(key)]=float(value)
              
            if line_number==2:
                x=temp_list
            else:
                biases=temp_list
      
          
          
        if line_number==3:
            class_label=float(word[1])          
        if line_number==4:
            learning_rate=float(word[1])
        if line_number==5:
            epsilon=float(word[1])
    
    f.close()


layers=[]
x={}
class_label=0
learning_rate=0
epsilon=0
weights={}
biases={}
Err={}
delta_weights={}
delta_biases={}

input_from_file('backpropagation_input.txt')        # taking input from 'input.txt' file and initialing the required variables

number_of_hidden_layer=len(layers)-2

terminating=False
terminating_condition=False

ip={}
op=x

epoch=1
while not terminating:
            
    terminating_condition=True          # terminating_condition will be updated according to previous_delta_weights
    
### Start of I/P forwarding and O/P calculation
    start_layer=0
    end_layer=0
    start_unit=0
    for each_layer in inclusive_range(1, len(layers)-1):
        
        start_layer+=layers[each_layer-1]                                         # for calculation of the index of starting unit of the corresponding layer
        end_layer=start_layer+layers[each_layer]                               # for calculation of the index of last unit of the corresponding layer(layers[each_layer] is number_of_units)
        for j in inclusive_range(start_layer+1,end_layer):          # for each unit in that layer
            
            weighted_sum=0            
            for i in inclusive_range(start_unit+1,start_layer):     # weighted sum to the corresponding unit (calculated using previous layer's Outputs,as start_layer is the index of last unit of previous layer)
                weighted_sum+=weights[(i,j)]*op[i]
            
            ip[j]=weighted_sum+biases[j]            
            op[j]=1/(1+math.exp(-ip[j]))
        
        start_unit+=start_layer
### End of I/P forwarding and O/P calculation

### Start of Error backpropagation
    for j in range(sum(layers), sum(layers)+layers[-1]):
        Err[j]=op[j]*(1-op[j])*(class_label-op[j])
    
    for j in inclusive_range(layers[0]+1,layers[0]+layers[1]):
        ErrW=Err[sum(layers)]*weights[(j,sum(layers))]      # 'sum(layers)' indicates next higher level i.e, last/Output layer
        Err[j]=op[j]*(1-op[j])*ErrW
### End of Error backpropagation
    
    for key in weights:
        i=key[0]
        j=key[1]
        
        delta_weights[key]=learning_rate*Err[j]*op[i]
        
        weights[key]+=delta_weights[key]
    
    for key in biases:        
        j=key
        
        delta_biases[key]=learning_rate*Err[j]
        
        biases[key]+=delta_biases[key]
    
    print('\n\nEpoch : ',epoch)
#     print("\nDelta Weights:")
#     print(delta_weights)

    for key in delta_weights:
        if delta_weights[key]>epsilon:
            terminating_condition=False
    
    if terminating_condition:
        terminating=True
        print("\nDelta Weights (each value is smaller than the predefined value of 'epsilon' as 0.001) :")
        print(delta_weights)
    
    print('\nWeights :')
    print(weights)
    print('\nBiases :')
    print(biases)
    
    epoch+=1