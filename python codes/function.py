def greeting(ip):
    op_length = 15 + len(ip)
    styled_line = '*'*op_length
    print(styled_line)
    print(f'{ip:^{op_length}}')
    print(styled_line)
greeting('apple')
greeting('hi')
greeting('sibi')
