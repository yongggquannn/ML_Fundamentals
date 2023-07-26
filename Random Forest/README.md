# Random Forest

## Steps

### Training:
Given the whole dataset:
<ul>
    <li> Get a subset of the dataset</li>
    <li> Create a decision tree</li>
    <li> Repeat for as many times as the number of trees</li>
</ul>

### Testing:
Given a data point:
<ul>
    <li> Get the predictions from each tree</li>
    <li> Classification: hold a majority vote</li>
    <li> Regression: get the mean of the predictions</li>
</ul>
