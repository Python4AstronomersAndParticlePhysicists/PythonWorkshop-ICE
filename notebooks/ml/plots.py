import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
import collections
import seaborn as sns
import numpy as np


def draw_tree(clf):
    import pydotplus
    d = tree.export_graphviz(
                clf,
                out_file=None,
                filled=True,
    )
    graph = pydotplus.graph_from_dot_data(d)

    colors = ('limegreen', 'dodgerblue')
    edges = collections.defaultdict(list)

    for edge in graph.get_edge_list():
        edges[edge.get_source()].append(int(edge.get_destination()))

    for edge in edges:
        edges[edge].sort()
        for i in range(2):
            dest = graph.get_node(str(edges[edge][i]))[0]
            dest.set_fillcolor(colors[i])

    return graph.create(format='png')


def draw_svm_decission_function(clf, ax=None, **kwargs):
    if not ax:
        ax = plt.gca()

    x_low, x_high = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    x1 = np.linspace(x_low, x_high, 40)
    x2 = np.linspace(y_low, y_high, 40)

    X1, X2 = np.meshgrid(x1, x2)
    xy = np.vstack([X1.ravel(), X2.ravel()]).T
    # get the separating hyperplane
    Z = clf.decision_function(xy).reshape(X1.shape)

    # plot decision boundary and margins
    cs = ax.contour(X1, X2, Z, levels=[-1., 0, 1.0], linestyles=['--', '-', '--'], **kwargs)
    cs.collections[0].set_label(kwargs.get('label', 'SVM Decission Boundary'))
    plt.axis('off')


def draw_linear_regression_function(reg, ax=None, **kwargs):
    if not ax:
        ax = plt.gca()
    b_1, b_2 = reg.coef_
    b_0 = reg.intercept_

    # solve the function y = b_0 + b_1*X_1 + b_2 * X_2 for X2

    x_low, x_high = ax.get_xlim()
    x1s = np.linspace(x_low, x_high)
    x2s = (0.5 - b_0 - b_1 * x1s) / b_2

    ax.plot(x1s, x2s, **kwargs)


def draw_decission_boundaries(knn, ax=None, cmap='winter', alpha=0.07, **kwargs):
    if not ax:
        ax = plt.gca()

    x_low, x_high = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    x1 = np.linspace(x_low, x_high, 100)
    x2 = np.linspace(y_low, y_high, 100)

    X1, X2 = np.meshgrid(x1, x2)
    xy = np.vstack([X1.ravel(), X2.ravel()]).T
    Z = knn.predict(xy).reshape(X1.shape)

    # plot decision boundary and margins
    cs = ax.contourf(X1, X2, Z, **kwargs, cmap=cmap, alpha=alpha,)
    cs.collections[0].set_label(kwargs.get('label', 'Decission Boundary'))
    plt.axis('off')


def draw_decission_surface(clf, predictions, label=None):
    ax = plt.gca()
    x_low, x_high = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    x1 = np.linspace(x_low, x_high, 100)
    x2 = np.linspace(y_low, y_high, 100)

    X1, X2 = np.meshgrid(x1, x2)
    xy = np.vstack([X1.ravel(), X2.ravel()]).T
    Z = clf.predict_proba(xy)[:, 1].reshape(X1.shape)

    plt.imshow(Z, extent=[x_low, x_high, y_low, y_high], cmap='GnBu', origin='lower', vmin=0, vmax=1)
    plt.grid()
    plt.colorbar(label=label)
    plt.axis('off')


def plot_bars_and_confusion(truth, prediction, axes=None, vmin=None, vmax=None):
    accuracy = accuracy_score(truth, prediction)
    cm = confusion_matrix(truth, prediction)

    if not axes:
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    if not vmin:
        vmin = cm.min()

    if not vmax:
        vmax = cm.max()

    (prediction == truth).value_counts().plot.barh(ax=axes[0])
    axes[0].text(150, 0.5, 'Accuracy {:0.3f}'.format(accuracy))

    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='RdPu',
        xticklabels=['No', 'Yes'],
        yticklabels=['No', 'Yes'],
        ax=axes[1],
        vmin=vmin,
        vmax=vmax,
    )
    axes[1].set_ylabel('Actual')
    axes[1].set_xlabel('Predicted')
