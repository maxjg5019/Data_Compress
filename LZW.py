def compress(uncompressed):
    # 產生初始編碼字典 0~127
    Dict_size = 128
    Dictionary = {chr(i): i for i in range(Dict_size)}

    # 初始化，Previous為空字元，Result為空串列
    Previous = ""
    Result = []
    for Current in uncompressed:
        print("Previous:" + Previous)
        print("Current:" + Current)
        PC = Previous + Current
        print("PC:" + PC)
        if PC in Dictionary:
            Previous = PC
            print("PC有找到，P=P+C:" + Previous)
        else:
            Result.append(Dictionary[Previous])
            print("PC沒找到，輸出 Previous: " + str(Dictionary[Previous]))
            # print(Dictionary[Previous])
            # 把新的符號(PC)加到字典中.
            Dictionary[PC] = Dict_size
            print("新增 " + PC + "到字典並編碼:" + str(Dict_size) )
            Dict_size += 1
            Previous = Current
            print("更新:Previous =  " + Previous)
        print("----------")
    
    # 記得要把最後一個符號丟進字串裡面，我還沒上車R。
    if Previous:
        Result.append(Dictionary[Previous])
        print("我還沒上車R，輸出 Previous " + str(Dictionary[Previous]))
    return Result
    
def decompress(compressed):
    from io import StringIO
    # 產生初始編碼字典 0~127
    Dict_size = 128
    Dictionary = {i: chr(i) for i in range(Dict_size)}

    Result = StringIO()
    Word = chr(compressed.pop(0))
    Result.write(Word)
    for Code in compressed:
        if Code in Dictionary:
            Entry = Dictionary[Code]
        elif Code == Dict_size:
            Entry = Word + Word[0]
        else:
            raise ValueError('Bad compressed k: %s' % Code)
        Result.write(Entry)

        # 把新的符號(Word+Entry[0])加到字典中.
        Dictionary[Dict_size] = Word + Entry[0]
        Dict_size += 1

        Word = Entry
    return Result.getvalue()


# 壓縮它 ! 先編碼，再解碼。
compressed = compress('ABABBA')
print (compressed)
print("編碼結束")
decompressed = decompress(compressed)
print (decompressed)
print("解碼結束")