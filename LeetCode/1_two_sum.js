var twoSum = function(nums, target) {
    
    let arr=[];
    let flag=false;
    for (let i=0;i,nums.length;i++)
        {
            for (let j=i+1; j<nums.length;j++)
                {
                 
                    if(nums[i]+nums[j]==target)
                        {
                            arr.push(i);
                            arr.push(j);

                            // or also return [i,j];
                            flag=true;
                            break;
                            
                        }
                }
            if(flag)
                break;
        }
    return arr;
};