# Dashboards y procesos ETL
Juan Francisco Mier Montoto
*Inteligencia de Negocio, EPI Gijón 23-24*

---

# Índice
1. Introducción
2. Conceptos clave
   1. Definición de dashboard
   2. Definición de ETL
3. Procesos ETL
   1. Extracción
   2. Transformación
   3. Carga
4. Creación y diseño de Dashboards
5. Integración
6. Demostración práctica
7. Conclusiones

## Tabla de figuras
TBW

## Bibliografía
-

---

# 1. Introducción
En la actualidad, las empresas se enfrentan a un gran volumen de datos gracias a los avances en las técnicas de recolección e interés generalizado en la recopilación de datos. Estos datos pueden ser de gran utilidad para la toma de cualquier decisión, tanto financiera como estratégica, pero para se necesita un buen proceso de análisis, visualización y valoración de los mismos.

En este documento se pretende explicar y expandir los conceptos "cuadro de mando" (dahsboard) y "procesos de extracción, transformación y carga" (ETL), así como su importancia en el sector tecnológico. Además de dar ejemplos de herramientas y procesos que se utilicen hoy en día, se realizará una breve demostración práctica de cómo una empresa utiliza estos procesos, sacados de mi experiencia laboral personal.

Como comentario, este trabajo sirve como prueba de GPT4 y todas las características que ofrece OpenAI en su modelo de pago.

---

# 2. Conceptos clave
## 2.1. ¿Qué es un dashboard?
La palabra "dashboard", que traducido de manera literal es "cuadro de mandos", es un término que se utiliza para referirse a cualquier interfaz gráfica que muestre información relevante de manera visual sobre un proceso o negocio. Aunque el término se utiliza en muchos ámbitos (puede incluir indicadores comerciales, de producción, de marketing, de calidad, de recursos humanos...), por lo general van siempre unidos a otros conceptos representados por sus siglas en inglés:
- KPI (*Key Performance Indicator*): valor cuantificable que permite medir el rendimiento de un proceso o actividad. Por ejemplo, en el caso de una empresa, un KPI puede ser el número de ventas, el número de clientes, el número de productos defectuosos, etc.
- BI (*Business Inteligence*): conjunto de estrategias y herramientas que permiten transformar los datos en información útil para la toma de decisiones. El BI se puede aplicar a cualquier ámbito, pero en este caso se aplica a los negocios.
- ETL (*Extract, Transform, Load*): esta definición se expandirá en el siguiente apartado, pero básicamente se trata de un proceso que permite extraer datos de una fuente, transformarlos y cargarlos en otra fuente.
