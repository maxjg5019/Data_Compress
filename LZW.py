def compress(uncompressed):
    # 產生初始編碼字典 0~127
    Dict_size = 128
    Dictionary = {chr(i): i for i in range(Dict_size)}

    # 初始化，Previous為空字元，Result為空串列
    Previous = ""
    Result = []

    for Current in uncompressed:
        Word = Previous + Current
        if Word in Dictionary:
            Previous = Word
        else:
            Result.append(Dictionary[Previous])
            # 把新的符號(Word)加到字典中.
            Dictionary[Word] = Dict_size
            Dict_size += 1
            Previous = Current

    # 記得要把最後一個符號丟進字串裡面，我還沒上車R。
    if Previous:
        Result.append(Dictionary[Previous])
    return Result


def decompress(compressed):
    from io import StringIO
    # 產生初始編碼字典 0~127
    Dict_size = 128
    Dictionary = {i: chr(i) for i in range(Dict_size)}

    Result = StringIO()
    Word = chr(compressed.pop(0))
    Result.write(Word)
    for k in compressed:
        if k in Dictionary:
            Entry = Dictionary[k]
        elif k == Dict_size:
            Entry = Word + Word[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        Result.write(Entry)

        # 把新的符號(Word+Entry[0])加到字典中.
        Dictionary[Dict_size] = Word + Entry[0]
        Dict_size += 1

        Word = Entry
    return Result.getvalue()


# 壓縮它 ! 先編碼，再解碼。
compressed = compress('ABABABABAB')
print (compressed)
decompressed = decompress(compressed)
print (decompressed)