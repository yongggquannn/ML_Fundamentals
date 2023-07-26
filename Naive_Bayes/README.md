# Naive Bayes

The Naive Bayes classifier is a "probabilistic classifier" based on applying Bayes' theorem with strong (naive) independence assumptions between the features.

<img src="Naive_Bayes/assets/Bayes'_Theorem.png" width ="500" height="500"> 

<img src="Naive_Bayes/assets/Independent.png" width ="500" height="500"> 

<img src="Naive_Bayes/assets/Posterior_Probability.png" width ="500" height="500"> 

<img src="Naive_Bayes/assets/Conditional.png" width ="500" height="500"> 

## Steps

### Training: 
<ul>
    <li> Calculate mean, var, and prior (frequency) for each class</li>
</ul>

### Predictions:
<ul>
    <li> Calculate posterior for each class with log formula(Refer to image) and Gaussian Formula.</li>
    <li> Choose the class with the highest posterior probability</li>
</ul>


