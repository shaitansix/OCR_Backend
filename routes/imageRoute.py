from fastapi import APIRouter
import base64
import numpy as np
import cv2
import easyocr
from models.imageModel import ImageBase64
from schemas.responseSchema import responseEntity

router = APIRouter(prefix = '/image', tags = ['image'])

@router.post('/extract_text')
async def get_image(data: ImageBase64):
    try:
        encoded = data.image.split(',')[-1]
        img_bytes = base64.b64decode(encoded)
        img_array = np.frombuffer(img_bytes, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        reader = easyocr.Reader(['es'], gpu = False)
        results = reader.readtext(image, paragraph = False)
        text = ' '.join([word[1] for word in results])

        return responseEntity(
            state = 'Success', 
            data = { 'output': text }, 
            message = 'Texto extraído correctamente'
        )
    except Exception as ex:
        return responseEntity(
            state = 'Failed', 
            message = f'Error del server: {ex}'
        )