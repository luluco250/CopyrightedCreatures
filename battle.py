from moves import move_list

def single(a, b):
    def turn(attacker, defender):
        print(f"Choose your move, {a.name}:")
        move = choice(move_list)
        move_list[move].execute(attacker, defender)

    while not a.defeated() and not b.defeated():