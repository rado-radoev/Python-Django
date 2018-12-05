import threading
import timeit

from Bob import Bob

exitFlag = 0

class ThreadedBob (threading.Thread):

    def askBob(self, ask_bob_what, lock):
        bob = Bob()

        lock.acquire()
        bob.hey(ask_bob_what)
        lock.release()


    def main_task(self, message):
        lock = threading.Lock()

        t = threading.Thread(target=self.askBob, args=(message, lock,))

        t.start();

        t.join()


if __name__ == '__main__':
    tb = ThreadedBob()

    messages = {"Tom-ay-to, tom-aaaah-to.", "WATCH OUT!",
                "Does this cryogenic chamber make me look fat?",
                "Let's go make out behind the gym!",
                "WHAT THE HELL WERE YOU THINKING?"}
    def test_func():
        for message in messages:
            tb.main_task(message)

    duration = timeit.timeit(test_func, number=1000)
    print(duration)