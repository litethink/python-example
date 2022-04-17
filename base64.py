import base64

data = "Hello world"
data = "".join(data.split(" ")).lower()
data = base64.b64encode(data.encode("utf8"))
urlsafeb64 = base64.urlsafe_b64encode(data)
base64.b64decode(base64.b64decode(urlsafeb64))

