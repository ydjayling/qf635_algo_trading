"""
By default, asyncio.run() executes the coroutines in the current main thread.

We are going to create a new thread to runs the coroutines.

"""
import logging
import asyncio
import time
import random
from threading import Thread

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


def start():
    loop_thread = Thread(target=run_async_task, daemon=True, name='Async Thread')
    loop_thread.start()


def run_async_task():
    # create a new event loop to run task by the calling thread
    loop = asyncio.new_event_loop()

    # create task and add it to the event loop
    loop.create_task(print_forever())

    # run the event loop until stop() is called
    loop.run_forever()


# TODO define a coroutine that continuously print a random number once a second in a while loop
async def print_forever():
    while 1:
        logging.info(f"Random number: {random.randint(1, 100)}")
        await asyncio.sleep(1)

if __name__ == '__main__':
    # start the background task
    start()
    while True:
        time.sleep(5)
        logging.info('sanity check')

