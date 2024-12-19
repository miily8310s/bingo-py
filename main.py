# 入力されるビンゴカードの行数/列数
s = int(input())
# 入力されるビンゴカードを1行ずつ格納した配列
bingoRows = [input().split() for _ in range(s)]
# 入力される単語数
n = int(input())
# 入力されるn個の単語を格納した配列
inputWords = [input() for _ in range(n)]


# 縦か横線でビンゴになっているか否かを返却
def checkLineBingo():
    # 1箇所でも縦か横線でビンゴになっているか否かのフラグ
    isBingo = False
    for row in range(s):
        # 1つの横線で、入力されるn個の単語が含まれていた回数を格納
        rowSum = 0
        # 1つの縦線で、入力されるn個の単語が含まれていた回数を格納
        colSum = 0
        for col in range(s):
            # 1行ごとに右に1文字ずつ単語が含まれるか確認する
            if bingoRows[row][col] in inputWords:
                rowSum += 1
            # 1列ごとに下に1文字ずつ単語が含まれるか確認する
            if bingoRows[col][row] in inputWords:
                colSum += 1
        # 1行/1列すべてで単語が含まれていた時点でループを抜けて、ビンゴであることを返す
        if s == rowSum or s == colSum:
            isBingo = True
            break
    return isBingo


# 斜め線でビンゴになっているか否かを返却
def checkDiagonalBingo():
    # 左上から右下に向けた斜めで、入力されるn個の単語が含まれていた回数を格納
    leftDiagonalSum = 0
    # 右上から左下に向けた斜めで、入力されるn個の単語が含まれていた回数を格納
    rightDiagonalSum = 0
    for row in range(s):
        # 左上から右下に向けた斜めで1文字ずつ確認する
        if bingoRows[row][row] in inputWords:
            leftDiagonalSum += 1
        # 右上から左下に向けた斜めで1文字ずつ確認する
        if bingoRows[row][s - 1 - row] in inputWords:
            rightDiagonalSum += 1
    return s == leftDiagonalSum or s == rightDiagonalSum


if checkLineBingo() or checkDiagonalBingo():
    print("yes")
else:
    print("no")
