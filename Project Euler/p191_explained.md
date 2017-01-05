# Problem 91 explained

Let's assume we have 'n' days, we want to find a formula for the function:

<b><i>f(n) = # of ways to write "O","A","L" s.t. there are no more than 2 consecutive "O"s and no more than one "L"</i><b>

The simplest point to start is the "Late" days - we know that we can have at most one "L" in the chain.
Assuming "L" appears on day 'i', two day-chains are created - the first one is (i-1) days long, and the second is (n-i) days long.
What is left is to find a formula for:

<b><i>g(n) = # of ways to write "O"s and "A"s s.t. there are no more than 2 consecutive "O"s</i></b>

And then we have:

<b><i>f(n) = (sum of g(i - 1) * g(n - i) where i goes from 1 to n) + g(n) </i></b>

Let's assume we want to know <b>g(n)</b> for <b>n>3</b>.
Looking at the first three letters, we can divide into three cases according to the last "O" in the first three letters (We know there is such since "AAA" is illegal):

* The last "O" is the 3rd letter:
[x,x,O,x,x,...,x,x] the two first letters can be anything, so the number of such options is the number of total solutions for the last n-3 letters which is g(n-3)
* Similarly, if the last "O" is the 2nd letter: [x,O,x,x,...,x,x] the first letter can be anything so solution is g(n-2)
* Finally, if the last "O" is the 1st letter, there will be g(n-1) solutions

Thus:

<b><i> g(n) = g(n-1) + g(n-2) + g(n-3) </i></b>
