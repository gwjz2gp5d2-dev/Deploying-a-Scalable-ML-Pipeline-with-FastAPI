# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a Random Forest classifier developed to predict whether an individual's annual income is greater than 
$50,000 using information from the Census Income dataset. The model was implemented using 
scikit-learn with n_estimators=100 and a fixed random state of 42 to support reproducibility. 
Categorical features were transformed using one-hot encoding before training. The trained model and categorical 
encoder were saved as pickle files for later use in the FastAPI application.

## Intended Use
This model is intended to demonstrate the development and deployment of a machine learning classificaton model using
census income data. It predicts whether an individual's annual income is greater than $50,000 based on demographic and
employment metrics. The model is designed for educational purposes, including evaluating model performance and serving 
predictions through a FastAPI application. It is not intended for real-world use or decisions that could directly 
affect individuals.

## Training Data
The model was trained using the Census Income dataset, which contains 32,561 records with demographic and employment 
information. The dataset was divided into 80% training data and 20% testing data using a stratified split to preserve
the proportions of the two income categories. Categorical features were converted into numerical features using one-hot
encoding. The salary labels were converted into binary values using a LabelBinarizer.

The dataset also contained missing information represented by question marks (?) in the workclass, occupation, and 
native-country columns. These values were retained and treated as separate categories during preprocessing rather than 
removing the affected records.

## Evaluation Data
Evaluation was done on the 20% of the Census Income dataset that was not used during training. Predictions were 
compared against actual salary labels to measure overall model performance. Additional evaluations were performed 
on individual categorical groups to identify differences in predictive performance.

## Metrics
The model was evaluated using precision, recall, and F1 score on the testing dataset. The model achieved a 
precision of 0.7327, recall of 0.6397, and F1 score of 0.6830. These results indicate that the model identifies 
approximately 64% of individuals earning over $50,000, with approximately 73% of its positive predictions being correct.

## Ethical Considerations
The model uses demographic information, including race, sex, and marital status, which could introduce or reinforce 
biases present in the historical census data. Differences in model performance across demographic groups may lead to 
inaccurate or unequal predictions for certain individuals. Because of these concerns, the model should be used for 
educational purposes only and not for decisions involving employment, lending, or other situations that could 
negatively affect individuals.

## Caveats and Recommendations
The dataset contains missing information, question marks (?), which were retained as separate categories and may affect
the model's predictions. Model performance also varied across categorical groups, with some groups showing substantially
lower F1 scores than others. Results for categories with very few observations may be unreliable. Future improvements 
could explore alternative methods for handling missing values, evaluate model performance across demographic groups,
and use additional data to improve reliability.