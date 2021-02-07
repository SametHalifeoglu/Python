i = 1
while i <= 10:
    print(i)
    i += 1
    print(i)

print("Done with loop")

print("--------------------Guess game with while------------------------------------")

secret_word = "secret"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:

    if guess_count < guess_limit:
        guess = input("Enter the secret word: ")
        guess_count += 1
        print(guess_count)
    else:
        out_of_guess = True

if out_of_guess:
    print("YOU LOSE")
else:
    print("YOU WIN! ")
