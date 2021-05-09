import asyncio
import time

async def async_call(x: int = 1):
    print('One')
    # await asyncio.sleep(x)
    time.sleep(x)
    print('two')

def test_coroutine():
    print('start thread')
    y = 10
    x = yield y
    y -= 1
    print('x is: ', x)

def f_wrapper(func_iterable):
    print('wrap start...')
    # for item in func_iterable:
    #     yield item
    yield from func_iterable
    print('wrap end')

def fab(maxValue):
    n, a, b = 0, 0, 1
    while n < maxValue:
        yield b
        a, b = b, a + b
        n += 1

if __name__ == "__main__":
    # wrap = f_wrapper(fab(5))
    # print(next(wrap))
    coros = [async_call(1), async_call(3)]
    # print(asyncio.iscoroutinefunction(async_call))
    asyncio.run(async_call(3))