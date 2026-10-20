# JobMarket AI

Plataforma de análisis inteligente del mercado laboral tecnológico utilizando Python, análisis de datos, Machine Learning y NLP.

## Objetivo

El objetivo de este proyecto es analizar ofertas de empleo del sector tecnológico para identificar:

- Tecnologías más demandadas
- Perfiles profesionales con mayor número de ofertas
- Skills con mayor impacto en empleabilidad
- Compatibilidad entre una oferta y un perfil profesional
- Tendencias del mercado laboral
- Rangos salariales
- Habilidades que merece la pena aprender

El proyecto está pensado para evolucionar progresivamente desde Python básico hasta técnicas de Inteligencia Artificial y Big Data.

---

## Problema que resuelve

Cuando una persona busca empleo tecnológico puede encontrar cientos de ofertas, pero resulta difícil saber:

- Qué tecnologías aparecen más
- Qué perfiles tienen mayor demanda
- Qué conocimientos faltan para optar a determinados puestos
- Qué habilidades merece la pena aprender primero
- Qué ofertas encajan mejor con su perfil

JobMarket AI transforma ofertas de empleo en datos analizables y permite extraer información útil para tomar mejores decisiones profesionales.

---

# Roadmap del proyecto

## Fase 1 — Python

Objetivo: practicar fundamentos de Python.

El sistema trabajará inicialmente con un archivo CSV que contenga ofertas de empleo.

Ejemplo:

```csv
puesto,empresa,ubicacion,tecnologias,salario
Data Analyst,Empresa A,Málaga,"Python,SQL,Power BI",28000
Frontend Developer,Empresa B,Remoto,"JavaScript,React,Git",30000
AI Developer,Empresa C,Madrid,"Python,TensorFlow,Docker",35000
```

Funcionalidades:

- Leer archivos CSV
- Recorrer ofertas
- Buscar tecnologías
- Contar frecuencia de aparición
- Filtrar ofertas
- Trabajar con listas
- Trabajar con diccionarios
- Crear funciones
- Ordenar resultados

Ejemplo de salida:

```text
Tecnologías más demandadas

Python: 32 ofertas
SQL: 27 ofertas
JavaScript: 24 ofertas
Docker: 18 ofertas
Power BI: 15 ofertas
```

---

## Fase 2 — Análisis de datos

Tecnologías:

- Python
- Pandas
- NumPy

Objetivos:

- Convertir las ofertas en DataFrames
- Limpiar datos
- Eliminar duplicados
- Gestionar valores nulos
- Analizar salarios
- Analizar tecnologías
- Analizar ubicaciones
- Analizar tipos de puesto

Posibles análisis:

```text
Tecnología más demandada
Salario medio por perfil
Skills más comunes
Ciudades con más ofertas
Porcentaje de ofertas remotas
```

---

## Fase 3 — Visualización de datos

Tecnologías:

- Matplotlib
- Seaborn
- Power BI

Visualizaciones previstas:

- Top tecnologías demandadas
- Salario medio por perfil
- Número de ofertas por ciudad
- Distribución de puestos
- Comparativa entre perfiles
- Evolución de tecnologías

---

## Fase 4 — Sistema de compatibilidad

El usuario podrá definir su perfil profesional.

Ejemplo:

```python
perfil = [
    "JavaScript",
    "React",
    "PHP",
    "MySQL",
    "Git",
    "Python"
]
```

El sistema comparará esas skills con cada oferta.

Ejemplo:

```text
Oferta:
Junior Data Analyst

Compatibilidad:
72%

Skills coincidentes:
Python
SQL
Git

Skills faltantes:
Power BI
Pandas
Excel
```

Las ofertas podrán ordenarse según el nivel de compatibilidad.

---

## Fase 5 — Machine Learning

Objetivo: utilizar modelos de aprendizaje supervisado.

El sistema aprenderá a clasificar ofertas automáticamente.

Posibles categorías:

```text
Frontend Developer
Backend Developer
Full Stack Developer
Data Analyst
Data Scientist
AI Engineer
Machine Learning Engineer
DevOps
Business Intelligence
```

Modelos a probar:

- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Naive Bayes

Ejemplo:

Entrada:

```text
Buscamos desarrollador con conocimientos en Python,
Pandas, SQL, Power BI y análisis de datos.
```

Salida:

```text
Perfil detectado:
Data Analyst

Probabilidad:
91%
```

---

## Fase 6 — Evaluación de modelos

Se compararán diferentes modelos utilizando:

- Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusión

Ejemplo:

```text
Logistic Regression: 84%
Decision Tree: 79%
Random Forest: 89%
Naive Bayes: 86%
```

El objetivo será seleccionar el modelo que mejor clasifique las ofertas.

---

## Fase 7 — Procesamiento de lenguaje natural

Se utilizarán técnicas de NLP para analizar automáticamente las descripciones.

Objetivos:

- Detectar tecnologías
- Extraer skills
- Detectar experiencia requerida
- Detectar modalidad
- Detectar ubicación
- Detectar requisitos
- Clasificar ofertas

Ejemplo:

Entrada:

```text
We are looking for a developer with experience in
Python, AWS, Docker and TensorFlow.
```

Salida:

```json
{
  "skills": [
    "Python",
    "AWS",
    "Docker",
    "TensorFlow"
  ]
}
```

---

## Fase 8 — Recomendador de skills

El sistema analizará qué conocimientos faltan al usuario en las ofertas que le interesan.

Ejemplo:

```text
Skills recomendadas para mejorar empleabilidad

1. Python
Presente en 62% de las ofertas objetivo

2. Docker
Presente en 47%

3. AWS
Presente en 39%

4. Power BI
Presente en 31%
```

Esto permitirá decidir qué tecnología aprender primero.

---

## Fase 9 — Dashboard

Se desarrollará una interfaz utilizando:

- Streamlit

Posibles secciones:

### Mercado laboral

- Número de ofertas
- Tecnologías más demandadas
- Salarios
- Ubicaciones

### Mi perfil

- Skills actuales
- Skills faltantes
- Compatibilidad media

### Ofertas recomendadas

Ranking de ofertas según compatibilidad.

---

## Fase 10 — API

Se creará una API utilizando:

- FastAPI

Ejemplo:

```http
POST /predict-job
```

Entrada:

```json
{
  "description": "Python SQL Pandas Power BI"
}
```

Salida:

```json
{
  "profile": "Data Analyst",
  "confidence": 0.91
}
```

---

# Evolución hacia Big Data

En fases futuras el proyecto podrá trabajar con grandes cantidades de ofertas.

Tecnologías potenciales:

- Hadoop
- Spark
- Hive
- MapReduce
- sistemas distribuidos
- herramientas de Business Intelligence

Arquitectura futura:

```text
Fuentes de empleo
      ↓
Recolección de datos
      ↓
Python
      ↓
Procesamiento
      ↓
Base de datos
      ↓
Machine Learning / NLP
      ↓
API
      ↓
Dashboard / Power BI
```

---

# Tecnologías

## Inicio

- Python
- CSV
- JSON
- Git
- GitHub

## Data

- Pandas
- NumPy
- Matplotlib

## Machine Learning

- Scikit-learn

## NLP

- Scikit-learn
- spaCy
- modelos de lenguaje

## Backend

- FastAPI

## Dashboard

- Streamlit
- Power BI

## Big Data

- Hadoop
- Spark
- Hive

---

# Estructura prevista

```text
jobmarket-ai/

data/
    ofertas.csv

src/
    main.py
    analysis.py
    skills.py
    matching.py

models/
    job_classifier.pkl

notebooks/
    exploration.ipynb
    machine_learning.ipynb

dashboard/
    app.py

api/
    main.py

README.md

requirements.txt
```

---

# Primera versión

La primera versión del proyecto será sencilla.

Objetivo:

Analizar un archivo CSV con ofertas y mostrar las tecnologías más demandadas.

Pasos:

1. Crear dataset de ofertas
2. Leer el CSV con Python
3. Extraer tecnologías
4. Contar apariciones
5. Ordenarlas
6. Mostrar ranking

Ejemplo esperado:

```text
TOP SKILLS

1. Python — 38 ofertas
2. SQL — 31 ofertas
3. JavaScript — 27 ofertas
4. Docker — 22 ofertas
5. AWS — 19 ofertas
```

---

# Objetivo de aprendizaje

Este proyecto está diseñado para aprender progresivamente:

```text
Python
↓
Pandas
↓
Análisis de datos
↓
Visualización
↓
Machine Learning
↓
NLP
↓
APIs
↓
Business Intelligence
↓
Big Data
```

---

# Objetivo profesional

JobMarket AI pretende convertirse en un proyecto de portfolio capaz de demostrar conocimientos en:

- Desarrollo de software
- Python
- Data Analytics
- Machine Learning
- NLP
- Inteligencia Artificial
- APIs
- Business Intelligence
- Big Data

El objetivo final es construir una herramienta real que permita entender mejor el mercado laboral tecnológico y utilizar datos para mejorar la búsqueda de empleo.

---

# Normas de Interacción con IA

1. **PROHIBIDO ESCRIBIR CÓDIGO POR EL USUARIO:** La Inteligencia Artificial actuará exclusivamente como mentor/tutor. Bajo ningún concepto escribirá, creará o modificará archivos de código (.py, .csv, etc.) del proyecto de forma autónoma.
2. Todo el código debe ser escrito manualmente por el desarrollador (el usuario) para garantizar el aprendizaje y asimilación de los conceptos expuestos en este documento.