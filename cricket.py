wheather=['sunny','sunny','overcast','Rainy','Rainy','Rainy','overcast','sunny','sunny','Rainy','sunny','overcast','overcast','Rainy']
temp=['Hot','Hot','Hot','mild','cool','cool','cool','mild',',mild','mild','Hot','mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
wheather_encoded=le.fit_transform(wheather)
print (wheather_encoded)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print("Temp:",temp_encoded)
print("play:",label)
features=list(zip(wheather_encoded,temp_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(features,label)
print(sunny-2,overcast-1,Rainy-0)
print(hot-2,cool-1,mild-0)
a=int(input("enter the value for wheather"))
b=int(input("enter the value for temprature"))
predicted= model.predict([[a,b]]) # 0:Overcast, 2:Mild                        
print("Predicted Value:", predicted)

