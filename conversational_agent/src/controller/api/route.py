from fastapi import APIRouter, HTTPException, File, UploadFile, Form
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter()

@router.post("/conversation")
async def conversation_agents():
    pass