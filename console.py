
MAX_MESSAGES = 10
messages = []

def Write(message):
    messages.insert(0, message)
    if (len(messages)) > MAX_MESSAGES:
        del messages[len(messages) - 1]