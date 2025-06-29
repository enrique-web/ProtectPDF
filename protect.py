from pypdf import PdfReader, PdfWriter

def protect_pdf(input_pdf_path: str, output_pdf_path: str, user_password: str, owner_password: str = None, 
                allow_printing: bool = False, allow_copying: bool = False):
    """
    Protect a PDF by adding password encryption.

    Parameters:
    - input_pdf_path: str, path to the input PDF file.
    - output_pdf_path: str, path to save the protected PDF file.
    - user_password: str, password required to open the PDF.
    - owner_password: str or None, password for owner permissions (if None, user_password will be used).
    - allow_printing: bool, allow printing if True.
    - allow_copying: bool, allow copying content if True.
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Copy all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Set permissions flags
    from pypdf.constants import Permissions
    permissions = 0
    if allow_printing:
        permissions |= Permissions.PRINTING
    if allow_copying:
        permissions |= Permissions.COPY

    # Use owner_password same as user_password if not provided
    if owner_password is None:
        owner_password = user_password

    # Encrypt PDF with passwords and permissions
    writer.encrypt(
        user_password=user_password,
        owner_password=owner_password,
        permissions=permissions
    )

    # Write the protected PDF to disk
    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

    print(f"Protected PDF saved to: {output_pdf_path}")

# Example usage
if __name__ == "__main__":
    input_pdf = "example.pdf"             # Path to your input PDF
    output_pdf = "protected_example.pdf" # Path to save the protected PDF
    user_pwd = "userpass123"              # Password to open the PDF
    owner_pwd = "ownerpass456"            # Owner password (optional)

    protect_pdf(input_pdf, output_pdf, user_pwd, owner_pwd, allow_printing=True, allow_copying=False)
