import multiprocessing

from Bob import Bob

class ManagerBob():

    bob = Bob()

    def __init__(self):
        pass

    def print_list_of_messages(self, messages):
       for message in messages:
           print(self.bob.hey(message))

    def add_new_message(self, messages, message):
        messages.append(message)


if __name__ == '__main__':
    default_messages = {"Tom-ay-to, tom-aaaah-to.", "WATCH OUT!",
                        "Does this cryogenic chamber make me look fat?",
                        "Let's go make out behind the gym!",
                        "WHAT THE HELL WERE YOU THINKING?"}


    manager_bobber = ManagerBob()

    with multiprocessing.Manager() as manager:
        records = manager.list(default_messages)

        new_message = list("Okay if like my  spacebar  quite a bit?   ")

        p1 = multiprocessing.Process(target=manager_bobber.add_new_message, args=(records, new_message, ))
        p2 = multiprocessing.Process(target=manager_bobber.print_list_of_messages, args=(records,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()









