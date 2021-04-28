* build a layered system

**abstraction boundary** 抽象屏障。在 SQRT 和 GOOD-ENUF 之间就有一种 abstraction boundary，SQRT 不管 GOOD-ENUF 是如何运行的，只要不出问题。GOOD-ENUF 也不管 SQRT 要用自己做什么。

**numerator** 分子，**denominator** 分母，**rational number** 有理数

**constructor** 构造函数，**selector** 选择函数

> programming language to express the concepts that we have in our heads

## List Structure

### pairs 

```Lisp
(cons x y)
    constructs a pair whose first part is x and whose second part is y

(car p)
    selects the first part of the pair p

(cdr p)
    selects the second part of the pair p

for any x and y
    (car (cons x y)) is x
    (cdr (cons x y)) is y
```

* Box and Pointer notation
    | x   | y   |
    | --- | --- |



## data abstraction 
> a method for controlling complexity

例子：构建有理数如 $\frac{1}{4}, \frac{3}{5}...$

```Lisp
(define (make-rat a b)
    (cons a b))

(define (numer n)
    (car n))

(define (denom n)
    (cdr n))

or

(define (make-rat a b)
    (let ((g (gcd a b)))
        (cons (/ a g)
              (/ b g))))

// gcd 是一个求最大公因数的 procedure
// let 和 define 类似并会建立一个子代码块

// 再实现对有理数的加减乘除

(define (*rat a b)
    (make-rat (* (numer a) (numer b))
              (* (denom a) (denom b))))

(define (+rat a b)
    ......)

(define (-rat a b)
    ......)
```

make-rat, numer, denom 作为抽象层，用 pairs 抽象出了有理数。
而 +rat, *rat, -rat 是对有理数的操作，使用层。
有理数使用 pairs 来表示的，所以 pairs 在这里是 representation ，表示层。
这样，有理数这个抽象的使用层和表示层做到了分离。这就是数据抽象。


* closure 闭包
    >make pairs of pairs


## pure abstraction 
从虚无中构建出 pair

```Lisp
(define (cons a b)
    (λ (pick)
        (cond ((= pick 1) a)
              ((= pick 2) b))))

(define (car n)(n 1))
(define (cdr n)(n 2))
```

> blurring this traditional line between what you consider a procedure and what you consider data

所以之前构建的有理数，实际上是一个 procedure 。