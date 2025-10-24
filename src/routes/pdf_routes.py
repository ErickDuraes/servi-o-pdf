from flask import Blueprint, request, jsonify, send_file
from src.services.pdf_service import PDFService

pdf_bp = Blueprint('pdf', __name__)
pdf_service = PDFService()

@pdf_bp.route("/merge", methods=["POST"])
def merge_pdfs():
    """Endpoint para mesclar PDFs."""
    try:
        if "arquivos" not in request.files:
            return jsonify({"erro": "Nenhum arquivo enviado. Envie pelo menos um PDF."}), 400

        arquivos = request.files.getlist("arquivos")
        
        pdf_bytes = pdf_service.merge_pdfs(arquivos)
        
        return send_file(
            pdf_bytes,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='merged_contract.pdf'
        )
        
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado: {str(e)}"}), 500