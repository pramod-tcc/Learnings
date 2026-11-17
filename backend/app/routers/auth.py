
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.services.auth_service import (
    login_with_google,
    authenticate_with_google
)

from app.core.config import FRONTEND_URL

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/login")
async def google_login(request: Request):

    redirect_uri = request.url_for("google_callback")

    return await login_with_google(
        request,
        redirect_uri
    )

@router.get("/callback", name="google_callback")
async def google_callback(request: Request):

    user = await authenticate_with_google(request)

    request.session["user"] = {
        "google_id": user["sub"],
        "name": user.get("name"),
        "email": user.get("email"),
        "picture": user.get("picture")
    }

    return RedirectResponse(
        url=f"{FRONTEND_URL}/dashboard",
        status_code=303
    )