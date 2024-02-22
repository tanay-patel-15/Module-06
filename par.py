import multiprocessing as mp



if __name__ == "__main__":
  cores = mp.Pool(mp.cpu_count())

  print(cores)