# 4TrackFridayPlaylistAnalysis

## Quickstart

```bash
brew link python@3.7

python3 -m pip install --upgrade pip
python3 -m pip install --user virtualenv

python3 -m virtualenv venv
source venv/bin/activate
python -m pip install -r requirements.txt

python -m uvicorn src.app.main:app --reload
```