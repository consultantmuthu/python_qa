def capitalize(name):
    name_list = name.split(' ') # Not having space killed me in unix
    cap_name_list = ' '.join([name.capitalize() for name in name_list])
    return cap_name_list

if __name__ == '__main__':
    capitalize("hello world")
    capitalize("hello   world  lol")
    capitalize("132 456 Wq  m e")
    capitalize("q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M")