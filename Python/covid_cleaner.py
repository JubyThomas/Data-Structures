import re
from turtle import up


def cleaner(data):
        # Your code goes here 
    
    result=data
    
    updated_result=[]
    for newr in result:
        if("%" in newr):
            new_text="0"
        else:    
            new_text =re.sub("\D", "", newr)
        if(len(new_text)==0):
          new_text=0
        updated_result.append(int(new_text))
        
    print(updated_result)
    
    restv=4-len(updated_result)
    print(restv)
    if(len(updated_result)<4):    
        for i in range(restv):
            updated_result.append(0)
        #print(updated_result)
        
    #print("hello ", updated_result)
    
    flag=False
    if(len(updated_result)==4):   
        
        if(updated_result[2]>updated_result[0]):    
            updated_result[2]=0  
            flag=True
        if(updated_result[1]> updated_result[0] and updated_result!=0 ):
            updated_result[1]=0
            flag=True     
       # print("now", updated_result)
        if(updated_result[2]<updated_result[3] and updated_result[1]<updated_result[0]):
            updated_result[2]=updated_result[2]+updated_result[3]
            #print("meow",updated_result[2])            
           # print("meow",updated_result)   
            if(updated_result[1]>0 and updated_result[2]>updated_result[0] -updated_result[1]):
                updated_result[2]=0
              #  print("pp",updated_result)
                     
         
        if(updated_result[2]> updated_result[3] and updated_result[1]==0):
            updated_result[1]=updated_result[0]-updated_result[2]
        
        if(updated_result[1]< updated_result[0]-updated_result[2] and updated_result[2]>updated_result[3]):
            updated_result[1]=updated_result[0]-updated_result[2]
        if(updated_result[3]<= (updated_result[2]) and updated_result[2]<updated_result[0]-updated_result[1] and flag==False):
            updated_result[2]=updated_result[0]-updated_result[1]    
        if(updated_result[0]< updated_result[2]+updated_result[1]):
           updated_result[1]=0
           updated_result[2]=0
        else:
            updated_result[0]==updated_result[1]+updated_result[2]
    print(updated_result)     
    
cleaner([ "60", "36", "26","22" ])        
        