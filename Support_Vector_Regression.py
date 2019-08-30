from sklearn.svm import SVR

svr = SVR(kernel='rbf')
svr.fit(X_train, y_train)

print(mean_squared_error(svr.predict(X_test), y_test))