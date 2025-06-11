from ninja import Router, Schema
from ninja.errors import HttpError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from datetime import datetime, timedelta, timezone
import jwt
from django.conf import settings

router = Router()

class LoginSchema(Schema):
    username: str
    password: str

@router.post("/login")
def login(request, data: LoginSchema):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        raise HttpError(401, "Invalid email or password")
    user.last_login = datetime.now(timezone.utc)
    user.save(update_fields=["last_login"])
    payload = {
        "user_id": user.id,
        "exp": datetime.now(timezone.utc) + timedelta(hours=24),
        "iat": datetime.now(timezone.utc),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return {"access_token": token}

class LoginSchema(Schema):
    username: str
    email: str
    password: str

@router.post("/register")
def register(request, data: LoginSchema):
    if User.objects.filter(username=data.username).exists():
        raise HttpError(400, "User already exists")
    user = User.objects.create_user(username=data.username, email=data.email, password=data.password)
    user.save()
    payload = {
        "user_id": user.id,
        "exp": datetime.now(timezone.utc) + timedelta(hours=24),
        "iat": datetime.now(timezone.utc),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return {"access_token": token}
