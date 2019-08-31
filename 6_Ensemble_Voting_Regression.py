from sklearn.ensemble import VotingRegressor, RandomForestRegressor, AdaBoostRegressor

a = RandomForestRegressor(max_depth=4)
b = XGBRegressor()
c = AdaBoostRegressor(n_estimators=200, learning_rate=0.0001, random_state=0)

voting_reg = VotingRegressor(
    estimators=[('xgb', a), ('rdf', b), ('abr', c)]
)
voting_reg.fit(X_train, y_train)

print(mean_squared_error(voting_reg.predict(X_test), y_test))
