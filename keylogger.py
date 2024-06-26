from pynput import keyboard

def capture_keys():
    filename = "key_capture.txt"
    print("Key capture started. Press 'x' to stop.")

    def on_press(key):
        try:
            with open(filename,"a") as file:
                file.write('{0}\n'.format(key.char))
        except AttributeError:
            #handle special keys (e.g., space, enter etc.)
            with open(filename,"a") as file:
                file.write('{0}\n'.format(key))
    def on_release(key):
        if key == keyboard.Key.esc or (hasattr(key, 'char') and key.char == 'x'):
            print("Key capture stopped.")
            return False
    
    # Start listening to the keyboard events 
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    capture_keys()
