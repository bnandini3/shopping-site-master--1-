# Steps to run the backend

## 1. Create a virtual environment

This step is not necessary after the first time you run the backend.

```bash
python -m venv venv
```

## 2. Activate the virtual environment

```bash
venv\Scripts\activate
```

## 3. Install the requirements

You only need to do this step after the first time you run the backend or if you add a new package to the requirements.txt file.

```bash
pip install -r requirements.txt
```

## 4. Run the backend

```bash
flask run
```

new server will be running on http://127.0.0.1:5000
