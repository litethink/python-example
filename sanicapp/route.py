from app import App
@App.app.route("/index")
async def test(request):
  return json({"hello": "world"})


