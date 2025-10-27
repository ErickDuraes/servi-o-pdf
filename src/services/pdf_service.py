import io
from typing import List
import fitz  # PyMuPDF
from werkzeug.datastructures import FileStorage
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader


class ServicoPDF:
    """
    Serviço responsável por operações relacionadas a PDF,
    incluindo conversão em imagem e mesclagem padronizada.
    """

    def mesclar_pdfs(self, arquivos: List[FileStorage]) -> io.BytesIO:
        """
        Mescla múltiplos arquivos PDF convertendo cada página em imagem,
        garantindo consistência visual e compatibilidade.
        """
        imagens = []

        for arquivo in arquivos:
            try:
                pdf_bytes = arquivo.read()
                doc = fitz.open(stream=pdf_bytes, filetype="pdf")

                for page_index in range(len(doc)):
                    page = doc.load_page(page_index)
                    pix = page.get_pixmap(dpi=300, alpha=False)  # converte página em imagem
                    img_bytes = pix.tobytes("png")
                    imagens.append(img_bytes)

                doc.close()

            except Exception as e:
                raise ValueError(f"Erro ao processar o arquivo '{arquivo.filename}': {str(e)}")

        # Agora recria o PDF final com todas as imagens renderizadas
        buffer_pdf = io.BytesIO()
        pdf_canvas = canvas.Canvas(buffer_pdf, pagesize=A4)

        for img_bytes in imagens:
            img = ImageReader(io.BytesIO(img_bytes))
            width, height = A4
            pdf_canvas.drawImage(img, 0, 0, width=width, height=height)
            pdf_canvas.showPage()

        pdf_canvas.save()
        buffer_pdf.seek(0)

        return buffer_pdf
