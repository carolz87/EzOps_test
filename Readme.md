# FastAPI LLM

## Overview
This is a FastAPI-based project that integrates an open-source LLM from Hugging Face, enhanced with additional tools:
- **Mathematical Expression Evaluator**: Supports both explicit mathematical expressions (e.g., `2 + 2`) and natural language queries (e.g., *" five times three"*).
- **Wikipedia Search**: Fetches concise summaries from Wikipedia when users inquire about people, concepts, or historical events.

## Features
✅ **FastAPI-powered REST API**
✅ **Hugging Face LLM integration** (Google's `flan-t5-small`)
✅ **NLP-driven mathematical expression conversion**
✅ **Wikipedia search tool integration**
<!-- ✅ **Scalable and containerized with Docker** -->

---

## Installation & Setup
`Back-end install`
### **Prerequisites**
- Python 3.8+
- pip
<!-- - Docker (optional) -->

### **1️⃣ Clone the repository**
```sh
 git clone https://github.com/carolz87/EzOps_test

 cd EzOps_test
 cd backend

```

### **2️⃣ Set up the virtual environment** (Recommended)
```sh
cd backend
python -m venv venv
source venv/bin/activate  
```
If you're using Windows:
```sh
cd backend
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\activate
```

### **3️⃣ Install dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the FastAPI server**
```sh
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

`Front-end install`
## Prerequisites
- **Node.js** (v16 or later) – [Download here](https://nodejs.org/)
- **npm** (comes with Node.js)

### **1️⃣ Clone the repository**
___Note: If the clone already done, you don't have to do this again___
```sh
 git clone https://github.com/carolz87/EzOps_test

 cd EzOps_test
```
Acess the Front-end folder
```sh
 cd frontend
```

### **2️⃣ Install dependencies**
```sh
npm install
```

### **3️⃣ Run the Fron-end**
```sh
npm run dev
```

The Front-end will be available at: `http://127.0.0.1:4000`

---

## API Endpoints
### **🔹 Base URL:** `http://127.0.0.1:8000`

___All the backend endpoints are listed on Swagger in `BaseURL/docs`___

### **1️⃣ Health Check**
```http
GET /
```
✅ **Response:**
```json
{ "message": "API Ready!" }
```

### **2️⃣ Chat Endpoint**
```http
POST /chat
```
📌 **Request Body (JSON):**
```json
{ "input_text": "Who is Albert Einstein?" }
```
✅ **Response:**
```json
{ "response": "Albert Einstein was a theoretical physicist known for..." }
```

### **3️⃣ Mathematical Expression Processing**
Supports both **direct expressions** and **natural language queries**.
```json
{ "input_text": "2+2" }
```
✅ **Response:**
```json
{ "response": 4 }
```

Or:

```json
{ "input_text": "five times three" }
```
✅ **Response:**
```json
{ "response": 15 }
```

### **4️⃣ Wikipedia Search**
When the user asks for information, the API fetches a summary from Wikipedia.
```json
{ "input_text": "Wikipedia Neural Networks" }
```
✅ **Response:**
```json
{ "response": "A neural network is a computational model inspired by the human brain..." }
```

---
<!-- 
## Running with Docker (Optional)
For containerized deployment, use Docker:
```sh
docker build -t fastapi-ai-chatbot .
docker run -p 8000:8000 fastapi-ai-chatbot
```

--- -->
