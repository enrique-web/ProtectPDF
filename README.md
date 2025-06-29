# ProtectPDF

A simple Python utility to add password protection and encryption to PDF files using the `pypdf` library.

## Description

ProtectPDF allows you to secure your PDF documents by applying password protection and encryption. Using the `pypdf` library, you can easily restrict access to your PDFs, preventing unauthorized viewing, copying, or printing.

## Features

- Add user password to restrict opening the PDF
- Add owner password to restrict permissions (copying, printing, etc.)
- Supports 128-bit AES encryption
- Simple and minimal code usage
- Compatible with Python 3.x

## Installation

Install the required library using pip:

```
pip install pypdf
```

## Usage

Example code to protect a PDF file with a password:

```
from pypdf import PdfReader, PdfWriter

def protect_pdf(input_pdf_path: str, output_pdf_path: str, user_password: str, owner_password: str = None):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Copy all pages to writer
    for page in reader.pages:
        writer.add_page(page)

    # Encrypt PDF with user and owner passwords
    writer.encrypt(user_password=user_password, owner_password=owner_password, use_128bit=True)

    # Write the protected PDF to output
    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

    print(f"Protected PDF saved to: {output_pdf_path}")

if __name__ == "__main__":
    input_pdf = "input.pdf"
    output_pdf = "protected_output.pdf"
    user_pwd = "userpass123"
    owner_pwd = "ownerpass456"
    protect_pdf(input_pdf, output_pdf, user_pwd, owner_pwd)
```

## Notes

- The **user password** is required to open the PDF.
- The **owner password** controls permissions such as printing, copying, and modifying the document.
- If no owner password is provided, the user password will be used for both.
- Encryption uses 128-bit AES by default for strong security.

## Contributing

Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```
