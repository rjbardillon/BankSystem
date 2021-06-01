def get_int(prompt):
    while True:
        try:
            answer = int(input(prompt))
            break
        except ValueError:
            print("Numbers only!")
    return answer
