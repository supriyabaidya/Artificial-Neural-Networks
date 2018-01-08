'''
Created on 26-Dec-2017

@author: TomHardy
'''
import copy

#there are 5 Training vectors s0 to s4 ,belong to 2 clusters c0,c1
s=[[1,0,0,0],[0,1,0,0],[1,1,0,0],[0,0,0,1],[0,0,1,1]]
cluster=[0,0,0,1,1] # s0 in cluster c0 and s3 in cluster c1 and so on

weights=[[s[0][0],s[3][0]],[s[0][1],s[3][1]],[s[0][2],s[3][2]],[s[0][3],s[3][3]]]
previous_weights=[]        # for stopping condition checking
training_vectors=[s[1],s[2],s[4]]       # since s0 & s3 are used in weight initialization, s1,s2,s4 are taken as training vectors
cluster_of_training_vectors=[0,0,1]
print('Initial weight :\n',weights)
print('Initial training vectors :\n',training_vectors)
learning_rate=0.2
decreasing_factor=0.5

terminating=False

epoch=1
while not terminating:
    x=0
    previous_weights=copy.deepcopy(weights)
    for each_training_vector in training_vectors:        
        #calculation of distance
        D_j=[0,0]
        for j in range(2):
            for i in range(len(each_training_vector)):
                D_j[j]+=(each_training_vector[i]-weights[i][j])**2
        
        minimum=0
        if D_j[1]<=D_j[minimum]:
            minimum=1
        
        J=minimum
        #weight vector update        
        if cluster_of_training_vectors[x]==J:
            for i in range(len(each_training_vector)):
                weights[i][J]+=learning_rate*(each_training_vector[i]-weights[i][J])
        else:
            for i in range(len(each_training_vector)):
                weights[i][J]-=learning_rate*(each_training_vector[i]-weights[i][J])
        
        x+=1
        
    learning_rate*=decreasing_factor
    print('Epoch :',epoch)
    epoch+=1
    print('Weights : \n',weights)
# stopping condition checking
    if previous_weights==weights:
        terminating=True