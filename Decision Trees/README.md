# Decision Trees

## What needs to be decided on? 

Refer to Decision.png

## Steps

### Training:
Given the whole dataset:
<ul>
    <li>Calculate information gain with each possible list</li>
    <li>Divide set with that feature and value that gives the most IG</li>
    <li>Divide tree and do the same for all created branches</li>
    <li>...until a stopping criteria is reached</li>
</ul>

### Testing:
Given a data point:
<ul>
    <li>Follow the tree until you reach the leaf node</li>
    <li>Return the most common class label</li>
</ul>

## Terms
Refer to Terms.png for the formula of the respective terms.

Information gain is the basic criterion to decide whether a feature should be used to split a node or not. 

Entropy is a measure of disorder or impurity in a node. Thus, a node with more variable composition, such as 2 Pass and 2 Fail would be considered to have higher Entropy than a node which has only pass or only fail.





