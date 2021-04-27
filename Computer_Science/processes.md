>*how particular patterns of procedures and expressions cause particular patterns of execution.*

> If we're going to understand processes and how we control them, then we have to a mapping from the mechanisms of this procedure into the way in which these processes behave.

> to understand this we're going to have a **mechanical model**, **engineering model**.

# substitution model

## KINDS OF EXPRESSIONS

* numbers
* symbols 
* lambda expressions (special forms)
* definitions (special forms)
* conditionals (special forms)
* combinations

## Substitution Rule

    To evaluate an application
        Evaluate the operator to get procedure
        Evaluate the operands to get arguments
        Apply the procedure to the arguments
            Copy the body of the procedure,
             substituting the arguments supplied
             for the formal parameters (形参) of the procedure.
            Evaluate the resulting new body.

    (IF <predicate>    判断表达式
        <consequent>   结果表达式
        <alternative>) 选择表达式 

    To evaluate an IF expression
        Evaluate the predicate expression
            if it yields TRUE
                evaluate the consequent expression
            otherwise
                evaluate the alternative expression

> some order: right to left

> The key to understanding complicated things is to know what not to look at and what not compute and what not to think.

> if you can name it, you have power of it


* Peano arithmetic

    皮诺亚算数定义的求和过程

    这个程序运行起来的时候是一个递归，简单说就是 x 不断递减，y 不断递增。直到 x 等于 0 ，这时 y 就是 x 和 y 的和。

    这个例子很好的说明了 Substitution Rule

        (DEFINE (+ x y)
            (IF (= x 0)
                Y
                (+ (-1+ x) (1+ y))))

        e.g. 
        (+ 3 4)             (process time)
        -> (+ 2 5)          |
        -> (+ 1 6)          |
        -> (+ 0 7)          |
        ---------->(process space)
        -> 7
        _________________________________
        Linear Iteration Process:
        time = O(x)
        space = O(1)
> O(x) is order x, 表示结果正比于 x，至于正比的系数是不考虑的，总是是个常量。O(1) 表示结果是不变的，是个常量，至于常量具体的值是不考虑的。

> Substitution Rule is how a program made out of procedures and expressions evolves a process. Substitution Rule maybe not preciseness but good enough for now. I'd like to develop som intuition about how particular programs evolve particular processes, what the shapes of programs have to be in order to get particular shaped processes.

* another Peano arithmetic

        (DEFINE (+ x y)
            (IF (= x 0)
                Y
                (1+ (+ (-1+ x) y))))
        
        e.g.
        (+ 3 4)                     (process time)
        -> (1+ (+ 2 4))             |
        -> (1+ (1+ (+ 1 4)))        |
        -> (1+ (1+ (1+ (+ 0 4))))   |
        -> (1+ (1+ (1+ 4)))         |
        -> (1+ (1+ 5))              |
        -> (1+ 6)                   |
        ------------------------->(process space)
        -> 7
        _________________________________________
        Linear Recursion Process
        time = O(x)
        space = O(x)

different shape of programs get different shape of processes.

intuition of change

* Fibonacci

        (DEFINE (FIB N)
            (IF (< N 2)
                N
                (+ (FIB (- N 1))
                   (FIB (- N 2)))))        
        _________________________________
        time = O(fib(n))
        space = O(n)

* Hanoi

三根柱子，起始柱子叫 FROM ，中间柱子叫 SPARE ，终点柱子叫 TO。简单的例子，假设有四个从大到小的盘子在 FROM 上面，最终要从大到小放在 TO 上面。规则是一次只能移动一个盘子。

假设现在有能力把前三个盘子放在 spare ，那么只要把第四个盘子放在 to 上，再把三个盘子放在 to 上就好了。

> Now, whether or not this is not obvious in any deep way that this works. And why? Now why is it the case that I can presume, maybe, that I can move the three-high tower. Well the answer is because I'm always counting down, and eventually I get down to zero-high tower, and a zero-high tower requires no moves.

```Lisp
( DEFINE (MOVE N FROM TO SPARE))
    (COND ((= N 0) 'DONE')
    (ELSE
        (MOVE (-1+ N) FROM SPARE TO)
        (PRINT-MOVE FROM TO)
        (MOVE (-1+ N) SPARE TO FROM)))
```

question: can you write an iterative algorithm rather than a recursive algorithm for doing this?