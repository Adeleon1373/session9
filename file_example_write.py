#lets create a journal\
with open("journal.txt", "w") as journal:
    while True:  # Start a loop to keep taking input
        text = input("Enter a journal entry: (press q to quit): ")
        if text == "q":
            break  # Exit the loop if the user enters 'q'
        journal.write(text + "\n")  # Write the entry to the file
