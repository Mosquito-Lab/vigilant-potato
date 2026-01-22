from pathlib import Path

def get_image(image_name:str):
    """ Gets the filepath for the given image. """

    image_dir = Path(__file__).resolve().parent
    image= image_dir / image_name
    image_path = str(image.absolute())

    return image_path

