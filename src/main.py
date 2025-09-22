from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from predict import predict_data


app = FastAPI(title="Wine Classification API", description="API for predicting wine types using machine learning")

class WineData(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float

class WineResponse(BaseModel):
    prediction: int
    wine_class: str

@app.get("/", status_code=status.HTTP_200_OK)
async def health_ping():
    return {"status": "healthy", "message": "Wine Classification API is running"}

@app.post("/predict", response_model=WineResponse)
async def predict_wine(wine_features: WineData):
    """
    Predict wine class based on chemical analysis features.
    """
    try:
        # Create feature array in the same order as the wine dataset
        features = [[
            wine_features.alcohol,
            wine_features.malic_acid, 
            wine_features.ash,
            wine_features.alcalinity_of_ash,
            wine_features.magnesium,
            wine_features.total_phenols,
            wine_features.flavanoids,
            wine_features.nonflavanoid_phenols,
            wine_features.proanthocyanins,
            wine_features.color_intensity,
            wine_features.hue,
            wine_features.od280_od315_of_diluted_wines,
            wine_features.proline
        ]]

        prediction = predict_data(features)
        wine_class_names = ["Class_0", "Class_1", "Class_2"]
        
        return WineResponse(
            prediction=int(prediction[0]),
            wine_class=wine_class_names[int(prediction[0])]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


    
