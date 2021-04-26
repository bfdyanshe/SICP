> basic technique for controlling complexity

* black-box abstraction.
* conventional interfaces
* making new languages

# 1. black-box

**imperative knowledge** 指令性知识

> Just like I could make a box that says "square root."
> And I'd like to be able to express this in my language.
> So I'd like to express not only the imperative how-to knowledge of a particular thing like square root.
> but I'd like to be able to express the imperative knowledge of how to do a general thing like how to find fixed point.
> 

> use my language to define a box that says "fixed point", just like I could make a box that says "square root". And I'd like to be able to express this in my language.

> there's another piece of imperative knowledge which says, one way to compute square root is to apply this general fixed point method.

> See, not only is this a piece of imperative knowledge, how to find a fixed point, there's another piece of imperative knowledge which says, one way to compute square root is to apply this general fixed point method. 
> So I'd like to also be able to express that imperative knowledge. What that would that look like? That would say, this fixed point box is such that, if I input to it the function that takes Y to the average of Y and X/Y, then what should come out of that fixed point box is a method for finding square roots.

> this is a procedure, will end up being a procedure, as we'll see, whose value is another procedure, the reason we want to do that is because **procedures are going to be our ways of talking about imperative knowledge.** And the way to make that very powerful is to be able to talk about other kinds of knowledge. **So here is a procedure that, in effect, talks about another procedure, a general strategy that it self talks about general strategies.**

## BLACK-BOX ABSTRACTION

* **PRIMITIVE OBJECTS**

        primitive procedures
        primitive data

* **MEANS OF COMBINATION**

        procedure composition
        construction of compound data

* **MEANS OF ABSTRACTION**

        procedure definition
        simple data abstraction

* **CAPTURING COMMON PATTERNS**

        high-order procedures
        data as procedures

> as we go further and further on and become more abstract, the line between what we consider to be data and what we consider to be procedures is going to blur at an incredible rate.

# conventional interfaces (通用接口)

* generic operations
* large-scale structure and modularity
* object-oriented preogramming
* operations on aggregates

# Meta-linguistic Abstraction (元语言抽象)

apply-eval loop (应用-求值循环) and build Lisp

* interpretation apply-eval
* example-logic programming
* register machines