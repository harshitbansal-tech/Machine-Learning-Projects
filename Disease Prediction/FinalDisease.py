def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn import svm
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import LinearSVC

train_data = pd.read_csv("Training.csv")

data_train_x = train_data.drop(columns = ['prognosis', 'Unnamed: 133'], axis = 1)
data_train_y = train_data['prognosis']

test_data = pd.read_csv("Testing.csv")
data_test_x = train_data.drop(columns = ['prognosis', 'Unnamed: 133'], axis = 1)
data_test_y = train_data['prognosis']

column_names = data_train_x.columns
column_names_array = column_names.to_list()

patient_disease=[]
for i in range(0,len(column_names_array)):
    patient_disease.append(0)

svm = LinearSVC(random_state=42)
model = BaggingClassifier(base_estimator=svm, n_estimators=31, random_state=314)
model.fit(data_train_x, data_train_y)

y_pred = model.predict(data_test_x)

from sklearn.metrics import accuracy_score
accsc = accuracy_score(data_test_y, y_pred)

def finding_patient_disease():
    symtoms_patient_list = []
    for i in range(0,5):
        symtom_patient = str(input('Enter Sym'))
        symtoms_patient_list.append(symtom_patient)
    symptoms_index_p = []
    for i in range(0, 5):
        search_string = symtoms_patient_list[i]
        try:
            index = column_names_array.index(search_string)
            symptoms_index_p.append(index)
        except ValueError:
            print(f"'{search_string}' not found in the list")
    for i in range(0,5):
        new_value = 1
        index_to_change = symptoms_index_p[i]

        if 0 <= index_to_change < len(patient_disease):
            patient_disease[index_to_change] = new_value
        patient_df = pd.DataFrame(patient_disease)
        reshaped_array = patient_df.values.reshape(1, -1)
        reshaped_df = pd.DataFrame(reshaped_array)
    disease_of_patient = model.predict(reshaped_df)
    print(disease_of_patient)

finding_patient_disease()