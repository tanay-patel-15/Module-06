import threading

def busyWork(x):
  while x>0:
    print("The busy work has been carried out " + str(x)  + " times.")
    x -= 1


if __name__ == "__main__":
  first = threading.Thread(target=busyWork, args=(10,)) # Create a new thread that will carry out the busyWork function with argument 10
  # Create two threads, each running the busyWork function with a different argument.
  t1 = threading.Thread(target=busyWork, args=(1005,))   # Arguments are passed as a tuple.
  t2 = threading.Thread(target=busyWork, args=(20,))

  # Start both threads.
  t1.start()
  t2.start()

  # Wait for both threads to finish.
  t1.join()
  t2.join()
  print("Both threads have finished their work.")