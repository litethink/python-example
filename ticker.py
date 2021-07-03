import asyncio

loop = asyncio.get_event_loop()

def f():
    print("foo")

def tick():
    f()
    loop.call_later(1,tick)
# loop.create_task(f)

loop.call_later(3,tick)
loop.run_forever()
