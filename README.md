# Evaluación Final POA — Fase 5

**Curso:** Fundamentos de Programación (213022)  
**Estudiante:** Jehison Steven Naranjo Peña  
**Identificación:** 1.029.663.024  
**Grupo:** 213022_1173  
**Tutor:** Diomar Antonio Pineda Cervantes  
**Programa:** Ingeniería en Inteligencia Artificial y Ciencia de Datos  
**Problema:** 1 — Clasificación del compromiso de sesiones

## Descripción

Programa en Python que recorre una matriz de sesiones  
`[ID del cliente, duración en segundos, número de clics]` y clasifica el compromiso:

| Nivel | Condición |
|-------|-----------|
| **Alto** | duración > 180 **y** clics > 8 |
| **Bajo** | duración < 60 **o** clics < 3 |
| **Medio** | cualquier otro caso |

## Cómo ejecutar

```bash
python3 problema1_compromiso_sesiones.py
```

No pide datos por teclado: usa las 6 sesiones de ejemplo definidas en el código.

## Resultado esperado

```
C001  → Alto
C002  → Bajo
C003  → Bajo
C004  → Medio
C005  → Alto
C006  → Medio
```

## Estructura del repositorio

| Archivo | Contenido |
|---------|-----------|
| `problema1_compromiso_sesiones.py` | Solución completa |
| `README.md` | Este archivo |

## Funciones

| Función | Rol |
|---------|-----|
| `clasificar_compromiso(duracion, clics)` | Aplica la lógica de negocio y retorna Alto / Medio / Bajo |
| `generar_informe(matriz_sesiones)` | Recorre la matriz e imprime ID + clasificación |
| `prueba_escritorio()` | Explica dos casos borde (C003 y C006) |
| `main()` | Punto de entrada |

## Conceptos aplicados

- Constantes y variables  
- Arreglo bidimensional (lista de listas)  
- Estructuras de selección (`if`) y de repetición (`for`)  
- Funciones con parámetros y valor de retorno  
- Operadores relacionales (`>`, `<`) y lógicos (`and`, `or`)

## Autor

Jehison Steven Naranjo Peña — Grupo 213022_1173 — UNAD 2026
