# Obesity Prediction Microservice

#### Nama : Muhammad Fakhry Zacky Putra
#### NIM : 2410511009
#### Kelas : Informatika A

## Project microservice menggunakan:

- FastAPI
- scikit-learn
- Express.js

## Arsitektur
```bash
Client → Node.js → Python ML Service → ML Model
```

## Struktur Folder
```
obesity-microservice/
│
├── python/
│   ├── app.py
│   ├── train_model.py
│   ├── obesity.csv
│   ├── model.pkl
│   └── requirements.txt
│
├── js/
│   ├── server.js
│   ├── package.json
│   └── .env
│
├── postman/
│   └── obesity-api.json
│
└── README.md
```

## Menjalankan Python Service

```bash
cd python
```

Install dependency:

```bash
pip3 install -r requirements.txt
```

Train model:

```bash
python3 train_model.py
```

Run FastAPI:

```bash
python3 -m uvicorn app:app --reload
```

Swagger:
```
http://127.0.0.1:8000/docs
```

## Menjalankan Node Service

```bash
cd js
```

Install dependency:

```bash
npm install
```

Run server:

```bash
node server.js
```

## Endpoint

### GET /health

Health check service.

## POST /api/obesity/predict

### Request

```json
{
  "height": 170,
  "weight": 60,
  "age": 20
}
```

### Response

```json
{
  "service": "Node.js API Gateway",
  "ml_response": {
    "status": "success",
    "prediction": "Tidak Obesitas"
  }
}
```

## Dataset

Dataset  buatan sendiri:
- height
- weight
- age
- obesity status
