import time

def io_work(x):
    print("task {} begin".format(x))
    time.sleep(1)
    print("task{} done".format(x))
    return "done {}".format(x)

results = []
start = time.time()
for i in range(3):
    results.append(io_work(i))
end = time.time() - start
print("done 3 task after {} s".format(end))
