import asyncio



#Synchronous Function 

def main():
  print("Hello world")

main()

#Asynchronous Function 

async def main():
  print("Async Function")

asyncio.run(main())
