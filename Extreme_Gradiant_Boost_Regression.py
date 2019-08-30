from xgboost import XGBRegressor

xgbr = XGBRegressor(n_estimators=100, learning_rate=0.1)
xgbr.fit(X_train, y_train)
print(mean_squared_error(xgbr.predict(X_test), y_test))
