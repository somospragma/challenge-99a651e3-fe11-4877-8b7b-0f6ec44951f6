# Implementación y Despliegue de una Función Serverless

Tu tarea es implementar y desplegar una función serverless que procese eventos. La función debe ser capaz de recibir un evento, realizar una operación simple (como transformar el contenido del evento) y devolver un resultado. Esta función será desplegada en un entorno serverless y debe ser capaz de manejar múltiples invocaciones concurrentes.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | AWS Lambda |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 3-4 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del Problema y Planificación

**Objetivo:** Entender los requisitos del problema y planificar la implementación de la función serverless.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Identifica los eventos que la función debe manejar.
- Define la operación que la función realizará sobre los eventos.
- Planifica cómo la función será desplegada y gestionada en un entorno serverless.

**Entregable:** Un plan de implementación detallado.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los tipos de eventos que tu función podría recibir.
- Piensa en cómo tu función podría ser escalada para manejar múltiples invocaciones.

</details>

### Fase 2: Implementación de la Función

**Objetivo:** Implementar la función serverless según el plan definido.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Crea la función serverless.
- Implementa la lógica para manejar los eventos y realizar la operación definida.
- Asegura que la función pueda manejar múltiples invocaciones concurrentes.

**Entregable:** Código fuente de la función serverless.

<details>
<summary>Pistas de conocimiento</summary>

- Recuerda que tu función debe ser idempotente.
- Considera cómo manejarás errores y excepciones.

</details>

### Fase 3: Despliegue y Pruebas

**Objetivo:** Desplegar la función serverless y realizar pruebas para asegurar su correcto funcionamiento.

**Tiempo estimado:** 1 hora 30 minutos

**Instrucciones:**

- Despliega la función serverless en un entorno de pruebas.
- Realiza pruebas para asegurar que la función maneje correctamente los eventos y realice la operación definida.
- Verifica que la función pueda manejar múltiples invocaciones concurrentes sin problemas.

**Entregable:** Informe de pruebas con resultados.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza casos de prueba que cubran diferentes escenarios de eventos.
- Verifica el comportamiento de la función bajo carga.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una función serverless y cómo se diferencia de una función tradicional?
- **paraQueSirve**: ¿Para qué sirve desplegar una función en un entorno serverless?
- **comoSeUsa**: ¿Cómo se implementa y despliega una función serverless?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar y desplegar funciones serverless y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica el despliegue de una función serverless en términos de escalabilidad y gestión de errores?

## Criterios de Evaluacion

- Definición clara del problema y planificación de la implementación.
- Implementación correcta de la función serverless.
- Despliegue exitoso de la función y realización de pruebas exhaustivas.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
