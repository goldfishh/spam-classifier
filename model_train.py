import numpy as np
import time    
from sklearn import metrics    
import pickle as pickle    
root = "C:\\Users\\goldfish\\Desktop\\spam"
  
def naive_bayes_classifier(train_x, train_y):    
    from sklearn.naive_bayes import MultinomialNB    
    model = MultinomialNB(alpha=0.01)    
    model.fit(train_x, train_y)    
    return model    
    
def knn_classifier(train_x, train_y):    
    from sklearn.neighbors import KNeighborsClassifier    
    model = KNeighborsClassifier()    
    model.fit(train_x, train_y)    
    return model    
       
def logistic_regression_classifier(train_x, train_y):    
    from sklearn.linear_model import LogisticRegression    
    model = LogisticRegression(penalty='l2')    
    model.fit(train_x, train_y)    
    return model    
     
def random_forest_classifier(train_x, train_y):    
    from sklearn.ensemble import RandomForestClassifier    
    model = RandomForestClassifier(n_estimators=8)    
    model.fit(train_x, train_y)    
    return model    
      
def decision_tree_classifier(train_x, train_y):    
    from sklearn import tree    
    model = tree.DecisionTreeClassifier()    
    model.fit(train_x, train_y)    
    return model    
 
def gradient_boosting_classifier(train_x, train_y):    
    from sklearn.ensemble import GradientBoostingClassifier    
    model = GradientBoostingClassifier(n_estimators=200)    
    model.fit(train_x, train_y)    
    return model    
      
def svm_classifier(train_x, train_y):    
    from sklearn.svm import SVC    
    model = SVC(kernel='rbf', probability=True)    
    model.fit(train_x, train_y)    
    return model      
    
def read_data(feature_file, label_file):   
	from sklearn.model_selection import train_test_split 
    feature = np.fromfile(feature_file,dtype=np.int,sep=",")
    #↓ change if need!
    feature = feature.reshape(9348,5000)
    label = np.fromfile(label_file,dtype=np.int,sep=",")
    train_x, test_x, train_y, test_y = train_test_split(feature, label, test_size = 0.4,random_state = 7)
    return train_x, test_x, train_y, test_y  
        
if __name__ == '__main__': 
    #↓ change if need!   
    feature_file = root + "\\Tfeature.dat"   
    label_file = root + "\\Tlabel.dat"  
    model_save_file = None    
    model_save = {}    
     
    test_classifiers = ['NB', 'KNN', 'LR', 'RF', 'DT', 'SVM', 'GBDT']    
    classifiers = {'NB':naive_bayes_classifier,     
                  'KNN':knn_classifier,    
                   'LR':logistic_regression_classifier,    
                   'RF':random_forest_classifier,    
                   'DT':decision_tree_classifier,    
                  'SVM':svm_classifier,    
                 'GBDT':gradient_boosting_classifier    
    }    
        
    print('reading training and testing data...')    
    train_x, test_x, train_y, test_y = read_data(feature_file,label_file)    
        
    for classifier in test_classifiers: 
        classifier = 'GBDT'
        print('******************* %s ********************' % classifier)    
        start_time = time.time()    
        model = classifiers[classifier](train_x, train_y)    
        print('training took %fs!' % (time.time() - start_time))    
        predict = model.predict(test_x)    
        if model_save_file != None:    
            model_save[classifier] = model    
        precision = metrics.precision_score(test_y, predict)    
        recall = metrics.recall_score(test_y, predict)    
        print('precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall))    
        accuracy = metrics.accuracy_score(test_y, predict)    
        print('accuracy: %.2f%%' % (100 * accuracy))     
    
    if model_save_file != None:    
        pickle.dump(model_save, open(model_save_file, 'wb'))    