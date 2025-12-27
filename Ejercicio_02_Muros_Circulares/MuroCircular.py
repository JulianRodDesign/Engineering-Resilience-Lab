class MuroCircular:
    def __init__(self):
        self.nodos = {"Central": 0.0, "Apoyo_A": 0.0, "Apoyo_B": 0.0}
        self.limite = 100.0

    def recibir_ataque(self, magnitud):
        print(f"\n>>> Impacto detectado: {magnitu4d}")
        
        # Lógica de ingeniería: Distribución de esfuerzo
        if magnitud > 50:
            # El 40% se disipa hacia los apoyos laterales
            distribucion = magnitud * 0.4
            self.nodos["Central"] += (magnitud - distribucion)
            self.nodos["Apoyo_A"] += distribucion / 2
            self.nodos["Apoyo_B"] += distribucion / 2
            print("INFO: Carga compartida entre los apoyos del arco.")
        else:
            self.nodos["Central"] += magnitud
            
        return self.verificar_integridad()

    def verificar_integridad(self):
        for nodo, tension in self.nodos.items():
            if tension >= self.limite:
                return f"CRÍTICO: Nodo {nodo} colapsado. Estructura comprometida."
            # Resiliencia natural (enfriamiento)
            self.nodos[nodo] *= 0.85
        return f"ESTADO: Estructura estable. Nodos: {self.nodos}"

# --- PRUEBA EN VS CODE ---
mi_red = MuroCircular()
test_ataques = [40, 70, 80] # Ataques progresivos

for a in test_ataques:
    print(mi_red.recibir_ataque(a))