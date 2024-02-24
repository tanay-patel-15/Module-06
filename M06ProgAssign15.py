import multiprocessing
import random
import time
from datetime import datetime

def worker():

    wait_time = random.random()

    time.sleep(wait_time)

    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}")

    print("Exiting process.")

if __name__ == "__main__":

    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All processes have finished.")
