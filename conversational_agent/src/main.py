from fastapi import FastAPI
from conversational_agent.src.controller.api.route import router

app = FastAPI()

app.include_router(router, prefix="/api/v1/conversational_agent", tags=["Conversational Agent"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)