#Solution for the Pawn Brotherhood problem on checkio: https://py.checkio.org/mission/pawn-brotherhood/

def safe_pawns(pieces):
    list_of_squares = list(pieces)
    columns = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

    safe_list = []
    for piece in list_of_squares:
        row = piece[1]

        for i in list_of_squares:


            if int(i[1]) - 1 == int(row):

                col = piece[0]
                if columns[i[0]] + 1 == columns[col] or columns[i[0]] - 1 == columns[col]:
                    safe_list.append(i)

                else:
                    continue

            else:
                continue

    return len(set(safe_list))









#testing
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns(["a1","a2","a3","a4","h1","h2","h3","h4"]))
print(safe_pawns(["b4","c4","d4","e4","f4","g4","e3"]))
