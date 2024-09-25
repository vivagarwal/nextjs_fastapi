from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://nextjs-fastapi-8kvrmam3r-vivagarwals-projects.vercel.app","https://nextjs-fastapi-orcin.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to root page!"}

@app.get("/api/hello")
async def read_root():
    return {"message": "Hello from FastAPI!"}

