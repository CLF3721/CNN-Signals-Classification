



import asyncio
import os
import time
from typing import Any

import pytesseract
import pdf2image


API_URL = "nlpapi.some"
DIR_PATH = './data'

async def read_image(image: Any) -> Any:
    return pytesseract.image_to_string(image, output_type=pytesseract.Output.STRING)


async def process_file(filepath: str) -> Any:
    """
    In order to perform OCR on a PDF file, I first need to convert it to a file.
    To do that I'm using pdf2image function convert_from_bytes, which returns a list
    of images corresponding to each page in the file.
    """
    images = pdf2image.convert_from_path(filepath, dpi=200)
    tasks = [
        read_image(
            image=image,
        ) for image in images
    ]
    result = await asyncio.gather(*tasks) # [4]
    return result


async def read_dirs(dirpath: str) -> list:
    to_do = [process_file(f"{dirpath}/{file}") for file in os.listdir(dirpath)]
    to_do_iter = asyncio.as_completed(to_do) # [5]
    final_result = []
    for future in to_do_iter:
        final_result.append(await future)
    return final_result


if __name__ == '__main__':
    start = time.perf_counter()
    result = asyncio.run(read_dirs(DIR_PATH))
    elapsed = time.perf_counter() - start
    print(f'Took us [{elapsed:.2f}s] to run [{read_dirs.__name__}]')