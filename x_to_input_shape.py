from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X[numerical_features] = scaler.fit_transform(X[numerical_features])

from sklearn.preprocessing import LabelEncoder
label_encoders = []
for categorical_feature in categorical_features:
    le = LabelEncoder()
    X[categorical_feature] = le.fit_transform(X[categorical_feature])
    label_encoders.append(le)

means_to_fill = X.mean()
X = X.fillna(means_to_fill)



def x_to_input_shape(x):
    return [np.absolute(x[i]) for i in categorical_features] + [x[numerical_features]]
