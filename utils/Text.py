from PIL import Image
import pytesseract


def ocr_functon(image):
    """[Returns the result of a Tesseract OCR run on the image to string]

    Args:
        image ([image]): [preprocessed image containing only text]

    Returns:
        [str]: [identified text from image]
    """
    # TODO image needs to pre processed before given into ocr

    return pytesseract.image_to_string(image)


def spellCheck(text):
    # TODO check for spelling mistakes
    pass


def summarizer(text):
    # TODO summarized text
    pass


ocr_functon("text.JPG")

