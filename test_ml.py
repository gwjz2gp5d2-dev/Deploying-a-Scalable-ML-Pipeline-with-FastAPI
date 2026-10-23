import pytest
import numpy as np
from scipy.constants import precision

from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics,save_model, load_model

# Create reusable sample data for testing model training and inference.
@pytest.fixture
def sample_data():
    X = np.array([
        [25, 40],
        [35, 45],
        [45, 50],
        [55, 60]
    ])
    y = np.array([0, 0, 1, 1])

    return X, y

def test_train_model(sample_data):
    """
    Verify that training returns a fitted Random Forest classifier.
    """
    X, y = sample_data

    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier)
    assert hasattr(model, 'estimators_')


def test_inference(sample_data):
    """
    Verify that inference returns valid predictions for each record.
    """
    X, y = sample_data

    model = train_model(X, y)
    predictions = inference(model, X)

    assert len(predictions) == len(y)
    assert set(predictions).issubset({0, 1})


def test_compute_model_metrics():
    """
    Verify precision, recall, and F1 are calculated correctly.
    """
    y = np.array([0, 0, 1, 1])
    predictions = np.array([0, 1, 1, 1])

    precision, recall, f1 = compute_model_metrics(y, predictions)

    assert precision == pytest.approx(2/3)
    assert recall == pytest.approx(1.0)
    assert f1 == pytest.approx(0.8)

def test_save_load_model(sample_data, tmp_path):
    """
    Verify that saving and loading a model works as expected.
    """
    X, y = sample_data

    model = train_model(X, y)
    model_path = tmp_path / 'model.pkl'

    save_model(model, model_path)
    loaded_model = load_model(model_path)

    original_predictions = inference(model, X)
    loaded_predictions = inference(loaded_model, X)

    assert model_path.exists()
    assert np.array_equal(original_predictions, loaded_predictions)