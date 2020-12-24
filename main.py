import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from Adaboost import AdaBoost
from Shapes import Point, Line, VerticalLine

ITERATIONS = 100


def makePoints(data, points_arr):
    for index in range(0, len(data)):
        point = Point(np.double(data[index, 0]), np.double(data[index, 1]), np.double(data[index, 2]))
        points_arr = np.append(points_arr, point)
    return points_arr


def makePoints_HC(data, points_arr):
    for index in range(0, len(data)):
        point = Point(np.double(data[index, 0]), np.double(data[index, 2]), np.double(data[index, 1]))
        points_arr = np.append(points_arr, point)
    return points_arr


def makeRules(lines_arr, points_arr):
    for index in range(0, len(points_arr)):
        for k in range(index + 1, len(points_arr)):
            if int(points_arr[index].getX()) == int(points_arr[k].getX()):
                line1 = VerticalLine(points_arr[index].getX(), 0)
                line2 = VerticalLine(points_arr[index].getX(), 1)
            else:
                line1 = Line(points_arr[index], points_arr[k], 0)
                line2 = Line(points_arr[index], points_arr[k], 1)

            lines_arr = np.append(lines_arr, line1)
            lines_arr = np.append(lines_arr, line2)

    return lines_arr


# -------------------------------HC_BODY_TEMPERATURE---------------------------------
Body_temp_data = pd.read_csv('Data/HC_Body_Temperature.txt', delim_whitespace=True)
Body_temp_data['gender'] = Body_temp_data['gender'].replace(1, -1)
Body_temp_data['gender'] = Body_temp_data['gender'].replace(2, 1)
Body_temp_data = Body_temp_data.to_numpy()

points_temp = np.empty(0, dtype=Point)
points_temp = makePoints_HC(Body_temp_data, points_temp)

rules_temp = np.empty(0, dtype=object)
rules_temp = makeRules(rules_temp, points_temp)

total_hc_train_error = np.zeros(8)
total_hc_test_error = np.zeros(8)


# -------------------------------IRIS---------------------------------
iris_data = pd.read_csv('Data/iris.data')

iris_data = iris_data.replace('Iris-versicolor', 1)
iris_data = iris_data.replace('Iris-virginica', -1)
iris_data = iris_data.replace('Iris-setosa', 0)

iris_data = iris_data[(iris_data != 0).all(1)]

iris_data = iris_data.to_numpy()
iris_data = np.delete(iris_data, 0, 1)
iris_data = np.delete(iris_data, 2, 1)

points_iris = np.empty(0, dtype=Point)
points_iris = makePoints(iris_data, points_iris)

rules_iris = np.empty(0, dtype=object)
rules_iris = makeRules(rules_iris, points_iris)

total_iris_train_error = np.zeros(8)
total_iris_test_error = np.zeros(8)


for i in range(0, ITERATIONS):
    print("Number of iteration: "+str(i))
    points_temp = shuffle(points_temp)
    x_train, x_test = train_test_split(points_temp, test_size=0.5, random_state=1)
    train_hc = AdaBoost(x_train, x_test, rules_temp)
    train_hc.fit()

    hc_train_error = train_hc.get_train_error()
    hc_test_error = train_hc.get_test_error()
    total_hc_train_error = np.add(total_hc_train_error, hc_train_error)
    total_hc_test_error = np.add(total_hc_test_error, hc_test_error)

total_hc_train_error /= ITERATIONS
total_hc_test_error /= ITERATIONS
print("######HC BODY TEMPERATURE DATA#####")
for j in range(0, 8):
    print("number of rules:" + str(j+1))
    print("train error:" + str(total_hc_train_error[j]) + " test error:" + str(total_hc_test_error[j]))


for i in range(0, ITERATIONS):
    print("Number of iteration: " + str(i))
    points_iris = shuffle(points_iris)
    x_train, x_test = train_test_split(points_iris, test_size=0.5)
    train_iris = AdaBoost(x_train, x_test, rules_iris)
    train_iris.fit()

    iris_train_error = train_iris.get_train_error()
    iris_test_error = train_iris.get_test_error()
    total_iris_train_error += iris_train_error
    total_iris_test_error += iris_test_error

total_iris_train_error /= ITERATIONS
total_iris_test_error /= ITERATIONS
print("######IRIS DATA#####")
for j in range(0, 8):
    print("number of rules:" + str(j+1))
    print("train error:" + str(total_iris_train_error[j]) + " test error:" + str(total_iris_test_error[j]))

