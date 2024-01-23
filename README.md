# Descripción del Proyecto Freelance: Recordatorio de Clientes Deudores

Este código representa mi primer proyecto freelance para una pequeña casa de electrodomésticos. Su propósito es enviar recordatorios diarios al dueño de la tienda sobre los clientes con cuotas impagas al final del día. A continuación, se describen las funciones principales del código:

## 1. Lectura del Archivo Excel:
   - Utiliza la biblioteca `pandas` para leer el archivo Excel 'clientes.xlsx', que contiene información sobre los clientes y sus cuotas.
   - En caso de errores durante la lectura, imprime un mensaje de error para facilitar la identificación y resolución.

## 2. Cálculo de Fechas de Vencimiento:
   - Recorre el DataFrame generado a partir del archivo Excel, determinando las fechas de vencimiento para cuotas impagas.
   - Las fechas se calculan sumando días específicos (30, 60, o 90) a la fecha de compra, dependiendo de la cuota impaga.

## 3. Creación de Listas de Vencimientos Próximos:
   - Construye listas que contienen el nombre del cliente y las fechas de vencimiento para cuotas impagas.
   - Almacena estas listas en `list_vencimiento_prox`.

## 4. Envío de Mensajes de WhatsApp:
   - Itera sobre las listas creadas y envía mensajes de WhatsApp si la fecha de vencimiento está próxima (dentro de los próximos 7 días).
   - Los mensajes incluyen el nombre del cliente y la fecha de vencimiento, utilizando la biblioteca `pywhatkit`.

## 5. Función Adicional para Enviar Mensajes:
   - Proporciona una función llamada `mandar_mensaje` para enviar mensajes de texto a través de WhatsApp.
   - Utiliza la aplicación de WhatsApp web y cierra la ventana automáticamente después de enviar el mensaje.

Este script combina el manejo de datos con la automatización de mensajes de WhatsApp para ofrecer al dueño de la tienda una herramienta eficaz de gestión de pagos pendientes de clientes.
