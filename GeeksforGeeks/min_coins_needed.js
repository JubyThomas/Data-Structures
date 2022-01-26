/*Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents */


let coins= [25, 10, 5];
let  V = 30;


function min_coins=(coins,V)={

    for(let i=0;i<coins.length;i++)
    {
        for(let j=i+1;j<coins.length;j++)
        {
            if(coins[i]+coins[j]===V){
                
            }

        }
    }
}