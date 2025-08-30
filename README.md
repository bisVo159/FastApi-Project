# Car Price Prediction API

This project is a car price prediction service built with **FastAPI**. It uses a **RandomForest** machine learning model for predictions, implements **JWT authentication** for secure access, and uses **Redis** for caching.

## Features

- 🚗 Predict car prices using a trained RandomForest ML model
- 🔒 Secure endpoints with JWT authentication
- ⚡ Fast response times with Redis caching
- 📝 RESTful API built with FastAPI

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


**Author:** Anik Biswas