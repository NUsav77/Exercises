"""Start with a copy of your program from exercise 8.9. Write a function called send_messages() that prints each text
message and moves each message to a new list called sent_messages as it's printed. After calling the function,
print both of your lists to make sure the messages were moved correctly. """

txt_msgs = ['text', 'text2', 'text3', 'text4']
sent_messages = []


def show_message(messages):
    while messages:
        show = messages.pop(0)
        print(show)


def send_message(messages):
    while messages:
        current = messages.pop(0)
        print(current)
        sent_messages.append(current)


send_message(txt_msgs)

print('First list: ', txt_msgs)
print('Second List: ', sent_messages)