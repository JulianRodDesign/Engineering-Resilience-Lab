Algoritmo Red_Celosia_Financiera
	Definir tension_total, impacto, disipacion_malla Como Real
    Definir nodos_activos Como Entero
    
    tension_total <- 0
    nodos_activos <- 5  // Representa una malla de 5 puntos interconectados
    limite_ruptura_red <- 250 // Una red aguanta más que un solo arco
    
    Escribir "--- Simulador de Red de Celosía (Truss Network) ---"
    Escribir "Ingrese magnitud del impacto masivo:"
    Leer impacto
    
    // En una malla, el impacto se divide equitativamente entre los nodos
    disipacion_malla <- impacto / nodos_activos
    tension_total <- tension_total + disipacion_malla
    
    Escribir "Carga disipada por nodo en la malla: ", disipacion_malla
    
    Si tension_total > (limite_ruptura_red / nodos_activos) Entonces
        Escribir "ALERTA: Fatiga global detectada. Activando nodos de respaldo."
    Sino
        Escribir "ESTADO: Estructura en equilibrio. Resiliencia de malla activa."
    FinSi
FinAlgoritmo
