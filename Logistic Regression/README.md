# Logistic Regression

<h1>Estimation</h1>

y = wx + b

<h1>Calculating Error</h1>

MSE = J(w,b) 

<h1>Gradient Descent</h1>

Calculate at a point where we have our parameter value, and which direction to go, to determine the global cost minimum, which have the lowest Mean Square Error(MSE).

The learning rate helps us get to the lowest Mean Square Error at an optimal amount of time.

<h1>Steps</h1>

<h2 style="font-weight: bold">Training:</h2>
<ul>
    <li>Initialize weight as zero.</li>
    <li>Initialize bias as zero</li>
</ul>

<h2 style="font-weight: bold">Given a data point</h2>
<ul>
    <li>Predict result by using y = wx + b</li>
    <li>Calculate Error</li>
    <li>Use gradient descent to figure out new weight and bias values</li>
    <li>Repeat n times</li>
</ul>

<h2 style="font-weight: bold">Testing:</h2>
Given a data point:
<ul>
    <li>Put in the values from the data point into the equation y = wx + b</li>
</ul>


