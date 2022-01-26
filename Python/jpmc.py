
def convertCase(arr, N) :
    
    arr=arr.replace('\n', ' ')
    print(arr)   
    arr= arr.split(' ')
    print(len(arr))
    
    res=[]
    for i in range(0,len(arr)):
        x=arr[i][0].upper()+ arr[i][1::].lower()
        res.append(x)
    print(res)
    string1=" "
    print(string1.join(res))

if __name__ == "__main__" :
 
    arr = "AnNiruddHA\nrouth\nLOVES\nto\nCOdE\neveryDAY"
    N = len(arr);
    convertCase(arr, N)
    
