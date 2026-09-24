def checkmate(board):
    # แปลง board string เป็นแต่ละแถว
    rows = board.splitlines()

    # เช็กว่า board ใช้งานได้
    if not rows:
        return

    size = len(rows)

    # board ต้องเป็นสี่เหลี่ยมจัตุรัส
    for row in rows:
        if len(row) != size:
            return

    # หา King
    king_positions = []

    for r in range(size):
        for c in range(size):
            if rows[r][c] == "K":
                king_positions.append((r, c))

    # ต้องมี King แค่ 1 ตัว
    if len(king_positions) != 1:
        return

    king_r, king_c = king_positions[0]

    # ตัวหมากที่ถือว่า "บังทาง" ได้
    pieces = "KPRBQ"

    # -----------------------
    # เช็ก Pawn
    # Pawn เดินโจมตีเฉียงขึ้น
    # เพราะงั้น P ที่โจมตี King ต้องอยู่ด้านล่างของ King
    # -----------------------
    pawn_row = king_r + 1

    if pawn_row < size:
        if king_c - 1 >= 0:
            if rows[pawn_row][king_c - 1] == "P":
                print("Success")
                return

        if king_c + 1 < size:
            if rows[pawn_row][king_c + 1] == "P":
                print("Success")
                return

    # -----------------------
    # เช็ก Rook / Queen
    # บน ล่าง ซ้าย ขวา
    # -----------------------
    straight_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in straight_directions:
        r = king_r + dr
        c = king_c + dc

        while 0 <= r < size and 0 <= c < size:
            square = rows[r][c]

            if square in pieces:
                if square == "R" or square == "Q":
                    print("Success")
                    return

                # เจอหมากอื่นก่อน -> บังทาง
                break

            r += dr
            c += dc

    # -----------------------
    # เช็ก Bishop / Queen
    # แนวทแยง 4 ทิศ
    # -----------------------
    diagonal_directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in diagonal_directions:
        r = king_r + dr
        c = king_c + dc

        while 0 <= r < size and 0 <= c < size:
            square = rows[r][c]

            if square in pieces:
                if square == "B" or square == "Q":
                    print("Success")
                    return

                # เจอหมากอื่นก่อน -> บังทาง
                break

            r += dr
            c += dc

    # ไม่มีตัวไหนโจมตี King
    print("Fail")
