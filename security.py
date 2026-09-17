from fastapi import Header, HTTPException


API_KEY = "exam123"


def check_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="invalid api key"
        )

    return True