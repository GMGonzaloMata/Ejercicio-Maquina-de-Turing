# Simulaciones de Máquinas de Turing en Python

## Este repositorio contiene implementaciones en Python que simulan el comportamiento de distintas Máquinas de Turing (MT) para la materia **Teoría de la Computación**.

## 📘 Ejercicios

### 🧩 Ejercicio 1: Desplazamiento a la derecha

- **Descripción:** Mueve una cadena binaria `{a, b}` una posición a la derecha, dejando el primer lugar en blanco.
- **Ejemplo entrada:** `abba`
- **Resultado esperado:** `␣abba`

---

### 🧩 Ejercicio 2: Duplicación de ceros

- **Descripción:** Duplicar una cadena compuesta por símbolos `0`. Por ejemplo, `000` se transforma en `000000`.
- **Ejemplo entrada:** `000`
- **Resultado esperado:** `000000`

---

### 🧩 Ejercicio 3: Reconocimiento del lenguaje 01ⁿ0

- **Descripción:** Acepta las cadenas que empiezan con `0`, luego cualquier cantidad de `1` (incluyendo 0), y terminan en `0`.
- **Lenguaje aceptado:** L(M) = { W ∈ {0,1}\* | W = 01ⁿ0 }
- **Ejemplos válidos:** `00`, `010`, `01110`
- **Ejemplos inválidos:** `1`, `001`, `01`

---

### 🧩 Ejercicio 4: Paridad de unos

- **Descripción:** Calcula la paridad de la cantidad de `1`s en una cadena binaria. Agrega `0` si la cantidad es par, `1` si es impar.
- **Ejemplo entrada:** `1011`
- **Resultado esperado:** `10111` (tres unos = impar)

---

### 🧩 Ejercicio 5: Copiar cadenas del alfabeto `{a, b, c}`

- **Descripción:** Duplicar una palabra formada por los símbolos `{a, b, c}`.
- **Ejemplo entrada:** `bb`
- **Resultado esperado:** `bbbb`

---

## 🚀 Cómo ejecutar

1. Cloná este repositorio o descargá los archivos `.py`.
2. Ejecutá un ejercicio con:

```bash
python Ejercicio1.py
```
