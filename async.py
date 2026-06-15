import asyncio



#Normal  Function synchronous 

def main():
  print("Hello world")

main()

#Asynchronous Function 

async def main():
  print("Async Function")

asyncio.run(main())
