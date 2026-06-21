import asyncio
import time



async def basics():
  print("Async Function")
  time.sleep(3)
  print("Hello World")

#Even though function is async but thread is locked due to time is synchronous so for making 
thread to be used we have to use async function inside this.


async def moderate():
  print("Async Function")
  asyncio.sleep(3)
  print("Hello world")

#This function solve the problem of above function here is not locked at asyncio.sleep()
it will directly print Hello world without waiting 3minutes




# Coroutine function
async def hard():
    print("Async Function") # This will print immediately
    await asyncio.sleep(1)# The thread is idle here
    print("Async Function after 1 second") # This will be executed right after the thread is idle


asyncio.run(main())


#If I use time here then it's become synchronous 