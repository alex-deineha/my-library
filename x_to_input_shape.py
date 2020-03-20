
def x_to_input_shape(x):
    return [np.absolute(x[i]) for i in categorical_features] + [x[numerical_features]]
