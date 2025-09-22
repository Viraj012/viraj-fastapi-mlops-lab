# FastAPI MLOps Lab - Viraj's Submission

## Student Information
- **Name**: Viraj
- **Assignment**: FastAPI MLOps Lab - Iris Classification API
- **Course**: MLOps

## Lab Overview
This lab demonstrates how to expose ML models as APIs using FastAPI and uvicorn. The workflow includes:
1. Training a Decision Tree Classifier on the Iris Dataset
2. Serving the trained model as an API using FastAPI and uvicorn
3. Testing the API endpoints

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv fastapi_lab_env
```

### 2. Activate Environment
```bash
# On macOS/Linux:
source fastapi_lab_env/bin/activate

# On Windows:
fastapi_lab_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Lab

### 1. Train the Model
Navigate to the src folder and train the Decision Tree Classifier:
```bash
cd src
python train.py
```

### 2. Start the FastAPI Server
```bash
uvicorn main:app --reload
```

### 3. Test the API
- **Documentation**: Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Interactive testing**: Use the FastAPI automatic documentation interface
- **Alternative**: Use Postman or curl for API testing

## Project Structure
```
viraj-fastapi-mlops-lab/
├── assets/
├── model/
│   └── iris_model.pkl
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── main.py
│   ├── predict.py
│   └── train.py
├── README.md
├── requirements.txt
└── .gitignore
```

## API Endpoints
- `GET /`: Health check endpoint
- `POST /predict`: Iris classification prediction endpoint

## Submission Details
- **Repository**: [Your GitHub URL will go here]
- **Completion Date**: [Date]
- **Status**: In Progress

## Notes
This is my implementation of the FastAPI MLOps lab, focusing on creating a robust API for machine learning model inference.
