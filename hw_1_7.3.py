def len_files(files):
    lenght_files = {}
    for i in files:
        with open(i, 'r', encoding='utf8') as f:
            if f.name not in lenght_files:
                lenght_files[f.name] = len(f.readlines())
    return write_file(sorted_files(lenght_files))


def sorted_files(lenghts):
    sorteded_files = {}
    sorted_keys = sorted(lenghts, key=lenghts.get)
    for i in sorted_keys:
        sorteded_files[i] = lenghts[i]
    return sorteded_files


def write_file(files):
    with open('out.txt', 'w', encoding='utf8') as out:
        for k, v in files.items():
            out.write(k + '\n' + str(v) + '\n')
            with open(k, 'r', encoding='utf8') as f:
                line = f.read()
            if line[-1::1] != '\n':
                out.write(line + '\n')
            else:
                out.write(line)


len_files(['1.txt', '2.txt', '3.txt'])
