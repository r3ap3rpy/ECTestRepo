import asyncio
import random

#ANSI Colors
Colors = (
    "\33[0m",
    "\33[36m",
    "\33[91m",
    "\33[35m"
)

async def makerandom(idx, threshold = 6):
    print(Colors[idx + 1] + f"Initiated makerandom({idx}).")
    i =  random.randint(0,10)
    while i <= threshold:
        print(Colors[idx + 1] + f"makerandom({idx}) == {i} too low; retrying!")
        await asyncio.sleep(idx + 1)
        i = random.randint(0,10)
    print(Colors[idx + 1] + f"---> Finished: makerandom({idx}) == {i} too low; retrying!" + Colors[0])
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == '__main__':
    random.seed(55)
    r1, r2, r3 = asyncio.run(main())
    print(f"\nr:1 : {r1},r:2 : {r2},r:3 : {r3}")
