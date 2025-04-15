using System;

public static class Kata
{
  
  public static int Solution(int value)
  {
    int total = 0;
      for (int i = 0; i < value; i++){
        /*  
        int i = 0 
            is declaring a variable i (stands for index or iterator).
            starting it at 0; this is the starting point of your loop.
          i < limit
            This is the condition that controls how long the loop runs.
            The loop keeps going as long as i is less than limit.
            The moment i is not less than limit, the loop stops.
           i++
            This is the increment.
            After each loop iteration, i is increased by 1.
            It's the same as saying i = i + 1.
          */
        
        if (i % 3 == 0 || i % 5 == 0) { // if i is divisible by 3 or by 5, add +1 to the total to get the sum.
          total += i;
        }    
      }
    return total;
    
  }
}
