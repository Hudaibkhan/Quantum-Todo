from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from ..utils.jwt import decode_access_token

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Try to get token from cookies first
        token = request.cookies.get("auth_token")

        # If not in cookies, try to get from Authorization header
        if not token:
            auth_header = request.headers.get("Authorization")
            if auth_header and auth_header.startswith("Bearer "):
                token = auth_header[len("Bearer "):]

        request.state.user_id = None

        if token:
            payload = decode_access_token(token)
            if payload:
                request.state.user_id = payload.get("sub")

        response = await call_next(request)
        return response

def get_current_user_id(request: Request):
    if not request.state.user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    return request.state.user_id
