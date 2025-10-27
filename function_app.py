import azure.functions as func
import json


from src.services.pdf_service import ServicoPDF

app = func.FunctionApp()


@app.function_name(name="MesclarPDFs")
@app.route(route="merge", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def mesclar_pdfs(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function para mesclar múltiplos arquivos PDF em um único documento.

    Args:
        req: Requisição HTTP contendo os arquivos PDF

    Returns:
        func.HttpResponse: PDF mesclado ou mensagem de erro
    """
    try:
        # Verifica se há arquivos na requisição
        if not req.files:
            return _criar_resposta_erro(
                "Nenhum arquivo foi enviado. Por favor, envie pelo menos um arquivo PDF.",
                400,
            )

        # Coleta os arquivos
        lista_arquivos = []
        if "arquivos" in req.files:
            lista_arquivos.extend(req.files.getlist("arquivos"))
        else:
            lista_arquivos.extend(req.files.values())

        if not lista_arquivos:
            return _criar_resposta_erro(
                "Nenhum arquivo válido foi encontrado na requisição.", 400
            )

        # Mescla os PDFs
        servico_pdf = ServicoPDF()
        pdf_mesclado = servico_pdf.mesclar_pdfs(lista_arquivos)

        # Retorna o PDF mesclado
        return func.HttpResponse(
            pdf_mesclado.getvalue(),
            status_code=200,
            mimetype="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=documento_mesclado.pdf",
                "Cache-Control": "no-cache",
            },
        )

    except ValueError as erro_validacao:
        return _criar_resposta_erro(str(erro_validacao), 400)

    except Exception:
        return _criar_resposta_erro(
            "Ocorreu um erro interno durante o processamento. Tente novamente mais tarde.",
            500,
        )


def _criar_resposta_erro(mensagem_erro: str, codigo_status: int) -> func.HttpResponse:
    """Retorna resposta padronizada de erro"""
    return func.HttpResponse(
        json.dumps(
            {
                "sucesso": False,
                "erro": mensagem_erro,
                "codigo": codigo_status,
            }
        ),
        status_code=codigo_status,
        mimetype="application/json",
    )



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
