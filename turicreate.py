
import turicreate as tc
dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00529/diabetes_data_upload.csv"
df = tc.SFrame(dataset_url)
feature_names =  df.column_names()[:-1]
train_data,test_data = df.random_split(0.75)
logistic_model = tc.logistic_classifier.create(train_data,target='class',features=feature_names)
logistic_model.summary()
logistic_model.evaluate(test_data)
sf = {'Age': 41,
 'Alopecia': 'Yes',
 'Gender': 'Male',
 'Genital thrush': 'No',
 'Irritability': 'No',
 'Itching': 'Yes',
 'Obesity': 'No',
 'Polydipsia': 'No',
 'Polyphagia': 'Yes',
 'Polyuria': 'Yes',
 'class': 'Positive',
 'delayed healing': 'Yes',
 'muscle stiffness': 'Yes',
 'partial paresis': 'No',
 'sudden weight loss': 'No',
 'visual blurring': 'No',
 'weakness': 'Yes'}
logistic_model.save('diabetes_prediction.model')
logistic_model = tc.load_model("diabetes_prediction.model/")
prediction1 = tc.SFrame({'data':[sf.values()]})
logistic_model.predict(prediction1)
logistic_model.classify(prediction1)
