import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.arange(5)
accuracy = [77.6,50.35,47.7,52.06,50.66]
f1 = [83.2,62.1,44.02,60.23,59.59]
precision = [78.1,59.2,66.25,62.33,60.84]
recall = [88.9,65.2,32.96,58.27,58.40]
width = 0.2
  
# plot data in grouped manner of bar type
plt.bar(x-0.2, accuracy, width, color='cyan')
plt.bar(x, f1, width, color='orange')
plt.bar(x+0.2, precision, width, color='green')
plt.bar(x+0.4, recall, width, color='red')
plt.xticks(x, ['BERT','LSTM','Random Forest','SVC','Logistic Regression'])
plt.xlabel("Metrics")
plt.ylabel("Scores")
plt.legend(["Accuracy","Macro-F1","Macro-Precision","Macro-Recall"])
plt.show()
