import qrcode

def generate_qr(data: str):
    img = qrcode.make(data)
    file_name = "pass_qr.png"
    img.save(file_name)
    return file_name
