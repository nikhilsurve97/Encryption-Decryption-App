from tkinter import *
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet cipher object with the key
cipher_suite = Fernet(key)


class EncryptionDecryptionGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Text Encryption and Decryption GUI")
        self.window.geometry('420x420')
        self.window.configure(bg='navy blue')

        # Create the input and output text boxes
        self.input_text = Text(self.window, height=5, width=55)
        self.input_text.configure(bg='grey', font='ariel 10')
        self.output_text = Text(self.window, height=5, width=55)
        self.output_text.configure(bg='grey', font='ariel 10')
        

        # Create the encryption and decryption buttons
        self.encrypt_button = Button(self.window, text="ENCRYPT", command=self.encrypt,bg='Yellow',fg='black',font='roboto 15')
        self.decrypt_button = Button(self.window, text="DECRYPT", command=self.decrypt,bg='Green',fg='black',font='roboto 15')
        self.reset_button= Button(self.window, text="RESET",command=self.reset,bg='red',fg='black',font='roboto 15')
        self.stamp = Label(self.window, text="-Nikhil Surve-",bg='navy blue',fg='white', font='tahoma 15' )

        # Place the widgets on the window
        self.input_text.pack(padx=0, pady=20,)
        self.output_text.pack(padx=10, pady=20)
        self.encrypt_button.place(x=30, y=280,width=150,height=30)
        self.decrypt_button.place(x=250, y=280,width=150,height=30)
        self.reset_button.place(x=120, y=350,width=150,height=30)
        self.stamp.place(x=250,y=400, width=150,height=20)

        # Start the mainloop
        self.window.mainloop()

    def encrypt(self):
        # Get the input text
        input_text = self.input_text.get("1.0", "end-1c")

        # Encrypt the text
        encrypted_text = self.encrypt_text(input_text)

        # Set the output text
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", encrypted_text)

    def decrypt(self):
        # Get the input text
        input_text = self.input_text.get("1.0", "end-1c")

        # Decrypt the text
        decrypted_text = self.decrypt_text(input_text)

        # Set the output text
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", decrypted_text)

    def reset(self):
        #reset input & output text1
        self.input_text.delete(1.0,END)
        self.output_text.delete(1.0,END)
        

    def encrypt_text(self, text):
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(text.encode())
        return encrypted_text
        

    def decrypt_text(self, text):
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(text).decode()
        return decrypted_text
    

if __name__ == "__main__":
    EncryptionDecryptionGUI()