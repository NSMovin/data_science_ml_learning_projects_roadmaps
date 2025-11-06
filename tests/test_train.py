import os
from projects.project1_name.src.train import train_and_save

def test_train_creates_model(tmp_path):
    out = tmp_path / "model.joblib"
    train_and_save(path=str(out))
    assert os.path.exists(str(out))
