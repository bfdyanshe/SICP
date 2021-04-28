
$\sum\limits_{i=a}^bi$  的 lisp 代码，用递归的思想。
```Lisp
(DEFINE (SUM-INT A B)
    (IF (> A B)
        0
        (+ A 
            (SUM-INT (1+ A) B))))
```

$\sum\limits_{i=a}^b i^{2}$
```Lisp
(DEFINE (SUM-SQ A B)
    (IF (> A B)
        0
        (+ (SQUARE A)
            (SUM-SQ (1+ A) B))))
```

> Now, wherever you see yourself writing the same thing down more than once, there's something wrong, and you shouldn't be doing it. And the reason is not because it's a waste of time to write something down more than once. It's because there's some idea here, a very simple idea, which has to do with the sigma notation not depending upon what it is I'm adding up. (西格玛 ∑ 标记并不依赖于我要求和的内容) And I would like to be able to-- always, whenever trying to make complicated systems and understand them, is's crucial to divide the things up into as many pieces as I can, each of which I understand separately.


PI-SUM: $\sum_{i=a_{by 4}}^b \frac{1}{i(i+2)}$ 
大致是：$\frac{1}{1*3}+\frac{1}{5*7}+\frac{1}{7*9}...$ 这样
```Lisp
(define (pi-sum a b)
    (if (> a b)
        0
        (+ (/ 1 (* a (+ a 2)))
            (pi-sum (+ a 4) b))))
```

# general pattern
> not only do you know something like that, but you give the knowledge of that a name.  

根据以上代码的形式，可以总结一个西格玛 ∑ 标记的抽象代码：
```Lisp
(define (fun a)
    (/ 1 (* a (+ a 2))))

(define (step a)
    (+ a 4))

(define (sigma a b)
    (if (> a b)
        0
        (+ (fun a)
            (sigma (step a) b)))))
```

这是 general pattern：
```Lisp
(DEFINE (SUM TERM A NEXT B)
    (IF (> A B)
        0
        (+ (TERM A)
            (SUM TERM 
                 (NEXT A)
                 NEXT
                 B))))
```

现在用 general pattern 改写上面的程序：
```Lisp
(DEFINE (SUM-INT A B)
    (DEFINE (IDENTITY X) X)  //这里的 x 是 IDENTITY 的形参，和外面的参数不冲突
    (SUM IDENTITY A 1+ B))

(DEFINE (SUM-SQ A B)
    (SUM SQUARE A 1+ B))

(DEFINE (PI-SUM A B)
    (SUM (LAMBDA(I) (/ I (* I (+ I 2)))) 
         A
         (LAMBDA(I) (+ I 4))
         B))
```

迭代方法：
```Lisp
(define (SUM TREM a NEXT b)
    (define (ITER j ans)
        (if (> j b)
            ans
            (ITER (NEXT j)
                  (+(TERM j) ans))))
    (ITER a 0 ))
```

> computers to make people happy, not people to make computers happy.

heron of alexandria 的求平方根方法：
```Lisp
(define (sqrt x)
    (define tolerance 0.00001)
    (define (good-enuf? y)
        (< (abs (- (* y y) x)) tolerance))
    (define (improve y)
        (average (/ x y) y))
    (define (try y)
        (if (good-enuf? y)
            y
            (try (improve y))))
    (try 1))
```
> But what's the real idea? Can we make it clear what the idea is?

求平方根就是找不动点: Look for a Fixed-Point
这里有求平方根的函数：
$f(y)=\frac{y+\frac{x}{y}}{2}$ 很显然 $f(\sqrt{x})=\sqrt{x}$

```Lisp
(DEFINE (SQRT X)
    (FIXED-POINT
        (LAMBDA(Y)(AVERAGE(/ X Y) Y))
        1))

(DEFINE (FIXED-POINT f START)
    (DEFINE (ITER OLD NEW)
        (IF (CLOSE-ENUF? OLD NEW)
            NEW
            (ITER NEW (f NEW))))
    (ITER START (f START)))
```
> SQRT X means The square root of X   
> 
找不动点的 general pattern：
```Lisp
(define (fixed-point f start)
    (define tolerance 0.00001)
    (define (close-enuf? u v)
        (< (abs (- u v)) tolerance))
    (define (iter old new)
        (if (close-enuf? old new)
            new
            (iter new (f new))))
    (iter start (f start)))
```

## a procedure which produces a procedure as its value

Higher-Order Procedure

>average damp is a special procedure, that's going to take a procedure as its argument and return a procedure as its value.

```Lisp
(DEFINE (SQRT X)
    (FIXED-POINT
        (AVERAGE-DAMP (λ(y)(/ x y)))
        1))

(DEFINE AVERAGE-DAMP
    (λ(f)
        (λ(X)(AVERAGE((f X) X)))))

注意：f 是 average-damp 的形参，
     而 X 是 average-damp 返回的 procedure 
    （即第二个 λ 的形参）

average-damp 的另一个写法
(DEFINE (AVERAGE-DAMP f)
    (λ(X)(AVERAGE((f X) X))))

两种写法是一样的，但是第一种写法更加强调了
 average-damp 也是一个 procedure。
 所以 average-damp 是一个接收一个 procedure 为参数
 返回一个 procedure 的 procedure。
```

--------------------
## Newton's method
a method for finding the roots of the function $f$.
sometime, when it converges, it does so very fast.
And sometimes, it doesn't converge, and we have to do something else.

to find a y such that 
$f(y)=0$
start with a guess, $y_0$
$y_{n+1}=y_n-\frac{f(y_n)}{\frac{df}{dy}|_{y=y_n}}$

> 首先有 A 点 $(y_n,f(y_n))$, $y_n$ 是随意猜的一个值
> 在 A 点上做 $f$ 的切线 $f(y_n)+f'(y_n)(y_{n+1}-y_n)$
> 然后这个在 A 点上近似 $f$ 的切线的根（即零点）会比 A 点更接近 $f$ 的根
> 所以这个更近的点是 $y_{n+1}=y_n-\frac{f(y_n)}{f'(y_n)}$

* wishfull thinking, topdown programing

假设 Newton Method 已经被实现，那么用 NM 求平方根就要输入 $f$ 和 guess value $y_n$，代码如下所示：
```Lisp
(DEFINE (SQRT X)
    (NEWTON (λ(Y)(- X (SQUARE Y)))
            1))
```
> SQRT X means The square root of X   

然后需要一个过程（procedure）来计算出函数（function）的导数，这个函数由给出的过程 f 来计算。所以函数和过程是两个概念。

```Lisp
(DEFINE (NEWTON f guess)
    (DEFINE DF (DERIVE f))
    (FIXED-POINT
        (λ(X)(- X (/ (f X)(DF X))))
        guess))
```

然后再实现这个求导的过程 DRIVE ，其以一个 procedure 为参数，然后返回一个 procedure。
求导：$df=\frac{f(x+dx)-f(x)}{dx}$
```Lisp
(DEFINE DERIVE
    (λ(f)
        (λ(X)
            (/ (- (f (+ X dX)) 
                  (f X)) 
               dX))))

(DEFINE dX 0.00001)
```


> DF means the derivative of f

> procedures compute functions

> The rights and privileges of first-class citizens -- by Chris Strachey
> 
> * To be named by variables.
> * To be passed as arguments to procedures.
> * To be returned as values of procedures.
> * To be incorporated into data structures.
   