# VS Pass Manager by Vladislav Slugin [vsdev.]

SecurePass Manager is a simple, yet powerful password manager application written in Python. It uses the `cryptography` library for encrypting and decrypting passwords, ensuring that your sensitive information is stored securely.

## Features

- **Add and save passwords** with associated websites, usernames, and comments.
- **Encrypt passwords** using the Fernet symmetric encryption method.
- **Copy passwords** to clipboard with a single click.
- **Open websites** directly from the application.
- **Delete passwords** easily when they are no longer needed.
- **Simple and intuitive GUI** built with `tkinter`.

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Add a password**:
    - Enter the website, username, password, and any comments.
    - Click "Save Password".

3. **Load passwords**:
    - Click "Load Passwords" to display all saved passwords.

4. **Copy a password**:
    - Select an entry from the list.
    - Click "Copy Password" to copy the decrypted password to the clipboard.

5. **Open a website**:
    - Select an entry from the list.
    - Click "Open Website" to open the website in your default browser.

6. **Delete a password**:
    - Select an entry from the list.
    - Click "Delete Password" to remove the entry from the list and the storage.

![image](https://github.com/user-attachments/assets/fbebd717-23aa-4766-9fd8-4a0dc206748e)

## File Structure

- `main.py`: The main script that runs the application.
- `requirements.txt`: A list of Python packages required to run the application.

## Security

- Passwords are encrypted using the Fernet symmetric encryption method provided by the `cryptography` library.
- A unique key is generated and stored in `key.key` file upon first run, which is used for encryption and decryption.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements, bug fixes, or features.


## Acknowledgements

- [cryptography](https://cryptography.io/en/latest/) - A package designed to expose cryptographic recipes and primitives to Python developers.
- [tkinter](https://docs.python.org/3/library/tkinter.html) - The standard Python interface to the Tk GUI toolkit.

---

Authored by Vladislav Slugin [vsdev.].
