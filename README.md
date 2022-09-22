# Hate Speech detection

To detect hatespeech I have used three different dataset available on kaggle (twitter hate speech datasets).
After merging the comboned dataset has more than 15,000 records.

After cleaning and data preprocessing I applied SVC algorithm on top of the dataset.
SVC gave an accuracy of 90%, which is okay, need to be more complex modelling on the dataset (xgboost, deep learning) as a future scope.

After training the model , create a flask app and UI to use the trained model to block the hatespeech, as shown in the below image.

To run the project, clone it in your system , run the app.py file and you are good to test this hatespeech prediction chat in your system.

![image](https://user-images.githubusercontent.com/52891188/191776694-01f7603b-e284-4f68-b473-6af8fb65a369.png)
