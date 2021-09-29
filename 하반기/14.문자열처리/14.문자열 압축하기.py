init_s = input()
cur_s = init_s
zip_size = len(init_s) // 2
while zip_size:
    i = 0
    next_s = []
    while i + zip_size <= len(cur_s) - zip_size:
        if cur_s[i: i + zip_size] == cur_s[i + zip_size: i + 2 * zip_size] and cur_s[i: i + zip_size].isalpha():
            zip_s = cur_s[i: i + zip_size]
            count = 2
            while True:
                if i + (count + 1) * zip_size <= len(cur_s) and cur_s[i + count * zip_size: i + (
                        count + 1) * zip_size] == zip_s:
                    count += 1
                else:
                    break
            next_s.append(str(count) + '(' + zip_s + ')')
            i += count * zip_size
        else:
            next_s.append(cur_s[i])
            i += 1
    if i < len(cur_s):
        next_s.append(cur_s[i:])
    cur_s = "".join(next_s)
    zip_size = min(len(cur_s) // 2, zip_size - 1)
    print(cur_s)
print(len(cur_s) if len(cur_s) < len(init_s) else len(init_s))
