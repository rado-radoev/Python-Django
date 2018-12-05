import multiprocessing
import timeit

from Bob import Bob

class PooledBob():

    bob = Bob()

    def asK_bob(self, message):
        self.bob.hey(message)

if __name__ == '__main__':
    messages = {"Tom-ay-to, tom-aaaah-to.", "WATCH OUT!",
                "Does this cryogenic chamber make me look fat?",
                "Let's go make out behind the gym!",
                "WHAT THE HELL WERE YOU THINKING?"}

    pooled_bob = PooledBob()

    p = multiprocessing.Pool()

    def test_func():
        p.map(pooled_bob.asK_bob, messages)

    duration = timeit.timeit(test_func, number=1000000)
    print(duration)