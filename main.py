from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to my website"}

@app.get("/contact")
def contact():
    return {
        "email": "nityavobugari@gmail.com",
        "phone": "8877666",
        "linkedin": "https://www.linkedin.com/in/nitya-vobugari/",
        "message": "Feel free to reach out!"
    }