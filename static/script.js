
document.addEventListener('DOMContentLoaded', () => {
    const tipoSelect = document.getElementById('tipo');
    const unidadDeSelect = document.getElementById('unidadDe');
    const unidadASelect = document.getElementById('unidadA');
    const form = document.getElementById('conversor-form');
    const resultadoP = document.getElementById('resultado');

    // Mapeo de unidades por tipo de conversión
    const unidades = {
        longitud: ['Metro', 'Kilómetro', 'Centímetro', 'Milla'],
        peso: ['Gramo', 'Kilogramo', 'Libra', 'Onza'],
        temperatura: ['Celsius', 'Fahrenheit', 'Kelvin']
    };

    // Función para actualizar las opciones de los selects de unidades
    function actualizarUnidades() {
        const tipoSeleccionado = tipoSelect.value;
        const opciones = unidades[tipoSeleccionado];

        // Limpiar selects anteriores
        unidadDeSelect.innerHTML = '';
        unidadASelect.innerHTML = '';

        // Poblar los selects con las nuevas opciones
        opciones.forEach(unidad => {
            const optionDe = document.createElement('option');
            optionDe.value = unidad.toLowerCase();
            optionDe.textContent = unidad;
            unidadDeSelect.appendChild(optionDe);

            const optionA = document.createElement('option');
            optionA.value = unidad.toLowerCase();
            optionA.textContent = unidad;
            unidadASelect.appendChild(optionA);
        });
        
        // Asegurarse de que las unidades por defecto no sean las mismas
        if (opciones.length > 1) {
            unidadASelect.selectedIndex = 1;
        }
    }

    // Evento para cambiar las unidades cuando se cambia el tipo de conversión
    tipoSelect.addEventListener('change', actualizarUnidades);

    // Evento para manejar el envío del formulario
    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Evitar que la página se recargue

        const formData = new FormData(form);
        const tipo = formData.get('tipo');
        const valor = formData.get('valor');
        const de = formData.get('de');
        const a = formData.get('a');

        if (!valor) {
            resultadoP.textContent = 'Por favor, introduce un valor numérico.';
            resultadoP.className = 'error';
            return;
        }

        // Construir la URL para la petición a la API
        const apiUrl = `/convertir?tipo=${tipo}&valor=${valor}&de=${de}&a=${a}`;

        resultadoP.textContent = 'Convirtiendo...';
        resultadoP.className = '';

        try {
            const response = await fetch(apiUrl);

            // Si la respuesta no es OK (ej. error 400), lanzamos un error
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Ocurrió un error en la petición.');
            }

            const data = await response.json();
            
            // Formatear y mostrar el resultado
            resultadoP.textContent = `${data.valor_original} ${data.unidad_origen} son ${data.valor_convertido} ${data.unidad_destino}.`;
            resultadoP.className = '';

        } catch (error) {
            resultadoP.textContent = `Error: ${error.message}`;
            resultadoP.className = 'error';
        }
    });

    // Inicializar las unidades al cargar la página
    actualizarUnidades();
});