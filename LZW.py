def compress(uncompressed):
    # 產生初始編碼字典 0~127
    dict_size = 128
    dictionary = {chr(i): i for i in range(dict_size)}

    # 初始化，w為空字元，result為空串列
    w = ""
    result = []

    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # 把新的符號(wc)加到字典中.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # 記得要把最後一個符號丟進字串裡面，我還沒上車R。
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    from io import StringIO
    # 產生初始編碼字典 0~127
    dict_size = 128
    dictionary = {i: chr(i) for i in range(dict_size)}

    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # 把新的符號(w+entry[0])加到字典中.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()


# 壓縮它 ! 先編碼，再解碼。
compressed = compress('ABABABABAB')
print (compressed)
decompressed = decompress(compressed)
print (decompressed)