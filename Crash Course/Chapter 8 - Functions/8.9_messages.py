"""Make a list containing a series of short text messages. Pass the list to a function called show_message(),
which prints each text message. """

txt_msgs = ['text', 'text2', 'text3', 'text4']


def show_message(message):
    while txt_msgs:
        show = message.pop(0)
        print(show)


show_message(txt_msgs)
