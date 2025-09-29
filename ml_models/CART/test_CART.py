import warnings
warnings.filterwarnings("ignore", category=UserWarning)  # Suppress sklearn warnings for cleaner

import numpy as np
from sklearn.datasets import (
    make_classification, 
    make_regression, 
    load_iris, 
    load_diabetes
)
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, 
    balanced_accuracy_score, 
    f1_score, 
    root_mean_squared_error, 
    mean_absolute_error, 
    r2_score
)

from CART import ClassificationTree, RegressionTree

# ====== Helpers ======

def eval_classification(model, X_train, y_train, X_test, y_test, name=""):
    model.train(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    bacc = balanced_accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")
    print(f"[CLS] {name:20s}  acc={acc:.3f}  bacc={bacc:.3f}  f1w={f1:.3f}")

def eval_regression(model, X_train, y_train, X_test, y_test, name=""):
    model.train(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = root_mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"[REG] {name:20s}  RMSE={rmse:.3f}  MAE={mae:.3f}  R2={r2:.3f}")

def sanity_pure_node(model_cls):
    # All labels identical -> tree should be a single leaf predicting that label/mean
    X = np.random.RandomState(0).randn(20, 3)
    y = np.zeros(20)  # single class or constant target
    model = model_cls(max_depth=None, min_samples_split=2)
    model.train(X, y)
    y_hat = model.predict(X)
    assert np.all(y_hat == y), "Pure-node sanity check failed: predictions should be constant."
    print("[SANITY] Pure-node case passed.")

def sanity_no_split(model_cls):
    # All features constant -> must produce a single leaf (no split possible)
    X = np.ones((30, 4))
    y = np.concatenate([np.zeros(15), np.ones(15)])  # still should not split (no gain)
    model = model_cls(max_depth=None, min_samples_split=2)
    model.train(X, y)
    y_hat = model.predict(X)
    # For classifier: majority vote; for regressor: mean
    print("[SANITY] No-split case ran. Pred unique:", np.unique(y_hat))

# ====== Main battery ======

def main():
    rng = np.random.RandomState(42)

    # --------------------
    # Classification tests
    # --------------------
    # 1) Synthetic easy classification
    Xc, yc = make_classification(
        n_samples=600, n_features=6, n_informative=4, n_redundant=0,
        n_clusters_per_class=2, class_sep=1.2, random_state=0
    )
    Xc_tr, Xc_te, yc_tr, yc_te = train_test_split(Xc, yc, test_size=0.3, random_state=0, stratify=yc)

    clf_shallow = ClassificationTree(max_depth=3, min_samples_split=4, loss="gini")
    eval_classification(clf_shallow, Xc_tr, yc_tr, Xc_te, yc_te, name="synthetic (depth=3)")

    clf_deep = ClassificationTree(max_depth=None, min_samples_split=2, loss="entropy")
    eval_classification(clf_deep, Xc_tr, yc_tr, Xc_te, yc_te, name="synthetic (deep)")

    # 2) Iris (small real-world)
    iris = load_iris()
    Xi, yi = iris.data, iris.target
    Xi_tr, Xi_te, yi_tr, yi_te = train_test_split(Xi, yi, test_size=0.3, random_state=1, stratify=yi)

    clf_iris = ClassificationTree(max_depth=4, min_samples_split=2, loss="gini")
    eval_classification(clf_iris, Xi_tr, yi_tr, Xi_te, yi_te, name="iris (depth=4)")

    # Sanity checks for classifier
    sanity_pure_node(ClassificationTree)
    sanity_no_split(ClassificationTree)

    # -----------------
    # Regression tests
    # -----------------
    # 1) Synthetic regression with noise
    Xr, yr = make_regression(
        n_samples=800, n_features=8, n_informative=6, noise=12.0, random_state=0
    )
    Xr_tr, Xr_te, yr_tr, yr_te = train_test_split(Xr, yr, test_size=0.25, random_state=0)

    reg_shallow = RegressionTree(max_depth=3, min_samples_split=5, loss="mse")
    eval_regression(reg_shallow, Xr_tr, yr_tr, Xr_te, yr_te, name="synthetic (depth=3)")

    reg_deep = RegressionTree(max_depth=None, min_samples_split=2, loss="mae")
    eval_regression(reg_deep, Xr_tr, yr_tr, Xr_te, yr_te, name="synthetic (deep, MAE)")

    # 2) Diabetes (tabular real-world, medium)
    diab = load_diabetes()
    Xd, yd = diab.data, diab.target
    Xd_tr, Xd_te, yd_tr, yd_te = train_test_split(Xd, yd, test_size=0.25, random_state=0)

    reg_diab = RegressionTree(max_depth=4, min_samples_split=3, loss="mse")
    eval_regression(reg_diab, Xd_tr, yd_tr, Xd_te, yd_te, name="diabetes (depth=4)")

    # Sanity checks for regressor
    sanity_pure_node(RegressionTree)
    sanity_no_split(RegressionTree)

    # ---------------
    # Edge behaviors
    # ---------------
    # min_samples_split preventing tiny splits
    X_edge, y_edge = X_edge, y_edge = make_classification(
    n_samples=120,
    n_features=4,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    random_state=0
    )
    Xtr_e, Xte_e, ytr_e, yte_e = train_test_split(X_edge, y_edge, test_size=0.3, random_state=0)
    clf_ms = ClassificationTree(max_depth=None, min_samples_split=20, loss="gini")
    eval_classification(clf_ms, Xtr_e, ytr_e, Xte_e, yte_e, name="min_samples_split=20")

    print("\nAll tests executed.")

if __name__ == "__main__":
    # Minimal graceful failure if your current implementation still has the split-loop issue.
    try:
        from CART import ClassificationTree, RegressionTree
    except ImportError:
        pass  # running as a script where classes are already in scope
    main()