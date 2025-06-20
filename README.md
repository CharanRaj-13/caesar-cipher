# Caesar Cipher Web

This repository contains a simple web application for encrypting and decrypting text using the Caesar cipher. It also includes a brute-force decryption option.

## Features

*   **Encrypt Text:** Encrypts input text using a specified key (1-25).
*   **Decrypt Text:** Decrypts input text using a specified key (1-25).
*   **Brute-Force Decryption:** Attempts to decrypt the input text using all possible keys (1-25) and displays all potential decryptions.
*   **User-Friendly Interface:** A clean web interface built with Flask and Tailwind CSS.
*   **Dark Mode:** Includes a theme toggle for light and dark modes.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CharanRaj-13/caesar-cipher.git
    cd caesar-cipher/caesar_cipher_web
    ```

2.  **Install dependencies:**
    This project uses Flask. Ensure you have Python installed.
    ```bash
    pip install Flask
    ```

3.  **Run the Flask application:**
    ```bash
    python app.py
    ```

4.  **Open in your browser:**
    Navigate to `http://127.0.0.1:5000/` in your web browser.

## File Structure

```
caesar-cipher/
└── caesar_cipher_web/
    ├── app.py             # Flask application logic
    ├── static/
    │   └── style.css      # (Currently empty, Tailwind CSS is used via CDN)
    └── templates/
        └── index.html     # HTML template for the web interface
```

## Functionality

### `app.py`

*   **`caesar_encrypt(text, key)`:** Takes a string `text` and an integer `key` as input. It shifts each alphabetic character in the text by the `key` positions. Non-alphabetic characters remain unchanged.
*   **`caesar_decrypt(text, key)`:** Decrypts text by calling `caesar_encrypt` with a negative key.
*   **`@app.route('/', methods=['GET', 'POST'])`:** Handles requests to the root URL.
    *   **GET:** Renders the main page (`index.html`).
    *   **POST:** Processes the form submission.
        *   Retrieves `text`, `key`, and `mode` (encrypt, decrypt, or brute-force) from the form.
        *   Validates the key (must be between 1 and 25 unless in brute-force mode).
        *   Performs the selected operation:
            *   **Encrypt/Decrypt:** Calls the respective function and displays the result.
            *   **Brute-force:** Iterates through keys 1 to 25, performs decryption for each, and displays all results.
        *   Renders the `index.html` template with the `result`.

### `templates/index.html`

*   A single HTML page that provides the user interface.
*   Uses **Tailwind CSS** for styling (included via CDN).
*   Contains a form with:
    *   A textarea for text input.
    *   An input field for the key (numeric).
    *   A select dropdown for the mode (Encrypt, Decrypt, Brute-force Decrypt).
    *   A submit button.
*   Displays the `result` passed from the Flask application.
*   Includes a JavaScript snippet for toggling between light and dark themes.

## Technologies Used

*   **Python:** Backend programming language.
*   **Flask:** Micro web framework for Python.
*   **HTML:** Structure of the web page.
*   **Tailwind CSS:** Utility-first CSS framework for styling.
*   **JavaScript:** For the theme toggle functionality.
