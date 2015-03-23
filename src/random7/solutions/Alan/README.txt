The easiest (think out of the box) solution is just return the result of the random integer from 1 to 5 and call it a random integer generator from 1 to 7 where the probability of getting 6 or 7 is 0.

This could be improved by mapping 5=>7, 4=>6, 3=>4, 2=>2, 1=>1.  Now it is the same as before but the odds of getting 3 or 5 are 0, but you get the range 1 to 5 and the average is even 4 which is what you would expect.

Now if we want to assume that we want a random integer generator where all values are equally likely I would do the following:

1) write function bitGen which does the following:
run the random number generator.  map a 1 or 2 to a 0 result and map a 3 or 4 to a 1 result and map a 5 to a retry.
2) run bitGen 3 times appending the results together.  For example if I ran bitGen 3 times and got a 1, 1, and 0 then the result would be 110.
3) convert that string to binary.  110 would be 6.
4) if the result is 0, start over, otherwise return the value.

The runtime on this is as follows:

The runtime is determined by the number of times you need to generate a randomInt from 1 to 5.  In our scenario, best case scenario you run it 3 times.  Worst case scenario you run it infinite times.

On expectation you run it:
let b1 be the expected number of times it takes to get 1 bit:
b1 = Sum( (1/5)^(1-n) * (4/5) * n , from n=1 to n = infinity )

let e be the expected number of times it takes to get your random integer from 1 to 7:
b = sum( (1/8)^(1-m) * (7/8) * m, from m=1 to m = infinity )
