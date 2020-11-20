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

    #test------------------
    print(feature_values)
    #feature_values.__delitem__('education')
    #print(feature_values)
    #test------------------

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
    
    data = data1 #readyData(data1, noNumColumn)
    
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


def combiner(combData):
    #Race
    #combData['race'].replace(['Black', 'Asian-Pac-Islander','Amer-Indian-Eskimo'], 'Other', inplace=True)
    #Mrital.status
    combData['marital.status'].replace(['Divorced', 'Widowed', 'Separated', 'Never-married'], 
                                       'Not-married', inplace=True)
    combData['marital.status'].replace(['Married-AF-Spouse', 'Married-civ-spouse','Married-spouse-absent'], 'Married', inplace=True)
    #native.country
    #combData.loc[~combData['native.country'].isin(['United-States']), 'native.country'] = 'Not-US'
    #Education.num
    #combData['education.num'].replace([1, 2, 3, 4 ,5, 6], 0, inplace=True)
    #combData['education.num'].replace([7, 8, 9], 1, inplace=True)
    #combData['education.num'].replace([10, 11, 12, 13], 2, inplace=True)
    #combData['education.num'].replace([14, 15, 16], 3, inplace=True)
