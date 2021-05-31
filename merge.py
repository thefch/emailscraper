lines_seen = set()
with open("result.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            lines_seen.add(i)
    f.truncate()
with open("result.txt", "r") as txt_file:
	new_data = list(set(txt_file))
	print(new_data)