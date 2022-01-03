import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.arange(5)
accuracy = [65.1,59.95,30.44,35.75,32.86]
f1 = [57.65,53.04,24.83,26.34,18.58]
precision = [59.29,53.91,24.83,27.98,23.19]
recall = [59.9,54.98,25.57,28.66,18.58]
width = 0.2
  
# plot data in grouped manner of bar type
plt.bar(x-0.2, accuracy, width, color='cyan')
plt.bar(x, f1, width, color='orange')
plt.bar(x+0.2, precision, width, color='green')
plt.bar(x+0.4, recall, width, color='red')
plt.xticks(x, ['BERT','Proposed Model','  ML Mode','LSTM','KNN'])
plt.xlabel("Metrics")
plt.ylabel("Scores")
plt.legend(["Accuracy","Macro-F1","Macro-Precision","Macro-Recall"])
plt.show()
