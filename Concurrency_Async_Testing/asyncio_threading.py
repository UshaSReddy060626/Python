import asyncio
import threading
async def morning():
    print("Good Morning")
async def evening():
    print("Good Evening")
async def main():
    await asyncio.gather(
        morning(),
        evening()
    )
def thread_work():
    print("Thread is running")
t = threading.Thread(target=thread_work)
t.start()
asyncio.run(main())
t.join()