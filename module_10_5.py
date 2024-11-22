import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    try:
        with open(name, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line)
    except FileNotFoundError:
        print(f"Файл {name} не найден.")
    return all_data


def linear(filenames):
    start_time = time.time()
    for file_name in filenames:
        read_info(file_name)
    end_time = time.time()
    print(f"{end_time - start_time:.2f} (Линейный).")


def multiproc(filenames):
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"{end_time - start_time:.2f} (многопроцессорный).")

if __name__ == "__main__":
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
    linear(filenames)
    multiproc(filenames)
