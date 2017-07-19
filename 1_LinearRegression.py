from sklearn import linear_model

# Instantiate a new linear regression model
model = linear_model.LinearRegression()

# Provide training data X (matrix), and training result y (vector)
training_data_X = [[0, 0], [1, 1], [2, 2]]
training_result_y = [0, 1, 2]

# Train the model by to fit the data X, y
print model.fit(training_data_X, training_result_y)
### LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

# Print the model cooefficients
print model.coef_
### array([ 0.5,  0.5])

# Use model to predict result
test_data_X = [[3, 3], [100, 100], [9999, 9999]]
print model.predict(test_data_X)
### [  3.00000000e+00   1.00000000e+02   9.99900000e+03]