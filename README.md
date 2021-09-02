# HASOC 2021

https://hasocfire.github.io/hasoc/2021/important_dates.html

Offensive and problematic content including insulting, hurtful, derogatory or obscene user contributions are pervasive in social media. Societies need to develop adequate response mechanisms in order to find a balance between freedom of expression on one side and the ability to live without oppressive remarks on the other side. A requirement for any response is robust technology for identifying problematic content automatically. HASOC provides a forum for developing and testing text classification systems for various languages
  
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
KNN | 78%
SVC | 84%
Random Forest  | 82%
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
KNN | 64%
SVC | 66%
Decision Tree | 53%
Random Forest  | 69%
LSTM | 60%
BERT  | 61%
Proposed Model  | 63%

### Proposed Model:
<img width="500px" src="https://user-images.githubusercontent.com/68152189/131232896-2c644a64-13e0-4d8c-a1dc-5b5b7adc2ea6.png">

Model | Accuracy
------------- | -------------
BERT_A  | 78%
BERT_OFFN/HATE  | 79% (2 epochs)
Profanity  | 92%


## Results


Sub-Task    |     Classifier      |   Macro F1-score   | Place in leaderboard 
------------|---------------------|--------------------|--------------------
A  | BERT | 83% | 24
B  | BERT | 57% | 13


## Files: 

* <a href="./Preprocess.ipynb"> Preprocess.ipynb </a> : Preprocessing the data.
* <a href="./dataAnalysis.ipynb"> dataAnalysis.ipynb </a> : Analysing the data.
* <a href="./Subtask A/ml_techniques_A.ipynb">ml_techniques_A.ipynb </a> : Applying ML models to classify the data and find the accuracy for Subtask A.
* <a href="./Subtask B/ml_techniques_B.ipynb">ml_techniques_B.ipynb </a> : Applying ML models to classify the data and find the accuracy for Subtask B.
* <a href="./Subtask A/DL_LSTM for task A.ipynb">DL_LSTM for task A.ipynb </a> : Applying DL LSTM model to classify the data and find the accuracy for Subtask A.
* <a href="./Subtask B/DL_LSTM for task B.ipynb">DL_LSTM for task B.ipynb </a> : Applying DL LSTM model to classify the data and find the accuracy for Subtask B.
* <a href="./Subtask A/BERT_A.ipynb">BERT_A.ipynb</a> : Applying BERT model to classify the data and find the accuracy for Subtask A.
* <a href="./Subtask B/BERT_B.ipynb">BERT_B.ipynb</a> : Applying BERT model to classify the data and find the accuracy for Subtask B.
* <a href="./Subtask B/Proposed Model">Proposed Model (Folder)</a> : Files related to the Proposed Model:
  * <a href="./Subtask B/Proposed Model/Profanity_Check.ipynb">Profanity_Check.ipynb</a> : Survey of various pre-trained models/libraries for profanity check.
  * <a href="./Subtask B/Proposed Model/ProposedModel.ipynb">ProposedModel.ipynb</a> : Implementation of the proposed model.
