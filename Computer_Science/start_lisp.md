* primitive elements
* means of combination - ways put primitive elements together
* means of abstraction - take hose complicated things and draw those boxes around them

how to build a thing, how to abstract a thing.

"3" is a representation of 3.  "operands"运算对象

"+" is a concept of how you add things. "operator"运算符

this is primitive elements.

combination: (+ 3 17.4 5) = 25.4

## abstruct in Lisp

``` Lisp
    e.g.
    1. (define A (* 5 5))
    2. (define B (+ A 5))
    3. (define (square x) (* x x))
    4. (define square (lambda (x) (* x x)))  //lambda: make a procedure. No.3 是 lambda 的语法糖 syntactic sugar
```
``` Lisp
    对x开根号

    (define (improve guess x)
        (average guess (/ x guess)))

    (define (goog-enough? guess x)
        (< (abs (- (square guess) x)) 0.001))

    (define (try guess x)
        (if (good-enough? guess x)
            guess
            (try (improve guess x) x)))
    
    (define (sqrt x) (try 1 x))
```


question: 

(define A (* 5 5)) 和 (define (A) (* 5 5)) 有什么区别？

前者是定义了一个primitive elements, 而后者是定义了一个procedure，这个procedure和 + ，square 一样，只是没有参数。

如果问Lisp第一个A是什么，Lisp会回答 25，如果问第二个A是什么，Lisp会回答compound-procedure。但是如果对于第二个A问Lisp （A）是什么，Lisp会回答是25 。而对于第一个 A 问 Lisp （A）是什么，Lisp会返回一个错误，因为第一个A不是一个procedure。