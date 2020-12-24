import numpy as np


class AdaBoost:

    def __init__(self, train, test, rules):
        self.K = 8
        self.rules = rules

        self.train = train
        self.test = test

        # initialize points weights
        n = self.train.shape[0]
        self.points_weights = np.ones(n) / n

        self.rules_weights = np.zeros(len(self.rules))
        self.rules_errors = np.zeros(len(self.rules))
        self.HK_train_errors = np.zeros(shape=self.K)
        self.HK_test_errors = np.zeros(shape=self.K)
        self.best_rules = np.zeros(shape=self.K)

    def fit(self):
        for i in range(0, self.K):
            self.rules_errors = np.zeros(len(self.rules))

            # compute weighted errors for each rule
            self.compute_weighted_errors()

            # Select the classifier with min weighted error
            index = np.argmin(self.rules_errors)

            # Set classifier weight 𝛼_𝑡 based on its error
            err = self.rules_errors[index]
            if err == 0:
                err = 0.0001
            self.rules_weights[index] = 0.5 * np.log((1 - err) / err)

            # Update point weights
            self.update_point_weights(index)

            self.best_rules = self.get_best_rules(i+1)
            self.HK_train_errors[i] = self.get_error(self.train)
            self.HK_test_errors[i] = self.get_error(self.test)

    def compute_weighted_errors(self):
        for i in range(0, len(self.rules)):
            for j in range(0, len(self.train)):
                if self.rules[i].label(self.train[j]) != self.train[j].getLabel():
                    self.rules_errors[i] += self.points_weights[j]

    def update_point_weights(self, index):
        for i in range(len(self.points_weights)):
            alpha = self.rules_weights[index]
            h = self.rules[index].label(self.train[i])
            y = self.train[i].getLabel()
            self.points_weights[i] = self.points_weights[i] * np.exp(-alpha * h * y)
        self.points_weights /= np.sum(self.points_weights)

    def get_best_rules(self, count):
        best_rules = np.empty(0, dtype=object)
        for rule_index in self.rules_weights.argsort()[-count:]:
            best_rules = np.append(best_rules, rule_index)
        return best_rules

    def get_label(self, p):
        _sum = 0
        for rule_index in range(0, len(self.best_rules)):
            label_h = self.rules[self.best_rules[rule_index]].label(p)
            _sum += self.rules_weights[self.best_rules[rule_index]] * label_h

        if _sum >= 0:
            label = 1
        else:
            label = -1

        return label

    def get_error(self, x):
        wrong = 0
        for point in range(0, len(x)):
            if x[point].getLabel() != self.get_label(x[point]):
                wrong += 1

        return wrong

    def get_train_error(self):
        return self.HK_train_errors

    def get_test_error(self):
        return self.HK_test_errors
