import azure.functions as func
import json

app = func.FunctionApp()

@app.function_name(name="HealthCheck")
@app.route(route="health", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function para verificar o status da API.
    """
    return func.HttpResponse(
        json.dumps({
            "status": "OK",
            "message": "API está funcionando normalmente"
        }),
        status_code=200,
        mimetype="application/json",
    )
