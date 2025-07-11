# main.py

from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

# Importamos la lógica de conversión desde nuestro módulo conversor
import conversor

# Creamos una instancia de la aplicación FastAPI
app = FastAPI(
    title="API de Conversión de Unidades",
    description="Una API simple para convertir unidades de longitud, peso y temperatura.",
    version="1.0.0"
)

# Montamos un directorio estático para servir el frontend (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
async def root():
    """Redirige a la página principal del frontend."""
    return RedirectResponse(url="/static/index.html")

@app.get("/convertir")
async def api_convertir(
    tipo: str = Query(..., description="Tipo de conversión: 'longitud', 'peso' o 'temperatura'"),
    valor: float = Query(..., description="El valor numérico a convertir"),
    de: str = Query(..., description="Unidad de origen"),
    a: str = Query(..., description="Unidad de destino")
):
    """
    Endpoint principal para realizar la conversión de unidades.
    """
    try:
        # Normalizamos las unidades a minúsculas para evitar errores
        de_lower = de.lower()
        a_lower = a.lower()
        tipo_lower = tipo.lower()

        # Llamamos a la función de conversión principal
        resultado = conversor.convertir_unidades(tipo_lower, valor, de_lower, a_lower)
        
        # Devolvemos el resultado en un formato JSON claro
        return {
            "valor_original": valor,
            "unidad_origen": de,
            "valor_convertido": round(resultado, 4), # Redondeamos para una mejor presentación
            "unidad_destino": a
        }
    except ValueError as e:
        # Si ocurre un error (ej. unidad no válida), devolvemos un error HTTP 400
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Capturamos cualquier otro error inesperado
        raise HTTPException(status_code=500, detail="Ocurrió un error interno en el servidor.")
