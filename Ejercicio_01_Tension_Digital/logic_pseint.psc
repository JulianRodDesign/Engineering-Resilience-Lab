Algoritmo Tension_Red_Basica
    // Definición de variables con enfoque estructural
    Definir limite_falla, tension_actual, impacto_paquete Como Real
    Definir continuar Como Logico
    
    limite_falla <- 100
    tension_actual <- 0
    continuar <- Verdadero
    
    Escribir "--- Simulador de Tensión Estructural de Datos ---"
    
    Mientras continuar Y tension_actual < limite_falla Hacer
        Escribir "Ingrese magnitud del impacto (Carga transaccional 1-50):"
        Leer impacto_paquete
        
        // Analogía de endurecimiento: la tensión se acumula
        tension_actual <- tension_actual + impacto_paquete
        
        Escribir "Nivel de Tensión en el Nodo: ", tension_actual
        
        Si tension_actual >= limite_falla Entonces
            Escribir "FALLA CRÍTICA: Límite elástico superado. Bloqueando acceso."
            continuar <- False
        Sino
            Escribir "Estructura estable. Disipando energía..."
            // Resiliencia: el sistema recupera su forma base poco a poco
            tension_actual <- tension_actual * 0.9
        FinSi
    FinMientras
FinAlgoritmo
