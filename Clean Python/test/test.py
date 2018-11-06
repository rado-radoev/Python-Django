#   region split string
# st = 'Print only the words that start with s in this sentence'
# edited = st.split(" ")
# print(edited)
#
# wordsWithS = [word for word in edited if word.lower().startswith("s")]
# print(wordsWithS)
#   endregion



#print ( [num for num in range(51) if num % 3 == 0] )


# st = 'Print every word in this sentence that has an even number of letters'
# splitted = st.split(" ")
# print ( [word for word in splitted if len(word) % 2 == 0] )

for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)



# st = 'Create a list of the first letters of every word in this string'
# splitted = st.split(" ");
#
# print ([word[0] for word in splitted])


st = 'Print only the words that start with s in this sentence'
print ([word[0] for word in st.split()])

