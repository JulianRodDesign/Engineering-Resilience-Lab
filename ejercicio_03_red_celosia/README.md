# Ejercicio 03: Red de Celosía (Truss Network) 🏗️

## Concepto de Ingeniería
En este ejercicio, evolucionamos de un arco simple a una **Red de Celosía**. En ingeniería civil y mecánica, las celosías son estructuras de barras interconectadas que ofrecen una alta redundancia. Si un elemento falla o se estresa, la carga se redistribuye a través de múltiples nodos.

## Lógica del Software
He implementado esta filosofía física en un algoritmo de seguridad:
* **Distribución Proporcional:** El impacto no golpea a un solo punto, sino que se reparte equitativamente en una malla de nodos.
* **Sensores de Fatiga:** Utilizo la lógica `any()` de Python para detectar si un solo nodo individual ha llegado a su límite crítico, permitiendo una alerta temprana.
* **Resiliencia de Malla:** El sistema demuestra que una estructura interconectada puede absorber impactos mucho mayores que los componentes aislados.

## Archivos
* `red_celosia.py`: Implementación en Python con clases y ciclos de distribución.
* `logic_pseint.psc`: Lógica inicial y prototipado del pensamiento estructural.
