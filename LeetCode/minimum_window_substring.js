
var lengthOfLongestSubstring = function(s) {
    
    let currentmaxlength, maxlen=0;
    let flag=false;
    for(let i =0;i<s.length;i++)
        {

            let res="";
            for(let j=i;j<s.length;j++)
            {
               res+=s[j];
               
             //  console.log(j +" "+ res);
            
                if(res.indexOf(s[j])==-1)
                    {
                     console.log(i +" "+ res);
                      flag=true;
                        break;
                        
                    }
                
            }
            if(flag==true)
            {
            if(currentmaxlen> maxlen)
                maxlen=currentmaxlen;
            }
        }
    return maxlen;
};

console.log(lengthOfLongestSubstring("abcabcbb"));