class RedCelosia:
    def __init__(self, num_nodos=5):
        self.nodos = [0.0] * num_nodos
        self.limite_nodo = 60.0 # Cada nodo es más pequeño, pero trabajan juntos

    def distribuir_carga(self, impacto_total):
        print(f"\n[EVENTO] Impacto masivo de: {impacto_total} unidades")
        
        # Lógica de Celosía: Reparto proporcional en la malla
        carga_por_nodo = impacto_total / len(self.nodos)
        
        for i in range(len(self.nodos)):
            self.nodos[i] += carga_por_nodo
            # Aplicamos una disipación rápida por la eficiencia de la malla (20%)
            self.nodos[i] *= 0.80
            
        return self.monitorear_red()

    def monitorear_red(self):
        promedio = sum(self.nodos) / len(self.nodos)
        print(f"Tensión promedio en la malla: {promedio:.2f}")
        
        if any(n >= self.limite_nodo for n in self.nodos):
            return "ALERTA: Punto de ruptura en celosía detectado. Redirigiendo tráfico..."
        return "SISTEMA: Carga absorbida por la red de celosía con éxito."

# --- PRUEBA DE CAMPO ---
malla_seguridad = RedCelosia()
impactos = [100, 250] # Un impacto normal y uno masivo

for imp in impactos:
    print(malla_seguridad.distribuir_carga(imp))