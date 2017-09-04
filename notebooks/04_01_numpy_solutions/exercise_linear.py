def linear_regression(x, y):

    cov_matrix = np.cov(x, y)
    b = cov_matrix[0, 1] / cov_matrix[0, 0]
    a = np.mean(y) - b * np.mean(x)

    return a, b
