Cada grupo define sus heuristicas tras el análisis del sector  
y las evalúan teniendo presente lo revisado en clase.  
1: Comparativa de rendimiento  
  
Definir un grafo sectorial (nodos = entidades de su sector, aristas = costos).  
Implementar los tres algoritmos: Greedy, A* y Weighted A* (con   
𝑤=1.5  
w=1.5   
𝑤=2  
estos W son opcionales, uds los ajustan a su sector en función de la realidad.  
  
Medir:  
Número de nodos expandidos.  
Longitud del camino.  
  
Crear una tabla comparativa.  
  
**2: Ajuste del peso (Trade-off)**  
  
Tomar el grafo anterior y ejecutar Weighted A* con   
w=1,1.2,1.5,2,3.  
  
Graficar:  
Costo del camino vs. w.  
Nodos expandidos vs. w.  
  
Responder:  
¿Qué peso logra el mejor balance entre rapidez y calidad?  
  
**3: Escenario dinámico**  
  
Simular un cambio en el grafo (p.ej., bloqueo de un nodo o aumento de costo en una arista).  
  
Recalcular el camino con cada algoritmo.  
Analizar:  
¿Cuál algoritmo se adapta mejor?  
¿Qué pasa con los costos?  
  
Tabla + reflexión del impacto de la heurística en la adaptabilidad.  
  
**4: Aplicación práctica en su sector**  
  
Ejemplo por sector:  
  
Salud: Ruta óptima para asignar ambulancias a hospitales con tiempos y tráfico como costos.  
Logística: Ruta de entrega más rápida considerando restricciones de combustible.  
Educación: Plan de asignación de tutores minimizando tiempo de desplazamiento.  
Tarea: Implementar Weighted A* en su contexto y justificar el peso elegido.