import fitz
from io import BytesIO

class PDFService:
    def is_pdf_file(self, arquivo) -> bool:
        return arquivo.content_type == "application/pdf"

    def rasterizar_pdf_para_documento(self, conteudo_pdf: bytes, doc_saida: fitz.Document, matrix: fitz.Matrix):
        with fitz.open(stream=conteudo_pdf, filetype="pdf") as pdf:
            for pagina in pdf:
                pix = pagina.get_pixmap(matrix=matrix, alpha=False)
                largura, altura = pix.width, pix.height
                pagina_out = doc_saida.new_page(width=largura, height=altura)
                rect = fitz.Rect(0, 0, largura, altura)
                pagina_out.insert_image(rect, stream=pix.tobytes("png"))

    def merge_pdfs(self, arquivos) -> BytesIO:
        if not arquivos:
            raise ValueError("Nenhum arquivo enviado")

        pdf_saida = fitz.open()
        zoom = 0.5
        matrix = fitz.Matrix(zoom, zoom)

        for arquivo in arquivos:
            if not self.is_pdf_file(arquivo):
                raise ValueError(f"O arquivo '{arquivo.filename}' não é um PDF.")
            conteudo_pdf = arquivo.read()
            if not conteudo_pdf:
                continue
            self.rasterizar_pdf_para_documento(conteudo_pdf, pdf_saida, matrix)

        if len(pdf_saida) == 0:
            pdf_saida.close()
            raise ValueError("Nenhuma página foi processada")

        pdf_bytes = BytesIO()
        pdf_saida.save(pdf_bytes, deflate=True, deflate_images=True, garbage=4)
        pdf_saida.close()
        pdf_bytes.seek(0)
        return pdf_bytes
