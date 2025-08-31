# Car Price Prediction API

This project is a car price prediction service built with **FastAPI**. It uses a **RandomForest** machine learning model for predictions, implements **JWT authentication** for secure access, and uses **Redis** for caching.

## Features

- 🚗 Predict car prices using a trained RandomForest ML model
- 🔒 Secure endpoints with JWT authentication
- ⚡ Fast response times with Redis caching
- 📝 RESTful API built with FastAPI

## Input Features

The prediction model expects the following input fields:

| Field           | Type   | Description / Example Values                                      |
|-----------------|--------|------------------------------------------------------------------|
| `company`       | str    | Car manufacturer (e.g., "Toyota")                                |
| `year`          | int    | Year of manufacture (1900–2100)                                  |
| `owner`         | str    | Ownership status (`First`, `Second`, `Third`, `Fourth & Above`, `Test Drive Car`) |
| `fuel`          | str    | Fuel type (`Diesel`, `Petrol`, `LPG`, `CNG`)                     |
| `seller_type`   | str    | Seller type (`Individual`, `Dealer`, `Trustmark Dealer`)         |
| `transmission`  | str    | Transmission type (`Manual`, `Automatic`)                        |
| `km_driven`     | float  | Kilometers driven (>= 0)                                         |
| `mileage_mpg`   | float  | Mileage in miles per gallon (>= 0)                               |
| `engine_cc`     | float  | Engine capacity in cc (>= 0)                                     |
| `max_power_bhp` | float  | Maximum power in BHP (>= 0)                                      |
| `torque_nm`     | float  | Torque in Nm (>= 0)                                              |
| `seats`         | float  | Number of seats (1–20)                                           |

## Requirements

- Python 3.8+
- FastAPI
- scikit-learn
- Redis
- uvicorn
- python-jose (for JWT)
- redis-py

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/bisVo159/FastApi-Project.git
   cd FastApi-Project
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Start Redis server** (if not already running):
   ```sh
   redis-server
   ```

4. **Run the API:**
   ```sh
   uvicorn main:app --reload
   ```

## Usage

- Obtain a JWT token by logging in via the `/login` endpoint.
- Use the token to access the `/predict` endpoint and get car price predictions.

## API Endpoints

- `POST /login` — Authenticate and receive a JWT token
- `POST /predict` — Predict car price (requires JWT)

## Example Request

```json
POST /predict
Authorization: Bearer <your-jwt-token>
{
  "company": "Toyota",
  "year": 2018,
  "owner": "First",
  "fuel": "Petrol",
  "seller_type": "Dealer",
  "transmission": "Manual",
  "km_driven": 30000,
  "mileage_mpg": 18.5,
  "engine_cc": 1197,
  "max_power_bhp": 82,
  "torque_nm": 113,
  "seats": 5
}
```

**Author:** Anik Biswas