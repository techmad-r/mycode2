def fetch_image(self, file=None):
    self.authcheck()
    data = None
    if not file:
        file = self.get_image()
        file=file[0] if file else None
    if file:
        with open(file, 'rb') as f:
            data = bytearray(f.read())
    return data