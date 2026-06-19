import asyncio
import time

# Coroutine function
async def main():
    print("Async Function") # This will print immediately
    await asyncio.sleep(1)# The thread is idle here
    print("Async Function after 1 second") # This will be executed right after the thread is idle


asyncio.run(main())


#If I use time here then it's become synchronous 



