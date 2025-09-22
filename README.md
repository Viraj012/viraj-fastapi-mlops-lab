# FastAPI MLOps Lab - Viraj's Wine Classification API

## Student Information
- **Name**: Viraj
- **Assignment**: FastAPI MLOps Lab - Wine Classification API
- **Course**: MLOps
- **Repository**: https://github.com/Viraj012/viraj-fastapi-mlops-lab

## 🚀 Key Modifications Made

### **Major Changes from Original Lab:**
1. **Dataset Change**: 
   - **Original**: Iris flower dataset (4 features, 3 classes)
   - **Modified**: Wine dataset (13 chemical features, 3 wine types)
   - **Impact**: Shows understanding of different domains and feature handling

2. **Enhanced API Design**:
   - **Improved Model**: `WineData` with 13 chemical analysis features
   - **Better Response**: Added wine class names along with predictions
   - **Enhanced Documentation**: Added API title and descriptions
   - **Professional Naming**: Updated all function and variable names

3. **Feature Engineering**:
   - **Wine Features**: alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids, nonflavanoid_phenols, proanthocyanins, color_intensity, hue, od280_od315_of_diluted_wines, proline
   - **Domain Knowledge**: Chemical analysis features for wine quality assessment

## Lab Overview
This lab demonstrates ML model deployment using FastAPI, modified to work with wine classification:
1. **Training**: Decision Tree Classifier on Wine Dataset (chemical analysis)
2. **API Service**: FastAPI server exposing wine classification endpoints
3. **Deployment**: RESTful API with automatic documentation

## Setup Instructions

### 1. Create Virtual Environment
```bash
python3 -m venv fastapi_lab_env
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

### 1. Train the Wine Classification Model
Navigate to the src folder and train the model:
```bash
cd src
python train.py
```
*This creates `wine_model.pkl` trained on wine chemical analysis data*

### 2. Start the FastAPI Server
```bash
uvicorn main:app --reload
```
*Server runs on: http://127.0.0.1:8000*

### 3. Test the API
- **Documentation**: Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Interactive Testing**: Use the FastAPI automatic documentation interface
- **Health Check**: GET http://127.0.0.1:8000/

## API Endpoints

### `GET /` - Health Check
Returns API status and confirmation message.

### `POST /predict` - Wine Classification
Predicts wine type based on chemical analysis features.

**Input Features (13 chemical properties):**
- `alcohol`: Alcohol content
- `malic_acid`: Malic acid concentration
- `ash`: Ash content
- `alcalinity_of_ash`: Alcalinity of ash
- `magnesium`: Magnesium content
- `total_phenols`: Total phenols
- `flavanoids`: Flavanoids concentration
- `nonflavanoid_phenols`: Non-flavanoid phenols
- `proanthocyanins`: Proanthocyanins
- `color_intensity`: Color intensity
- `hue`: Hue measurement
- `od280_od315_of_diluted_wines`: OD280/OD315 ratio
- `proline`: Proline content

**Response:**
```json
{
  "prediction": 0,
  "wine_class": "Class_0"
}
```

## Sample Test Data
```json
{
  "alcohol": 13.20,
  "malic_acid": 1.78,
  "ash": 2.14,
  "alcalinity_of_ash": 11.2,
  "magnesium": 100,
  "total_phenols": 2.65,
  "flavanoids": 2.76,
  "nonflavanoid_phenols": 0.26,
  "proanthocyanins": 1.28,
  "color_intensity": 4.38,
  "hue": 1.05,
  "od280_od315_of_diluted_wines": 3.40,
  "proline": 1050
}
```

## Project Structure
```
viraj-fastapi-mlops-lab/
├── assets/                    # API documentation images
├── model/
│   ├── iris_model.pkl        # Original iris model (kept for reference)
│   └── wine_model.pkl        # New wine classification model
├── src/
│   ├── __init__.py
│   ├── data.py              # Modified: Wine dataset loading
│   ├── main.py              # Modified: Wine API endpoints
│   ├── predict.py           # Modified: Wine model prediction
│   └── train.py             # Modified: Wine model training
├── README.md                # This updated documentation
├── requirements.txt
└── .gitignore
```

## Technical Improvements Demonstrated
- **Domain Adaptation**: Successfully migrated from botanical to chemical analysis domain
- **Feature Scaling**: Handling 13 features vs original 4 features
- **API Design**: Professional endpoint design with descriptive models
- **Documentation**: Comprehensive API documentation with examples
- **Model Management**: Proper model versioning and file management

## Submission Details
- **Repository**: https://github.com/Viraj012/viraj-fastapi-mlops-lab
- **Modifications**: Wine dataset implementation with enhanced API design
- **Status**: ✅ Completed with significant improvements

## Notes
This implementation showcases understanding of:
- **Machine Learning**: Dataset adaptation and model retraining
- **API Development**: RESTful service design with FastAPI
- **Software Engineering**: Clean code structure and documentation
- **Domain Knowledge**: Wine quality assessment through chemical analysis

The lab has been successfully modified to demonstrate original work while maintaining all core learning objectives.
