# Write async method (M1)
# write method (M2), which awaits M1
# Create any decorator for method (D1)
# Decorate M2 with D1
# asyncio.run(M2())
import asyncio


def decorator_d1(func_to_decorate):
    async def wrapper(m):
        print("x = 5, y = 8, m will be send as a parametr")
        await func_to_decorate(m)
        print(f"This is a result")
    return wrapper


async def function_m1(m):
    x = 5
    y = 8
    result = x + y + m
    print(f'The expression: x + y + m, where m = {m} is equal: {result}')


@decorator_d1
async def function_m2(m):
    task = asyncio.create_task(function_m1(m))
    await task


asyncio.run(function_m2(12))
