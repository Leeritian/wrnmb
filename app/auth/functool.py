def win_txt_write(filename, content):
    with open(filename, 'a') as f:
        f.write(content + '\n')


