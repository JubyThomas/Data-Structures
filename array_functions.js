
let str=["Apple","zebra", "cat", "ken","orange"]
console.log(str.sort());
// sort function works only with string values



let nums=[12,78,3,89,90,37]
/*console.log(nums.sort());  // This wont work */
 console.log(nums.sort((a,b)=>{return a-b;}));  // Sorts in Ascending Order
 console.log(nums.sort((a,b)=>{return b-a;}));  //Sorts in Descending Order

/* Array Manipulations :*/
 

// 'Push and Pop' vs 'Shift and Unshift'
    //Push and Pop deal with end of the array while Shift and Unshift deal with beginning of the array.  


// push - to add elements to end of  array
// pop - to remove elements from end of an array
//unshift adds one or more elements to the beginning of array and returns new length
//shift removes elements from beginning of array and returns that elements 

let array = [1, 2];
array.unshift(4);
// output: 3 (new length of the array)
 
array.unshift('a', 'b', 'c');
// output: 6 (new length of the array)

