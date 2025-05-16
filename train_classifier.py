import pickle

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data_dict=pickle.load(open('./data.pickle','rb'))
print(data_dict.keys())
print(data_dict)

data=np.asarray(data_dict['data'])
labels=np.asarray(data_dict['labels'])

x_train,x_test,y_train,y_test= train_test_split(data,labels,test_size=0.25,shuffle=True,stratify=labels)

model= RandomForestClassifier()
model.fit(x_train,y_train)

x_predict =model.predict(x_test)

score= accuracy_score(x_predict,y_test) 

print('{}% of samples were classified correctly !'.format(score*100))
#81.81818181818183% of samples were classified correctly !
#72.72727272727273% of samples were classified correctly !
#75.0% of samples were classified correctly !
#95.23809523809523% of samples were classified correctly !
#{'23', '21', '5', '14', '0', '10', '1', '18', '9', '15', '6', '12', '7', '8', '16', '11', '17', '24'}

#100.0% of samples were classified correctly !
#{'8', '17', '12', '16', '15', '6', '11', '13', '21', '25', '1', '24', '0', '10', '9', '14', '5', '19', '23', '7', '2', '18'}
#A B C F G H I J K L M N P Q R S T U W Y Z O

f=open('model.p','wb')
pickle.dump({'model':model},f)
f.close()

print(set(labels))  # labels من data.pickle


"""Way1
print(data_dict.keys())
print(data_dict)
"""