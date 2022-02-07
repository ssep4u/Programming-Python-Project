check = input()
s_list = ['1', '2', '3']

if check == s_list[0]:
    file = open('미림마이스터고.txt', 'r', encoding="UTF-8")
    m_lines = file.readlines()
    for m_line in m_lines:
        m_lis = int(m_line)
        m = m_lis + 1
        print(m)

    file = open('미림마이스터고.txt', 'w', encoding="UTF-8")
    file.write(str(m))
    file.close()


elif check == s_list[1]:
    file = open('선린인터넷고.txt', 'r', encoding="UTF-8")
    s_lines = file.readlines()
    for s_line in s_lines:
        s_lis = int(s_line)
        s = s_lis + 1
        print(s)

    file = open('선린인터넷고.txt', 'w', encoding="UTF-8")
    file.write(str(s))
    file.close()

elif check == s_list[2]:
    file = open('디지털미디어고.txt', 'r', encoding="UTF-8")
    d_lines = file.readlines()
    for d_line in d_lines:
        d_lis = int(d_line)
        d = d_lis + 1
        print(d)

    file = open('디지털미디어고.txt', 'w', encoding="UTF-8")
    file.write(str(d))
    file.close()


