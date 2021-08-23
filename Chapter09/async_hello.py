import asyncio
import time
# async and await
# 3.4 -> 3.7 (rapid evolution)

#class Awaitable():
#    def __await__(self):
#        ...

async def counter(name):
    print(f"First : {name}")
    await asyncio.sleep(1)
    print(f"Second : {name}")

async def whatever():
    ...

#def hello():
#    await asyncio.sleep(10)

async def main():
    await asyncio.gather(counter('Frodo'),counter('Sam'),counter('Pippin'),counter('Gimli'),counter('Legolas'),counter('Boromir'),counter('Sauron'))

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"The {__file__} executed in {(end-start):2f} second(s)!")
