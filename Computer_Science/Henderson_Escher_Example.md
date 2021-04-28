
```Lisp
向量
(define make-vector cons)
(define xcor car)
(define ycor cdr)

线段
(define make-seg cons)
(define seg-start car)
(define seg-end cdr)

(make-seg (make-vector 2 3)
          (make-vector 5 1))
```
> prodedures can be objects, and that you can name them.

>the set of data objects in Lisp is closed under the operation of forming pairs. That is **pairs in pairs**.
>**combination close** -- closure -- Lisp的闭包

# List
> for representing a sequence of things as, essentially, a chain of pairs, and that's called a List.

> **nil** is a name for the end of List marker.

```Lisp
(list 1 2 3 4)
即
(cons 1
        (cons 2
                (cons 3
                        (cons 4))))

(define 1-TO-4 (list 1 2 3 4))
__________________________________
(car (cdr 1-TO-4))  -> 2
1-TO-4              -> (1 2 3 4)
(cdr 1-TO-4)        -> (2 3 4)

如何实现 (scale-list 10 1-TO-4) -> (10 20 30 40)

CDR-ing down a list
(define (scale-list s l)
    (if (null? l)
        nil
        (cons (* (car l) s)
              (scale-list s (cdr l)))))
```

## higher-order MAP
接收一个 procedure 和一个 list，对 list 里的每个元素执行接收的 procedure。
```Lisp
(define (map p l)
    (if (null? l)
        nil
        (cons (p (car 1))
              (map p (cdr l)))))
```
map 就是 scale-list 的 higher-order 模式。
```Lisp
(define (scale-list s l)
    (map (λ(x)(* x s)) 
         l))
```

> see, once you say scale is just MAP, you stop thinking about whether it's iterative or recursive, and you just say, well there's this aggregate, there's this List, and what I do is transform every item in the List. and I stop thinking about the particular control structure in order.
> 
> Stop thinking about control structures, and you start thinking about operations on aggregates.

for-each 和 map 类似，但是不会创建新的集合
```Lisp
(define (for-each proc list)
    (cond ((null? list) "done")
        (else (proc (car list))
              (for-each proc
                        (cdr list)))))
```
这两个代码相似，但是这个 map 是一个递归过程（也可以有不递归的形式）因为要等待返回值。而这个 for-each 不是，因为没有等待返回值。

---------------------------------------------------------------------------

* List structure
* issues of abstraction
* representation
* capturing commonality (描绘共性) with higher order procedures
* meta-linguistic abstraction

# Peter Henderson

一门专门用来画递归图形的语言。

primitive object -- **picture**

> procedure is data, data is procedure

> layer language

