while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print("Try again, please enter a number")
    else:
        print('It is a number:', num ** num)
