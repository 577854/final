import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

####### 
## Get the model trained in the notebook 
# `../nbs/ML-Oblig2-Copy3.ipynb`
#######

model = joblib.load('models/transfor&predict.joblib')


def preprocess(data):

    feature_values = {
        'age': 38,
        'workclass': '?',
        #'fnlwgt': 1,
        #'education': 'Some-college',
        'education': 10, 
        'maritalStatus': 'Married-civ-spouse',  
        #'occupation': 'Other-service ',
        'relationship': 'Husband',
        #'race': 'White', 
        'sex': 'Male',
        #'capital.gain': 1077,
        #'capital.loss': 87,
        'hoursPerWeek': 40,  
        'country': 'United-States'
    }

    print(data)
    # Parse the form inputs and return the defaults updated with values entered.

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        
        if key == 'country':
            feature_values[key] = convertCountry(data[key])    
        else:
            feature_values[key] = data[key]

    #test
    print(feature_values)
    #feature_values.__delitem__('education')
    #print(feature_values)
    #test

    return feature_values

def convertCountry(dataKey):
    switcher = {
        True: 'United-States',
        False: 'Not-US'
    }
    return switcher.get(dataKey, True)

####### 
## Now we can predict with the trained model:
#######

def predict(data):
    """
    If debug, print various useful info to the terminal.
    """
 
    # Store the data in an array in the correct order:

    column_order = ['age','workclass','education','maritalStatus',
                    'relationship','sex',
                    'hoursPerWeek','country']

    #data = np.array([data[feature] for feature in column_order], dtype=object)

    noNumColumn = ['workclass','marital.status','relationship','sex','native.country']
    numColumns = ['age','education.num','hours.per.week']
    data1 = pd.DataFrame(np.reshape(np.array([data[feature] for feature in column_order]), (1,8)), columns =  ['age','workclass','education.num','marital.status','relationship','sex','hours.per.week','native.country']) 
    
    for column in numColumns:
        data1[column] = data1[column].astype(int)
    
    print(data1.head())
    data = data1 #readyData(data1, noNumColumn)

    # NB: In this case we didn't do any preprocessing of the data before 
    # training our random forest model (see the notebool `nbs/1.0-asl-train_model.ipynb`). 
    # If you plan to feed the training data through a preprocessing pipeline in your 
    # own work, make sure you do the same to the data entered by the user before 
    # predicting with the trained model. This can be achieved by saving an entire 
    # sckikit-learn pipeline, for example using joblib as in the notebook.
    
    pred = model.predict(data) #.reshape(1,-1))

    uncertainty = model.predict_proba(data) #.reshape(1,-1))

    return pred, uncertainty


def postprocess(prediction):
    """
    Apply postprocessing to the prediction. E.g. validate the output value, add
    additional information etc. 
    """

    pred, uncertainty = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    try: 
        int(pred[0]) > 0
    except:
        pass

    # Make strings
    pred = str(pred[0])
    uncertainty = str(uncertainty[0])


    # Return
    return_dict = {'pred': pred, 'uncertainty': uncertainty}

    return return_dict


def scale(data):
    scaler = StandardScaler()
    scaler.fit(data)
    return pd.DataFrame(scaler.transform(data))
    
def lbEnc(data, nonNumCol):
    for column in nonNumCol:
        le = preprocessing.LabelEncoder()
        data[column] = le.fit_transform(data[column])

def combiner(data):
#    data['race'].replace(['Black', 'Asian-Pac-Islander','Amer-Indian-Eskimo'], 'Other', inplace=True)
#    data['marital.status'].replace(['Divorced', 'Widowed', 'Separated', 'Married-spouse-absent'], 
#                                   'No-longer-married', inplace=True)
#    data['marital.status'].replace(['Married-AF-Spouse', 'Married-civ-spouse'], 'Married-present-spouse', inplace=True)
#    data.loc[~data['native.country'].isin(['United-States']), 'native.country'] = 'Not-US'
    data['capital.diff'] = data['capital.gain']-data['capital.loss']

#def remover(data):
#    data.drop('education', axis=1,inplace=True)
        
def readyData(data, nonNumCol):
    #remover(data)
    #combiner(data)
    lbEnc(data, nonNumCol)
    return (scale(data))