import multiprocessing
import timeit

from Bob import Bob

class PooledBob():

    bob = Bob()

    messages = {"Tom-ay-to, tom-aaaah-to.", "WATCH OUT!",
                "Does this cryogenic chamber make me look fat?",
                "Let's go make out behind the gym!",
                "WHAT THE HELL WERE YOU THINKING?"}

    def respond_to_messages(self, messages, q):
        for message in messages:
            msg = self.bob.hey(message)
            q.put(msg)

    def print_answers(self, q):
        print("Print Queued answers:")

        while not q.empty():
            print(q.get())

        print("Queue is now empty")

    def run_it(self):
        q = multiprocessing.Queue()

        p1 = multiprocessing.Process(target=pooled_bob.respond_to_messages, args=(self.messages, q,))
        p2 = multiprocessing.Process(target=pooled_bob.print_answers, args=(q,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

if __name__ == '__main__':

    pooled_bob = PooledBob()

    def test_func():
        pooled_bob.run_it()

    duration = timeit.timeit(test_func, number=1000)

    print(duration)