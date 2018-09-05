import time
import asyncio


async def io_work(x):
    print("task {} begin".format(x))
    await asyncio.sleep(1)
    print("task{} done".format(x))
    return "done {}".format(x)

start = time.time()
# set a event_loop
loop = asyncio.get_event_loop()
# set tasks
tasks = [ asyncio.ensure_future(io_work(i))for i in range(3)]
# register tasks in event loop
loop.run_until_complete(asyncio.wait(tasks))
end = time.time() - start
# show task.result()
for task in tasks:
    print(task.result())
print("done 3 task after {} s".format(end))