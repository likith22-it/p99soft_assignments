from functools import wraps
from fastapi import Request, HTTPException


# Default credentials (can be overridden)
VALID_CREDENTIALS = {
    "admin": "password123",
    "user": "user123"
}


async def verify_auth_basic(request: Request):
    """
    Verify username/password from form data or query params.
    Raises HTTPException(401) if credentials are invalid.
    """
    # Try to get username/password from query params (for API calls)
    username = request.query_params.get("username")
    password = request.query_params.get("password")
    
    if not username or not password:
        raise HTTPException(status_code=401, detail="Missing username or password")
    
    if username not in VALID_CREDENTIALS or VALID_CREDENTIALS[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return username


def require_auth_basic(func):
    """
    Decorator to add username/password authentication checks to FastAPI route handlers.
    Credentials can be passed via query params: ?username=admin&password=password123
    
    Usage:
        @app.get("/weather")
        @require_auth_basic
        async def get_weather(request: Request, city: str = ""):
            return {"city": city, "temp": 20}
    """
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        # Verify auth before calling handler
        await verify_auth_basic(request)
        # Call the original route handler
        return await func(request, *args, **kwargs)
    
    return wrapper