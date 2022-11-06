def greeting(ip,style_char='*',spacing=5):
    op_length = (2*spacing) + len(ip)
    styled_line = style_char*op_length
    print(styled_line)
    print(f'{ip:^{op_length}}')
    print(styled_line)
    
greeting('apple')
greeting('hi',style_char='=')
greeting('sibi', spacing=2, style_char='%')
greeting('mona',spacing=3, style_char=':')
