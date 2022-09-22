# Sample application to block abusive and hate speech on Teams channel - Project is built for Microsoft hacathon 2022

## The use of application like Teams, Zoom  etc is increasing day by day. To mitigate the misuse of these application its high time to block any abusive or hate speech over these channels. This application is a small step on the same direction so that we can make our workspace more inclusive and safe for all of us.

To detect hatespeech I have used three different datasets available on kaggle (twitter hate speech datasets).
After merging the combined dataset has more than 15,000 records.

After cleaning and data preprocessing I have used SVC algorithm on top of the dataset.
SVC gave an accuracy of 90%, which is okay . But we need more complex modelling on the dataset (xgboost, deep learning) as a future scope.

After training the model , created a flask app and UI to use the trained model to block the hatespeech, as shown in the below image.

To run the project, clone it in your system , run the app.py file and you are good to test this hatespeech prediction/blocking chat app in your system.

![image](https://user-images.githubusercontent.com/52891188/191776694-01f7603b-e284-4f68-b473-6af8fb65a369.png)
