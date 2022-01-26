let nums=[-1,0,3,5,9,12]

let binarySearch=(nums,target)=>
{
    let start=0;
    let end=nums.length;
         
    // Iterate while start not meets end
    while (start<=end){
 
        // Find the mid index
        let mid=Math.floor((start + end)/2);
  
        // If element is present at mid, return True
        if (nums[mid]===target) return true;
 
        // Else look in left or right half accordingly
        else if (target < nums[mid])
             end = mid - 1;
        else
             start = mid + 1;
    }
  
    return false;
}

console.log(binarySearch(nums,9));

/** 
I've realized the fact that under these situations it's better to go with the while loop iteration instead of for loop where you need to reinitialize index from inside the loop.
*/