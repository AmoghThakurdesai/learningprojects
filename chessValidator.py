# Write your code here :-)
chessBoard1 = {
    "1h": "bKing",
    "2h": "bKing",
    "6c": "wQueen",
    "2g": "bBishop",
    "5h": "bQueen",
    "3e": "wKing",
    "3f": "bPawn",
    "3g": "wPawn"
}


def isValidChessBoard(chessBoard):
    bK = 0
    wK = 0
    bP = 0
    wP = 0
    bB = 0
    wB = 0
    wN = 0
    bN = 0
    bR = 0
    wR = 0
    bQ = 0
    wQ = 0
    bPieces = bK + bP + bN + bR + bQ + bB
    wPieces = bK + bP + bN + bR + bQ + bB
    boardvalid = [
        "1a",
        "1b",
        "1c",
        "1d",
        "1e",
        "1f",
        "1g",
        "1h",
        "2a",
        "2b",
        "2c",
        "2d",
        "2e",
        "2f",
        "2g",
        "2h",
        "3a",
        "3b",
        "3c",
        "3d",
        "3e",
        "3f",
        "3g",
        "3h",
        "4a",
        "4b",
        "4c",
        "4d",
        "4e",
        "4f",
        "4g",
        "4h",
        "5a",
        "5b",
        "5c",
        "5d",
        "5e",
        "5f",
        "5g",
        "5h",
        "6a",
        "6b",
        "6c",
        "6d",
        "6e",
        "6f",
        "6g",
        "6h",
        "7a",
        "7b",
        "7c",
        "7d",
        "7e",
        "7f",
        "7g",
        "7h",
        "8a",
        "8b",
        "8c",
        "8d",
        "8e",
        "8f",
        "8g",
        "8h",
    ]
    while True:
        for i in chessBoard.keys():
            if i not in boardvalid:
                return False
        if "bKing" not in chessBoard.values():
            print("bK error")
            return False
        if "wKing" not in chessBoard.values():
            print("wK error")
            return False
        for i in chessBoard.values():
            if "bKing" in chessBoard.values():
                bK += 1
        break
        print(bK)
        for i in chessBoard.values():
            if "wKing" in chessBoard.values():
                wK += 1
        break
        print(wK)

        for i in chessBoard.values():
            if "bPawn" in chessBoard.values():
                bP += 1
        break
        print(bP)

        for i in chessBoard.values():
            if "wPawn" in chessBoard.values():
                wP += 1
        break
        print(wP)


    if (
        bK > 1
        or wK > 1
        or bP > 8
        or wP > 8
        or bPieces > 16
        or wPieces > 16
    ):
        return False
    else:
        return True


if isValidChessBoard(chessBoard1) == True:
    print("Yes")
elif isValidChessBoard(chessBoard1) == False:
    print("No")
