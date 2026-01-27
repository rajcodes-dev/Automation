import pyperclip, time

print("Recording Clipboard....(CTRL-C to stop)")
previous_content = ''

try:
    while True:
        content = pyperclip.paste()

        if content != previous_content:
            print(content)
            previous_content = content

            time.sleep(0.01)
except KeyboardInterrupt:
    pass
