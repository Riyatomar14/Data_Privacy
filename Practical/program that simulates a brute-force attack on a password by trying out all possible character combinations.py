# using dictionary 
my_dict = {
    1: "alpha",
    2: "bravo",
    3: "charlie",
    4: "delta",
    5: "echo",
    6: "magic"
}
attempt=0
secret_password = "magic"

for key, word in my_dict.items():
    print(f"Trying: {word}")
    attempt += 1
    if word == secret_password:
        print(f"Password found! It is: {word}")
        break
print (f"attempt: {attempt}")


# using string
