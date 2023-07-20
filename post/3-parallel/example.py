import time
import random
from concurrent.futures import ThreadPoolExecutor
import asyncio


def my_function(parameter1, parameter2):
    new_value = f'{parameter1} and {parameter2}'
    # fake delay
    time.sleep(random.randint(1, 5))
    print(new_value)


async def main():
    # change this to your needs
    WORKERS = 8
    # example of the set of parameters you may have for each execution
    parameters = [
        ('first_a', 'first_b'),
        ('second_a', 'second_b'),
        ('third_a', 'third_b'),
    ]
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        loop = asyncio.get_event_loop()
        futures = [loop.run_in_executor(executor, my_function, a, b) for a, b in parameters]
        for response in await asyncio.gather(*futures):
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
