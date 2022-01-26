def convertCase(arr, N) :
     
    # Stores the final sentence
    ans = "";
 
    # Loop to iterate over the array
    for i in range(N) :
 
        # If the current word is not the 1st
        # word, insert space
        if (len(ans) > 0) :
            ans += ' ';
 
        # Insert the first character of arr[i]
        ans += arr[i][0].upper();
     
        j = 1
         
        # Loop to iterate over current array element
        while j < len(arr[i]) :
             
            # If a space is found,
            # the next character
            # should be in upper case
            if (arr[i][j] == ' ') :
                ans += ' ';
                ans += arr[i][j + 1].upper();
                j += 1;
 
            # Otherwise the characters
            # must be in the lower case
            else :
                ans += arr[i][j].lower();
             
            j += 1;
 
    # Return Answer
    return ans;
 
# Driver program
if __name__ == "__main__" :
 
    arr = ["AnNiruddHA routh","LOVES", "to","COdE everyDAY"]
    N = len(arr);
    print(convertCase(arr, N));