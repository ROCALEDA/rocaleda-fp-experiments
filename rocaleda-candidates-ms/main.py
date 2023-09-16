from dotenv import load_dotenv
from fastapi import FastAPI

from initializer import Initializer

load_dotenv()

app = FastAPI()
Initializer(app).setup()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
