from pynput.keyboard import Key, Listener
import pyperclip
import time
from happytransformer import HappyTextClassification



happy_tc = HappyTextClassification("BERT", "Hate-speech-CNERG/dehatebert-mono-english")

def on_press(key):
    #print('{0} pressed'.format(key))

    if str(key).strip() == "'\\x03'":
        time.sleep(1)
        copyText = pyperclip.paste()
        result = happy_tc.classify_text(copyText)
        print(result)
        f = open("data.txt","w")
        f.write(copyText+"\n")
        f.write(result.label)
        f.close()

        

def on_release(key):
    #print('{0} release'.format(key))
    if key == Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()