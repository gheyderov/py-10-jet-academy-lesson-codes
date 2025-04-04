
import time
import threading, multiprocessing
import requests
import uuid

def do_something():
    print('Process Start!')
    response = requests.get('https://picsum.photos/200/300')
    with open(f'images/image_{uuid.uuid4()}.png', 'wb') as file:
        file.write(response.content)
    print('Process End!')


t1 = time.time()

threads = []

if __name__ == '__main__':
    for i in range(10):
        th1 = multiprocessing.Process(target=do_something)
        th1.start()
        threads.append(th1)

    for th in threads:
        th.join()


t2 = time.time()

print(t2 - t1)