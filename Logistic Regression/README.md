# Logistic Regression

## Estimation

Refer to Estimation.png

## Calculating Error (Cross-Entropy)

Refer to Calculating Error.png

## Gradient Descent

Calculate at a point where we have our parameter value, and which direction to go, to determine the global cost minimum, which have the lowest Mean Square Error(MSE).

The learning rate helps us get to the lowest Mean Square Error at an optimal amount of time.

## Steps

### Training:
<ul>
    <li>Initialize weight as zero.</li>
    <li>Initialize bias as zero</li>
</ul>

### Given a data point:
<ul>
    <li>Predict result by using y = wx + b</li>
    <li>Calculate Error</li>
    <li>Use gradient descent to figure out new weight and bias values</li>
    <li>Repeat n times</li>
</ul>

### Testing:
Given a data point:
<ul>
    <li>Put in the values from the data point into the equation y =  1 / (1 + e^(-wx + b))</li>
    <li>Choose the label based on the probability</li>
</ul>