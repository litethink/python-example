from sanic import Sanic
from sanic.response import text
from sanic_redis import SanicRedis


app = Sanic(__name__)


app.config.update({
    'REDIS_1': {
        'address': ('127.0.0.1', 6379),
        'db': 0,
    },
    'REDIS_2': {
        'address': ('127.0.0.1', 6379),
        'db': 1,
  }
})


r1 = SanicRedis(app, config_name="REDIS_1")
r2 = SanicRedis(app, config_name="REDIS_2")

#r1 = SanicRedis(config_name="REDIS_1")
#r2 = SanicRedis(config_name="REDIS_2")
#r1.init(app)
#r2.init(app)

@app.route('/test3')
async def test3(request):
    with await r1.conn as r:
        ok = await r.get('key')
    import pdb
    pdb.set_trace()

@app.route('/test4')
async def test4(request):
    with await request.app.redis_1 as r:
        await r.set('key', 'value1')
    with await request.app.redis_2 as r:
        await r.set('key', 'value2')


if __name__ == '__main__':
    app.run(debug=True)
