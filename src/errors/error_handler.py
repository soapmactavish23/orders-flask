from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.main.http_types.http_response import HttpResponse


def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntity)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )