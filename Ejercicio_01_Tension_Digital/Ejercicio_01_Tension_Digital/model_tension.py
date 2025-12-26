# Ejercicio 1: Simulación de Resiliencia Estructural
# Inspirado en el comportamiento de materiales bajo carga cíclica.

class NodoResiliente:
    def __init__(self, ip):
        self.ip = ip
        self.tension = 0.0
        self.coeficiente_seguridad = 1.2 

    def analizar_impacto(self, magnitud):
        # El sistema se endurece según el impacto recibido
        esfuerzo_detectado = magnitud * self.coeficiente_seguridad
        self.tension += esfuerzo_detectado
        
        if self.tension > 100:
            return f"ALERTA: Falla en {self.ip}. Estructura saturada."
        
        # Factor de Resiliencia: Capacidad de retorno al estado base
        self.tension *= 0.8 
        return f"OK: {self.ip} estable. Tensión residual: {self.tension:.2f}"

# Simulación de ráfaga de datos
servidor = NodoResiliente("192.168.1.100")
for i in range(5):
    print(servidor.analizar_impacto(30))
