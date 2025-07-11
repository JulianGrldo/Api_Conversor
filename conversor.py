# conversor.py

# Factores de conversión a la unidad base (metro y gramo)
FACTORES_LONGITUD = {
    'metro': 1.0,
    'kilometro': 1000.0,
    'centimetro': 0.01,
    'milla': 1609.34
}

FACTORES_PESO = {
    'gramo': 1.0,
    'kilogramo': 1000.0,
    'libra': 453.592,
    'onza': 28.3495
}

def convertir_longitud(valor: float, de: str, a: str) -> float:
    """Convierte un valor de una unidad de longitud a otra."""
    if de not in FACTORES_LONGITUD or a not in FACTORES_LONGITUD:
        raise ValueError("Unidades de longitud no válidas.")
    
    # Convertir el valor de origen a la unidad base (metros)
    valor_en_metros = valor * FACTORES_LONGITUD[de]
    
    # Convertir de metros a la unidad de destino
    resultado = valor_en_metros / FACTORES_LONGITUD[a]
    return resultado

def convertir_peso(valor: float, de: str, a: str) -> float:
    """Convierte un valor de una unidad de peso a otra."""
    if de not in FACTORES_PESO or a not in FACTORES_PESO:
        raise ValueError("Unidades de peso no válidas.")
        
    # Convertir el valor de origen a la unidad base (gramos)
    valor_en_gramos = valor * FACTORES_PESO[de]
    
    # Convertir de gramos a la unidad de destino
    resultado = valor_en_gramos / FACTORES_PESO[a]
    return resultado

def convertir_temperatura(valor: float, de: str, a: str) -> float:
    """Convierte un valor de una unidad de temperatura a otra."""
    if de == a:
        return valor

    # De Celsius a...
    if de == 'celsius':
        if a == 'fahrenheit':
            return (valor * 9/5) + 32
        elif a == 'kelvin':
            return valor + 273.15
    
    # De Fahrenheit a...
    elif de == 'fahrenheit':
        if a == 'celsius':
            return (valor - 32) * 5/9
        elif a == 'kelvin':
            return (valor - 32) * 5/9 + 273.15
            
    # De Kelvin a...
    elif de == 'kelvin':
        if a == 'celsius':
            return valor - 273.15
        elif a == 'fahrenheit':
            return (valor - 273.15) * 9/5 + 32
            
    raise ValueError("Unidades de temperatura no válidas.")

def convertir_unidades(tipo: str, valor: float, de: str, a: str) -> float:
    """Función principal que delega la conversión al tipo correspondiente."""
    if tipo == 'longitud':
        return convertir_longitud(valor, de, a)
    elif tipo == 'peso':
        return convertir_peso(valor, de, a)
    elif tipo == 'temperatura':
        return convertir_temperatura(valor, de, a)
    else:
        raise ValueError(f"Tipo de conversión '{tipo}' no soportado.")

