from fastapi import APIRouter
from schemas.responseSchema import responseEntity

router = APIRouter()

@router.get('/{full_path:path}')
async def not_found(full_path: str):
    try: 
        return responseEntity(
            state = 'Success', 
            message = f'La ruta {full_path} no existe'
        )
    except Exception as ex:
        return responseEntity(
            state = 'Failed', 
            message = f'Error del server: {ex}'
        )