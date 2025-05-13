

```markdown
# File Sharing Backend

A secure file-sharing backend system built with FastAPI and MongoDB Atlas.

## Features

- User registration & login (JWT Auth)
- Role-based access (Client & Ops)
- Secure file upload/download
- MongoDB for storage
- Passwords hashed using bcrypt

## Tech Stack

- FastAPI
- MongoDB (Atlas)
- Pydantic
- JWT Auth
- Bcrypt

## Setup

1. **Clone the repo**  
   `git clone (https://github.com/Rahulverma0706/EZ_Assignment.git)`

2. **Install dependencies**  
   `pip install -r requirements.txt`

3. **Configure environment**  
   Create `.env` with:
```

MONGO\_URI=your\_mongo\_uri
JWT\_SECRET=your\_secret

```

4. **Run the app**  
`uvicorn main:app --reload`

## API Endpoints

- `POST /register` – Register a user  
- `POST /login` – Login and get JWT token  
- `POST /upload` – Upload file (Auth required)  
- `GET /download/{file_id}` – Download file (Auth required)  

## License

MIT
```

---

Replace `https://github.com/username/repository-name.git` with your actual repo link. Let me know if you want to auto-generate it from your current folder.
