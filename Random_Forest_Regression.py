from sklearn.ensemble import RandomForestRegressor 

randfr = RandomForestRegressor(max_depth=4)
randfr.fit(X_train, y_train) 

print(mean_squared_error(y_test, randfr.predict(X_test)))