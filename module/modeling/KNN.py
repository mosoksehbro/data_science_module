import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

def do_modeling(scaled_df, target, test_size=0.25, shuffle=False, k=3):
    # Split dataset (Independent / Target)
    X = scaled_df.drop(columns=[target]).values
    y = scaled_df[target].values

    # Split dataset (train / test)
    X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=1-test_size,test_size=test_size,shuffle=shuffle)
    
    # KNN -> fit & predict
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    cv_scores = cross_val_score(knn,X_train,y_train,cv=5)

    # Evaluation
    print("<Result Score(k=",k,")>",sep="")
    print("Scores:",np.round(cv_scores,5),"/ mean:",np.round(np.mean(cv_scores),5))
    
    # Show matrix
    print("<Classification Report (KNN)>")
    print(classification_report(knn.predict(X_test),y_test))