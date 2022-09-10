import textwrap
value = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# Wrap this text.
wrapper = textwrap.TextWrapper(width=4)
word_list = wrapper.wrap(text=value) 
# Print each line.
for i in word_list:
    print(i)
#---------------------------------------------
# import textwrap
# def wrap(string, max_width):
#     word_list = textwrap.fill(string, max_width)  
#     return word_list
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)