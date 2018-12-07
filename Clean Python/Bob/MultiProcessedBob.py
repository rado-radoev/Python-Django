import multiprocessing
import timeit
from ctypes import c_char_p

from Bob import Bob

class MultiProcessedBob():

    bob = Bob()

    def asK_bob(self, message, lock):
        lock.acquire()

        self.bob.hey(message)

        lock.release()


def perform_transactions(message, multi_process_bob_object):

    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=multi_process_bob_object.asK_bob, args=(message, lock,))

    p1.start()

    p1.join()

if __name__ == '__main__':
    messages = {"Tom-ay-to, tom-aaaah-to.", "WATCH OUT!",
                "Does this cryogenic chamber make me look fat?",
                "Let's go make out behind the gym!",
                "WHAT THE HELL WERE YOU THINKING?"}

    mpb = MultiProcessedBob()

    def test_func():
        for message in messages:
            perform_transactions(message, mpb)

    duration = timeit.timeit(test_func, number=1000)

    print(duration)