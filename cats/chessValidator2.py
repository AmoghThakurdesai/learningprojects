# Write your code here :-)
chessBoard1 = {
    "1h": "bKing",
    "2h": "bPawn",
    "3h": "wQueen",
    "4h": "bBishop",
    "5h": "bQueen",
    "6h": "wKing",
    "7h": "bPawn",
    "8h": "wPawn",

}
def isValidChessBoard(chessBoard):
    boardvalid=['1a','1b','1c','1d','1e','1f','1g','1h',
    '2a','2b','2c','2d','2e','2f','2g','2h',
    '3a','3b','3c','3d','3e','3f','3g','3h',
    '4a','4b','4c','4d','4e','4f','4g','4h',
    '5a','5b','5c','5d','5e','5f','5g','5h',
    '6a','6b','6c','6d','6e','6f','6g','6h',
    '7a','7b','7c','7d','7e','7f','7g','7h',
    '8a','8b','8c','8d','8e','8f','8g','8h']

    #1 black and 1 white king
    bK=0
    wK=0
    for i in chessBoard.values():
        if i=='bKing':
            bK+=1
    if bK!=1:
        print('bKingError')
        return False

    for i in chessBoard.values():
        if i=='wKing':
            wK+=1
    if wK!=1:
        print('wKingError')
        return False

    #each player can have at most 16 pieces
    bpieces=0
    wpieces=0
    for i in chessBoard.values():
        if i[0]=='b':
            bpieces+=1
    if bpieces>16:
        print('bTotalPieceError')
        return False

    for i in chessBoard.values():
        if i[0]=='w':
            wpieces+=1
    if wpieces>16:
        print('wTotalPieceError')
        return False

    #at most 8 pawns for each
    bpawn=0
    wpawn=0
    for i in chessBoard.values():
        if i=='bPawn':
            bpawn+=1
    if bpawn>8:
        print('bTotalPawnError')
        return False

    for i in chessBoard.values():
        if i=='wPawn':
            wpawn+=1
    if wpawn>8:
        print('wTotalPawnError')
        return False

    #all pieces must beon valid space
    for i in chessBoard.keys():
        if i not in boardvalid:
           print('SpaceError')
           return False

    #all must begin with w or b
    for i in chessBoard.values():
        if i[0]=='b' or i[0]=='w':
            continue
        else:
            print('bwNameError')
            return False


    #pawn knight bishop rook queen or king
    for i in chessBoard.values():
        if i[1:]=='Pawn' or i[1:]=='Knight' or i[1:]=='Bishop' or i[1:]=='Rook' or i[1:]=='Queen' or i[1:]=='King':
            continue
        else:
            print('pieceNameError')
            return False

    else:
        return True
print(isValidChessBoard(chessBoard1))
