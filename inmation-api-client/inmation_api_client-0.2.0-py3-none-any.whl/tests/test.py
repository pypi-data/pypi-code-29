import asyncio
import time

loop = asyncio.get_event_loop()

async def receive_forever():
    while True:
        print("receiving ...")        
        await asyncio.sleep(0.01)

def run_async(tasks):
    
    loop.run_until_complete(        
        loop.run_until_complete(asyncio.wait( [receive_forever()] + tasks))
    )

async def task1():
    while True:
        print('task1 ...')        
        await asyncio.sleep(0.01)

async def task2():
    while True:
        print('task2 ...')
        time.sleep(0.5)
        await asyncio.sleep(0.01)

def main():
    run_async([task1(), task2()])

if __name__ == '__main__':
    main()
