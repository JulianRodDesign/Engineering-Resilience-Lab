Algoritmo Muro_Circular_Distribuido
	Definir tension_central, tension_vecinos, impacto, carga_compartida Como Real
    tension_central <- 0
    tension_vecinos <- 0
    limite_seguridad <- 100
    
    Escribir "--- Simulador de Distribución de Carga Estructural ---"
    Escribir "Ingrese la magnitud del ataque al Nodo Central:"
    Leer impacto
    
    // Si el impacto es fuerte, el nodo central reparte el 30% a los vecinos
    Si impacto > 40 Entonces
        carga_compartida <- impacto * 0.3
        tension_central <- tension_central + (impacto - carga_compartida)
        tension_vecinos <- tension_vecinos + carga_compartida
        Escribir "Carga excesiva detectada. Distribuyendo energía a nodos vecinos..."
    Sino
        tension_central <- tension_central + impacto
    FinSi
    
    Escribir "Tensión Nodo Central: ", tension_central
    Escribir "Tensión Nodos de Apoyo (Vecinos): ", tension_vecinos
    
    Si tension_central > limite_seguridad Entonces
        Escribir "FALLA: El arco se ha colapsado."
    Sino
        Escribir "SISTEMA ESTABLE: La geometría circular absorbió el impacto."
    FinSi
FinAlgoritmo
