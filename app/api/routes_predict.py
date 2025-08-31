from fastapi import APIRouter, Depends
from app.schemas.userInput import CarFeatures
from app.core.dependencies import get_current_user,get_api_key
from app.services.model_service import predict_car_price

router= APIRouter()

@router.post("/predict")
def predict_price(features: CarFeatures, user: str = Depends(get_current_user), _ = Depends(get_api_key)):
    feature_dict = features.model_dump()
    prediction = predict_car_price(feature_dict)
    return prediction