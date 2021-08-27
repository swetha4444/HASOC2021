# HASOC 2021

https://hasocfire.github.io/hasoc/2021/important_dates.html

### Files: 

* <a href="./Preprocess.ipynb"> Preprocess.ipynb </a> : Preprocessing the data.
* <a href="./dataAnalysis.ipynb"> dataAnalysis.ipynb </a> : Analysing the data.
* <a href="./Subtask A/ml_techniques_A.ipynb">ml_techniques_A.ipynb </a> : Applying ML models to classify the data and find the accuracy for Subtask A.
* <a href="./Subtask B/ml_techniques_B.ipynb">ml_techniques_B.ipynb </a> : Applying ML models to classify the data and find the accuracy for Subtask B.
* <a href="./Subtask A/DL_LSTM for task A.ipynb">DL_LSTM for task A.ipynb </a> : Applying DL LSTM model to classify the data and find the accuracy for Subtask A.
* <a href="./Subtask B/DL_LSTM for task B.ipynb">DL_LSTM for task B.ipynb </a> : Applying DL LSTM model to classify the data and find the accuracy for Subtask B.
* <a href="./Subtask A/BERT_A.ipynb">BERT_A.ipynb</a> : Applying BERT model to classify the data and find the accuracy for Subtask A.
* <a href="./Subtask B/BERT_B.ipynb">BERT_B.ipynb</a> : Applying BERT model to classify the data and find the accuracy for Subtask B.


## Sub-task A: Identifying Hate, offensive and profane content
This task focus on Hate speech and Offensive language identification offered for English, German, and Hindi. Sub-task A is coarse-grained binary classification in which participating system are required to classify tweets into two classes, namely: Hate and Offensive (HOF) and Non- Hate and offensive (NOT).

* NOT :
Non Hate-Offensive - This post does not contain any Hate speech, profane, offensive content.
* HOF :
Hate and Offensive - This post contains Hate, offensive, and profane content.

Model | Accuracy
------------- | -------------
Gaussian NM  | 50%
Logistic Regression  | 80%
KNN | 76%
SVC | 79%
Decision Tree | 71%
Random Forest  | 76.6%
LSTM | 78%
BERT  | 78%


## Sub-task B: Discrimination between Hate, profane and offensive posts
This sub-task is a fine-grained classification offered for English, German, and Hindi. Hate-speech and offensive posts from the sub-task A are further classified into three categories:

* HATE :
Hate speech:- Posts under this class contain Hate speech content.
* OFFN :
Offenive:- Posts under this class contain offensive content.
* PRFN :
Profane:- These posts contain profane words.

Model | Accuracy
------------- | -------------
Gaussian NM  | 45%
KNN | 56%
SVC | 67%
Decision Tree | 50%
Random Forest  | 66%
LSTM | 60%
BERT  | 61%

## Proposed Model
![Untitled drawing (1)](https://user-images.githubusercontent.com/68152189/131159936-57007383-56cd-4976-ac71-4af4f262fc8a.png)

