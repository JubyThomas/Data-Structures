
/*Input: s = "abcde", goal = "cdeab"
Output: true*/

let s="abcde";
let goal="cdeab";

var rotateString = function(s, goal) {
    let count=0
s.forEach(x => {
     console.log(x);
     console.log(goal.substring(0,1));
    if(x!==goal.substring(0,1))
     count+=1;
});    

console.log(count);
};

rotateString(s,goal);
