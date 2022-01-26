var numPairsDivisibleBy60 = function(time) {
    let count=0
    for( let i=0;i<time.length;i++)
        {
            for(let j=i+1;j<time.length;j++)
                {
                    if( i<j && (time[i]+time[j])%60===0)
                        count+=1;
                }
        }
    return count;
};