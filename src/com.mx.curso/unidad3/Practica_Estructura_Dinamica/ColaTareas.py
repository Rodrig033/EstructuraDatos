from queue import Queue

cola_solicitudes = Queue()


# put equivale a offer en Java
cola_solicitudes.put("Analizar los sentimientos en el Tweet de Donald Trump")
cola_solicitudes.put("¿Qué es la vida?")
cola_solicitudes.put("Realizar un resumen de un artículo científico")
cola_solicitudes.put("Recrea la noche estrellada de Vangogh")
cola_solicitudes.put("Corregir grámatica en el documento")
cola_solicitudes.put("Generar un plan de estudios para aprender inglés")

total = cola_solicitudes.qsize()
restante = total
temporal = list(cola_solicitudes.queue)

print("\nSolicitudes = ",temporal)

print("\n---- Procesando solicitudes en orden FIFO ----")
print("Total de solicitudes: ", total)
while not cola_solicitudes.empty():
    solicitud = cola_solicitudes.get()
    restante -= 1
    print(f"Procesando solicitud: {solicitud}")
    print("Restantes ", restante)

print("Cola después de atender las solicitudes ", cola_solicitudes.get())