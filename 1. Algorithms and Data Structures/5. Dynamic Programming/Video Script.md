# Dynamic Programming

Today we are going to learn how to further optimise our code by the use of dynamic programming, so what exactly is dynamic programming? Dynamic programming is the method of breaking down an optimisation problem into smaller sub problems so that each sub-problem is only solved once. 

So why is this important? Like a lot of methods in programming, it gives us a way to optimise our code it allows us to optimise problems where we want to reach a maximum or minimum solution. This technique is vital to reducing the complexity of recursive functions which are both inefficient in terms of time and space complexity. 

To better understand this let's take a deeper dive into what is actually happening when we run a recursive function and why this can have a detrimental effect on the efficiency of our program.

## The recursive problem

Firstly let's analyse recursive functions and try to understand why it is likely a bad idea to use this method when programming. Recursion is the method of defining a function in terms of itself. With a recursive function, the function is calling itself directly or indirectly and will continue this process until it solves the desired problem. 

[Show] Animation of simple recursive function calling itself to solve the problem

```
def recursive(x):
    if(x==0):
        return
    recursive(x-1)
```

Let's have a look at how we would generally approach a recursive problem. First, we define a base case, this is a conditional that will stop our program running once we reach it so that our function doesn't run indefinitely. Either a maximum we want to reach or a minimum. 

[Show] Show with the example above what would happen if we didn't have that conditional.

[Show] The max and min version and how those conditionals will stop the function from running.

```
def recursive_max(x):
    if (x==1000)
        return
    recursive_max(x)

def recursive_min(x)
    if (x==0)
        return
    recursive_min(x)
```
We then define the recursive rule to reach that destination, this will be called our recurrence relation. 

[Show] Some recurrence relations n * fact(n -1), 

This rule will run calling on itself until we reach the destination, the condition we defined earlier. Sounds great right, it solves our problem and we can implement it in a few lines of code. Now let's investigate why this in fact is going to be very computationally expensive for us. 

## Fibonacci function

To show this more clearly we will be using the classic recursive example the fibonacci sequence function. The fibonacci sequence is an integer sequence where every number in the sequence is the sum of the two previous numbers.

[Show]Fibonacci sequence of numbers

The function to get this sequence is 

[Show] Fibonacci function and walk through a few examples of how to get some numbers. 

Now let's have a look at how we would define this function in code using Python.

```

def fibonacci(n):
    # Simple base case. In this case if n is 0, it return 0, and if it is 1, it return 1.
    # Remember that, when you call for fibonacci(2), you will call for fibonacci(1) and fibonacci(0)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recurrence relation
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

So we can see that every time the function is run then is calling on the previous instance of the function and the instance before it to arrive at the required number. Now, this might seem like a great way to implement the function so why is this so computationally expensive?

Well to see this we need to understand what is actually going on when the function calls on itself. When the function calls on itself it will need to calculate all previous values of the function to arrive at the desired value. This is better explained with a diagram.

Let's take the example that we want to get the fibonacci sequence where n = 6.

[Show] Diagram of fibonacci sequence with all function call to return f(6).

So you can see because we're using recursion the function has to calculate all previous values of the functions to arrive at a solution. This makes the algorithm slow and it only gets worse the higher the value we need to calculate. 

We can even see it has to calculate multiple versions of the same function to arrive at a solution. We need fibonacci 5 and fibonacci 4 to calculate 6. From the diagram, we are calculating fibonacci 3, 3 times just to arrive at a solution!

So the algorithm isn't very efficient but just how inefficient is it? Well we think of the algorithm as splitting into two at every value needing to be calculated. You can see we arrive at a time complexity of O(2^n) which scales incredibly quickly! 

## Memorisation

So what can we do about solving this problem and optimise our code to be more efficient? Dynamic programming to the rescue! We can employ two techniques to resolve this problem memorisation and tabulation. 

First, we're going to look at memorisation to solve the problem. Another name for memorisation is top-down dynamic programming. Since we're starting at the top n = 6 and working our way to the base case n = 0. With memorisation what we do is each time we calculate the value of n in our recursive function we will store it in memory i.e memorisation so that we can call upon it again if needed. From before that fibonacci which was calculated 3 times is now only calculated once and is called upon when needed by our function.

This is how it looks in code

[Show] Point our memo[n] is storing the function value for every n. 

```
def fibonacci_memo(n, memo=None):
    # If the value is already calculated, return it
    if memo is None:
        memo = {}
    # If the value is not calculated, calculate it and store it
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    memo[n] = result
    return result

```
[Show] Run both functions and time them show the difference both functions for n = 35. Should take around 6 seconds to run.

Near instantaneous for our memorisation function but 6 seconds for our purely recursive function. Brilliant problem solved right? Not quite, notice our function is still calling itself recursively. Why is this a problem? Well, look what happens when we try to call a very large value of n = 100000.

[Show] Python recursive depth error when calling this. 

The problem here is that Python has a recursive depth limit which is actually 1000 times. So we won't be able to get the value required with this method. 

## Tabulation

We can solve this problem by another dynamic programming technique tabulation. With tabulation instead of computing our values with the top-down approach we can use a bottom-up approach to reach the desired value. What this means is we start from the base case and calculate all values as we go until we reach our goal. This avoids the recursive depth problem we have previously.  

```
def fib_tabulation(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        # Let's create a cache to store the results of the function
        memo = [None] * (n + 1)
        memo[0] = 0
        memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo
    
super_fib = fib_tabulation(10000)
```

[Show] Run the code and show that it runs without a recursive depth problem. Point out there is no recursion and each value is stored in a list as we go. 

Excellent but we can make this even more efficient! Currently, we would need to store all values in memory to work out the problem 10000 values!

What if we only needed to work out the previous value of the function? Then we don't need to store all previous values we can just store the last two values and discard the rest.

[Show] function only stores the last two variables and overwrites every time through. 

```
def fib_linear(n: int) -> int:
    """
    Return the nth number in the Fibonacci sequence.
    """
    if n == 0:
        return 0
    a = 0
    b = 1
    for _ in range(2, n):
        # a, b = b, a + b This would be even more efficient!
        c = a + b
        a = b
        b = c
    return a + b
    
super_fib_linear = fib_linear(10000)

```
[Show] Show the output of getsizeof and show it much reduced.

That's an amazing reduction in the size of our output making our function amazingly more memory efficient. 

## Tradeoffs

Why not always use tabulation in this case and forget about memorisation? Well it depends on what you want your function to do, how large the problem is and whether you want every value calculated. With memorisation if your problem doesn't require the computation of all sub problems. Memorisation has computational advantages in reaching a result since you won't have to calculate all values to reach the result. Though you can have problems with recursive depth if your problem is large in scale.

With tabulation the benefit is you can compute all necessary values so if you would like all values of your function then this method is more efficient. Access to solutions is fast since all values of your function will have been calculated. 

The decision is up to you really think about the scale of the problem and how you would like your values to be stored when you are using dynamic programing. I hope this helps in your understanding and leads to you implementing more efficient and robust code in your journey!
