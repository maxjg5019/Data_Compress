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
            print("PC有找到,P=P+C:" + Previous)
        else:
            Result.append(Dictionary[Previous])
            print("PC沒找到,輸出 Previous: " + str(Dictionary[Previous]))
            # print(Dictionary[Previous])
            # 把新的符號(PC)加到字典中.
            Dictionary[PC] = Dict_size
            print("新增 " + PC + "到字典並編碼:" + str(Dict_size))
            Dict_size += 1
            Previous = Current
            print("更新:Previous =  " + Previous)
        print("----------")
    
    # 記得要把最後一個符號丟進字串裡面，我還沒上車R。
    if Previous:
        Result.append(Dictionary[Previous])
        print("我還沒上車R,輸出 Previous " + str(Dictionary[Previous]))
    return Result
    
def decompress(compressed):
    from io import StringIO
    # 產生初始編碼字典 0~127
    Dict_size = 128
    Dictionary = {i: chr(i) for i in range(Dict_size)}

    Result = StringIO()
    print("Cw讀取第一個符號: " + str(compressed[0]))
    Word = chr(compressed.pop(0))
    print("解碼輸出Cw(): " + Word)
    print("----------")
    Result.write(Word)
    for Code in compressed:
        if Code in Dictionary:
            Entry = Dictionary[Code]
            print("Cw有找到,解碼當前Cw: " + str(Code) +
             " 輸出Cw(): " + Entry)
        elif Code == Dict_size:
            Entry = Word + Word[0]
            # 這邊需要通靈一下，按照編碼邏輯才能篤定解碼時直接輸出
            print("Cw沒找到,紀錄當前符號 " + 
            Entry + " 為: " + str(Code) + " 同時直接輸出P+C: " + Entry)
        Result.write(Entry)
        # 把新的符號(Word+Entry[0])加到字典中.
        Dictionary[Dict_size] = Word + Entry[0]
        print("新增P+C符號: " + str(Dictionary[Dict_size]))
        Dict_size += 1
        Word = Entry
        print("----------")    
    return Result.getvalue()


# 壓縮它 ! 先編碼，再解碼。
compressed = compress('ABABBA') # ABABCABABAC 可測試通靈那部分
print (compressed)
print("編碼結束")
print()
decompressed = decompress(compressed)
print (decompressed)
print("解碼結束")