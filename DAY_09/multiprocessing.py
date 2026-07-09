from multiprocessing import Process
def apple():
    print("Apple")
def banana():
    print("Banana")
if __name__ == "__main__":
    p1 = Process(target=apple)
    p2 = Process(target=banana)
    p1.start()
    p2.start()
    p1.join()
    p2.join()