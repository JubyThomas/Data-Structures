var containsDuplicate = function(nums) {
    flag =false;
   for(i =0;i<nums.length;i++)
       {
          
           for(j=i+1;j<nums.length;j++)
               {
                      if(nums[j] == nums[i])
                         {
                         flag=true;
                         break;
                         }
                   
               }
      
       }
   
   return flag;
};


/*Solution 2*/

var containsDuplicate = function(nums) {
    let res= new Set(nums);
    if(nums.length ===res.size)
        return false;
    else
        return true;

};