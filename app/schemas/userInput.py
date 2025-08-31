from pydantic import BaseModel, Field

class CarFeatures(BaseModel):
    company: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1900, le=2100)
    owner: str = Field(..., examples=['First' 'Second' 'Third' 'Fourth & Above' 'Test Drive Car'])
    fuel: str = Field(..., examples=['Diesel' 'Petrol' 'LPG' 'CNG'])
    seller_type: str = Field(..., examples=['Individual' 'Dealer' 'Trustmark Dealer'])
    transmission: str = Field(..., examples=['Manual' 'Automatic'])
    km_driven : float = Field(..., ge=0)
    mileage_mpg: float = Field(..., ge=0)
    engine_cc: float = Field(..., ge=0)
    max_power_bhp: float = Field(..., ge=0)
    torque_nm: float = Field(..., ge=0)
    seats: float = Field(..., ge=1, le=20)