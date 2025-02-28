"""
Train a naive Bayes classifier for only continuous features.
->
Use a Gaussian naive Bayes classifier in Scikit-Learn.

Warning:
- Prior probabilities can be too small to change non-calibrated extreme predicted probabilities
https://github.com/scikit-learn/scikit-learn/issues/29648

The Gaussian naive Bayes classifier is best used in cases of all continuous features.
The likelihood of the feature values $x_j$, given an observation of class $y$,
follows a normal distribution:
$$
p(x_j | y) = 1 / \sqrt{ 2 \pi \sigma_{x_jy}^2 } \exp{ -(x_j - \mu_{x_jy})^2 / (2 sigma_{x_jy}^2) }
$$,
where $\sigma_{x_jy}^2$ and $\mu_{x_jy}$ are the variance and mean of $x_j$ for $y$.

Then
$$
P(y | observations) ~ P(observations | y) P(y) = \prod_{observation} P(observation | y) P(y) \\
~ \prod_{observation} \prod_{x_j} P(y) \int_{x_j} p(x_j | y) dx_j
$$.
The formula will be logarithmed.

Notice:
Predicted probabilities obtained by "predict_proba" is are not calibrated.
->
That is, they should not be believed.

See also:
- How Naive Bayes classifier algorithm works in machine learning
https://dataaspirant.com/naive-bayes-classifier-machine-learning/
"""
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB

# Load data
iris = datasets.load_iris()
features = iris.data
target = iris.target

# Create Gaussian naive Bayes
classifer = GaussianNB()  # The prior is adjusted based on the data
# Train model
model = classifer.fit(features, target)
# Create new observation
new_observation = [[5.2, 3.6, 1.5, 0.3]]
# Predict class
model.predict(new_observation)
# array([0])

# Non-calibrated predicted probabilities are too extreme
# and cannot be changed by "GaussianNB(priors=...".
model.predict_proba([[5.2, 3.6, 1.5, 0.3]])
# array([[1.00000000e+00, 6.06941525e-17, 3.10259941e-24]])

# Set prior probabilities P(y) of each class of 3
clf = GaussianNB(priors=[1e-12, 1-1e-11, 9e-12])
# Train model
model_priors = clf.fit(features, target)
# Create new observation
new_observation = [[5.2, 3.6, 1.5, 0.3]]
# Predict class
model_priors.predict(new_observation)
# array([0])

# also
clf.predict(new_observation)
# array([0])
