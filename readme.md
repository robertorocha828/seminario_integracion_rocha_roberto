# 🎓 Seminario de Integración Curricular
# 🎓 Autor: Roberto Rocha

Bienvenido al repositorio oficial del proyecto desarrollado para la materia **Seminario de Integración Curricular**. Este proyecto consiste en el desarrollo de una aplicación web moderna, separando la lógica del servidor (Backend) y la interfaz de usuario (Frontend) utilizando tecnologías de vanguardia.

---

## 🚀 Tecnologías Principales

Este proyecto está construido sobre una arquitectura cliente-servidor utilizando las siguientes herramientas:

### Backend: FastAPI ⚡
[FastAPI](https://fastapi.tiangolo.com/) es un framework web moderno y de alto rendimiento para construir APIs con **Python**. 
* **Concepto clave:** Se basa en las anotaciones de tipos estándar de Python, lo que permite que el código sea muy fácil de escribir, leer y depurar.
* **Ventajas:** Es increíblemente rápido (comparable con NodeJS o Go), soporta programación asíncrona de forma nativa (`async`/`await`) y genera documentación interactiva de la API (Swagger UI y ReDoc) de manera automática.

### Frontend: Angular 🅰️
[Angular](https://angular.io/) es una plataforma y framework de desarrollo creado por Google para construir aplicaciones web de una sola página (SPA - *Single Page Applications*).
* **Concepto clave:** Utiliza **TypeScript** y se basa en una arquitectura de componentes, donde la interfaz gráfica se divide en piezas reutilizables e independientes.
* **Ventajas:** Ofrece herramientas robustas para el manejo de rutas, inyección de dependencias, gestión de estado y comunicación con APIs externas mediante su módulo `HttpClient`.

---

## 📁 Estructura del Proyecto

El repositorio está dividido en dos directorios principales para mantener el código organizado:

```text
📦 raiz-del-proyecto
 ┣ 📂 backend/       # Código fuente de FastAPI (Python)
 ┣ 📂 frontend/      # Código fuente de Angular (TypeScript)
 ┣ 📜 .gitignore     # Reglas de exclusión de Git
 ┗ 📜 README.md      # Documentación del proyecto