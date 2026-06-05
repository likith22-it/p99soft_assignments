import asyncio

async def func():
    print(" 1Hello, World!")
    await asyncio.sleep(1)
    print("Continuing...1")
async def func1():
    print(" 2Hello, World!")
    await asyncio.sleep(0.7)
    print("Continuing...2")

async def func2():
    print(" 3Hello, World!")
    await asyncio.sleep(0.5)
    print("Continuing...3")

async def main():
    await asyncio.gather(
        func(),
        func1(),
        func2()
    )

asyncio.run(main())