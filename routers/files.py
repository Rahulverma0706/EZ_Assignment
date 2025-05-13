from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr
import os
import shutil
import uuid
from database import db  # assuming you have a db setup as shown earlier

router = APIRouter()

UPLOAD_FOLDER = "uploaded_files"  # Ensure this folder exists

class RegisterUser(BaseModel):
    name: str
    email: EmailStr
    password: str

# This should come from your auth system
def get_current_user():
    return {"email": "user@example.com", "role": "Ops"}  # Mocked user

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), current_user: dict = Depends(get_current_user)):
    try:
        # Unique filename to prevent clashes
        file_id = str(uuid.uuid4())
        filename = f"{file_id}_{file.filename}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save file to disk
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Save metadata to DB
        await db["files"].insert_one({
            "file_id": file_id,
            "filename": filename,
            "original_name": file.filename,
            "uploaded_by": current_user["email"],
            "role": current_user["role"],
            "path": file_path,
        })

        return {"message": "File uploaded successfully", "file_id": file_id}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/files/{file_id}")
async def download_file(file_id: str, current_user: dict = Depends(get_current_user)):
    file_doc = await db["files"].find_one({"file_id": file_id})

    if not file_doc:
        raise HTTPException(status_code=404, detail="File not found")

    # Optional: Restrict download based on user role
    if file_doc["role"] != current_user["role"]:
        raise HTTPException(status_code=403, detail="Access denied")

    return FileResponse(path=file_doc["path"], filename=file_doc["original_name"])


@router.post("/register")
def register_user(user: RegisterUser):
    return {"message": f"User {user.name} registered successfully"}
