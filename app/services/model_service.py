import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import get_cached_prediction, set_cached_prediction

def load_model():
    model = joblib.load(settings.MODEL_PATH)
    return model

model = load_model()

def predict_car_price(features: dict) -> dict:
    cache_key = " ".join([str(v) for v in features.values()])
    
    cached_result = get_cached_prediction(cache_key)
    if cached_result:
        return cached_result
    
    feature_df = pd.DataFrame([features])
    prediction = model.predict(feature_df)[0]
    result = {"predicted_price": round(prediction, 2)}
    
    set_cached_prediction(cache_key, result)
    return result