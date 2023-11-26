from fastapi import FastAPI, Request 
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-pgn")
async def upload_pgn(request: Request):

    pgn_data = await request.json()
    pgn = pgn_data.get('pgn','')
    # You can store it in a database, perform additional processing, etc.
    print(f"Received PGN: {pgn}")
    return {"message": "PGN: " + pgn + " received successfully"}


