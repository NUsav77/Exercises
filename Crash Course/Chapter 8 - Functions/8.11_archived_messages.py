"""Start with your work from exercise 8.10. Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your lists to show that the original list has retained its messages. """


txt_msgs = ['text', 'text2', 'text3', 'text4']
message_copy = txt_msgs[:]
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


send_message(message_copy)

print('First list: ', txt_msgs)
print('Second List: ', sent_messages)
