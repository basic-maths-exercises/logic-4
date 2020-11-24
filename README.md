# The logical conjunction

The previous exercise contrasted logical propositions such as ![](https://render.githubusercontent.com/render/math?math=X=1) and ![](https://render.githubusercontent.com/render/math?math=X=2) that can never be true simultaneously with propositions such as ![](https://render.githubusercontent.com/render/math?math=X<2) and ![](https://render.githubusercontent.com/render/math?math=X>1) which can.  We can place these notions that we gestured at in the previous exercise on a more firm foundation by introducing the logical conjunction operator and using this to write longer propositions such as:

![](https://render.githubusercontent.com/render/math?math=a<X\wedge\X<b)

If we wanted to write a python program to set a variable called `c` equal to 3 if this condition was true we would then write the following code:

````
if a < X and X < b : c = 3
````

The truth value of the proposition above is determined from the truth values of the two propositions of which it is composed using the following truth table:

<table>
  <tr> 
    <td>![](https://render.githubusercontent.com/render/math?math=a)</td>
    <td>![](https://render.githubusercontent.com/render/math?math=X)</td>
    <td>![](https://render.githubusercontent.com/render/math?math=ab)</td>
  </tr>  
  <tr><td>1</td><td>1</td><td>1</td></tr>
  <tr><td>1</td><td>0</td><td>0</td></tr>
  <tr><td>0</td><td>1</td><td>0</td></tr>
  <tr><td>0</td><td>0</td><td>0</td></tr>
</table>

__To complete the exercise you will need to use the ideas above to complete the function called `numberBetween`.__  This function takes three arguments:

1. `data` - a numpy array containing a list of numbers
2. `a` - a single integer  
3. `b` - a second integer which is greater than `a`

Your function should return the number of elements in `data` that are greater than `a` and less than `b`.

 
