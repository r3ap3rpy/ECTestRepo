import asyncio

def whatever():
    ...

@asyncio.coroutine
def python34coroutine():
    yield from whatever()

async def python37coroutine():
    await whatever()