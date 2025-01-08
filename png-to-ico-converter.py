from PIL import Image


def png_to_ico(input_png, output_ico, sizes=[16, 32, 48, 64, 128, 256]):
    """
    Converts a PNG file to an ICO file with specified sizes.

    Args:
        input_png (str): Path to the input PNG file.
        output_ico (str): Path to the output ICO file.
        sizes (list): List of sizes for the ICO file (default: [16, 32, 48, 64, 128, 256]).
    """
    try:
        # Open the PNG image
        img = Image.open(input_png)

        # Convert and save as ICO
        img.save(output_ico, format="ICO", sizes=[(size, size) for size in sizes])
        print(f"Successfully converted {input_png} to {output_ico}.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
input_png_path = "Logo-Paint-Innovators.png"  # Replace with your PNG file path
output_ico_path = "favicon.ico"  # Replace with the desired ICO file path

png_to_ico(input_png_path, output_ico_path)
