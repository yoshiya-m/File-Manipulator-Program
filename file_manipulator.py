import sys


# copy
def copy():
    if len(sys.argv) < 4:
        print('引数が' + str(4 - len(sys.argv)) + 'つ足りません')
        return
    inputPath = sys.argv[2]
    outputPath = sys.argv[3]
    with open(inputPath) as f:
        contents = f.read()

    with open(outputPath, 'w') as f:
        f.write(contents)
    print('copied!')
    return

# reverse
def reverse():
    if len(sys.argv) < 4:
        print('引数が' + str(4 - len(sys.argv)) + 'つ足りません')
        return
    inputPath = sys.argv[2]
    outputPath = sys.argv[3]
    with open(inputPath) as f:
        contents = f.read()
    reversedContents = contents[::-1]

    with open(outputPath, 'w') as f:
        f.write(reversedContents)
    print('reversed!')
    return

# duplicate-contents
def duplicateContents():
    if len(sys.argv) < 4:
        print('引数が' + str(4 - len(sys.argv)) + 'つ足りません')
        return
    inputPath = sys.argv[2]
    n = int(sys.argv[3])
    with open(inputPath) as f:
        contents = f.read()

    with open(inputPath, 'a') as f:
        for i in range(n):
            f.write(contents)
    print('deplicated!')
    return

# replace-string
def replaceString():
    if len(sys.argv) < 5:
        print('引数が' + str(5 - len(sys.argv)) + 'つ足りません')
        return
    inputPath = sys.argv[2]
    needle = sys.argv[3]
    newString = sys.argv[4]
    with open(inputPath) as f:
        contents = f.read()
    newContents = contents.replace(needle, newString)
    with open(inputPath, 'w') as f:
        f.write(newContents)
    print('replaced!')
    return

commands = {
    'copy': copy,
    'reverse': reverse,
    'duplicate-contents':duplicateContents,
    'replace-string': replaceString
}

command = sys.argv[1]

if command not in commands:
    print('command "' + command + '" ' + 'does not exist')
    exit()

commands[command]()

'''
reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

'''