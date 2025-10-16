from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
from PIL import Image
from email.parser import BytesParser
from email.policy import default
import os

PORT = 8000

HTML_FORM = b"""\
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>Konverter Gambar ke PDF</title>
</head>
<body>
  <h2>Unggah gambar untuk dikonversi ke PDF</h2>
  <form enctype="multipart/form-data" method="post">
    <input name="imagefile" type="file" accept="image/*" required>
    <br><br>
    <button type="submit">Upload & Convert</button>
  </form>
  <p>Supported: JPG, JPEG, PNG, BMP, TIFF, dsb.</p>
</body>
</html>
"""

class UploadHandler(BaseHTTPRequestHandler):
    def _send_html(self, content_bytes, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content_bytes)))
        self.end_headers()
        self.wfile.write(content_bytes)

    def do_GET(self):
        self._send_html(HTML_FORM)

    def do_POST(self):
        try:
            content_type = self.headers.get('Content-Type')
            if not content_type or 'multipart/form-data' not in content_type:
                self._send_html(b"<h1>400 Bad Request</h1><p>Expected multipart/form-data.</p>", status=400)
                return

            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)

            headers = f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode("utf-8")
            full_message = headers + body
            msg = BytesParser(policy=default).parsebytes(full_message)

            part = None
            for p in msg.iter_parts():
                if p.get_param('name', header='content-disposition') == 'imagefile':
                    part = p
                    break

            if not part:
                self._send_html(b"<h1>400</h1><p>Field 'imagefile' tidak ditemukan.</p>", status=400)
                return

            filename = part.get_filename()
            if not filename:
                self._send_html(b"<h1>400</h1><p>Tidak ada file dipilih.</p>", status=400)
                return

            file_data = part.get_payload(decode=True)

            image = Image.open(BytesIO(file_data))
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")

            pdf_buffer = BytesIO()
            image.save(pdf_buffer, "PDF")
            pdf_bytes = pdf_buffer.getvalue()

            name_wo_ext = os.path.splitext(os.path.basename(filename))[0]
            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Disposition", f'attachment; filename="{name_wo_ext}.pdf"')
            self.send_header("Content-Length", str(len(pdf_bytes)))
            self.end_headers()
            self.wfile.write(pdf_bytes)

        except Exception as e:
            error_message = f"<h1>500 Internal Server Error</h1><pre>{e}</pre>".encode("utf-8")
            self._send_html(error_message, status=500)


def run():
    server = HTTPServer(('localhost', PORT), UploadHandler)
    print(f"Server berjalan di http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")


if __name__ == "__main__":
    run()
