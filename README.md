

                                                   # OrangeHRM API Test Automation

## 📌 Descripción del Proyecto
Este repositorio contiene el plan de pruebas y las pruebas automatizadas de la API REST del sistema **OrangeHRM**, enfocado en el módulo de **Administración** especificamente en los submodulos (Estado de Empleado,Categorías de Trabajo,Categorías de Trabajo).

OrangeHRM es un sistema de gestión de recursos humanos (HRM) que permite administrar empleados, asistencia, licencias, reclutamiento y desempeño desde una plataforma centralizada.

---

## 🎯 Objetivos
- Validar las funcionalidades del módulo Administración mediante pruebas automatizadas.
- Garantizar que los endpoints REST de la API cumplan con los requisitos funcionales.
- Documentar y automatizar casos de prueba positivos y negativos.
- Ejecutar pruebas exploratorias, funcionales, de humo (smoke), regresión ,valor limite y de seguridad.

---

## 🧩 Módulos Probados
El presente plan de pruebas se enfocará exclusivamente en las funcionalidades del módulo Administración, cubriendo 
los siguientes submódulos a nivel de API:
- Administración de usuarios
- Estado de empleado
- Categorías de trabajo

---

## 🚫 Limitaciones
Token de autenticación: No se prueba el flujo de login. Se utiliza token obtenido automáticamente vía web scraping desde la demo pública de OrangeHRM.

# byte-girls-api-testing
### Obtener/Actualizar el token
Ejecuta el siguiente comando para obtener el token desde la página web y actualizarlo en config.py:
```
python .\src\utils\update_token_config.py
```
Este comando extrae el token automáticamente y lo guarda en la variable TOKEN.

---
## Herramienetas 
- Postman  para la ejecución y documentación sobre  la API REST de OrangeHRM. Estas estarán organizadas por colecciones
- Python + Pytest, utilizados para la creación de pruebas automatizadas y la integración con librerías que permitan validaciones sobre la API.

---
## 📍 Funcionalidades y Endpoints

### 1. Admin>Estado de Empleado,Categorías de Trabajo,Categorías de Trabajo

| Jira Código | Funcionalidad                  | Verbo | Endpoint                           |
|-------------|--------------------------------|-------|------------------------------------|
| BYT-7       | Obtener usuario por ID         | GET   | `/admin/users/{id}`               |
| BYT-8       | Listar usuarios                | GET   | `/admin/users`                    |
| BYT-1       | Crear usuario                  | POST  | `/admin/users`                    |
| BYT-22      | Eliminar usuario               | DELETE| `/admin/users`                    |
| BYT-23      | Validar nombre de usuario único| GET   | `/admin/validation/user-name`    |

### 2. Estado de Empleado

| Jira Código | Funcionalidad                  | Verbo | Endpoint                             |
|-------------|--------------------------------|-------|--------------------------------------|
| BYT-11      | Obtener estado de empleado     | GET   | `/admin/employment-statuses/{id}`   |
| BYT-25      | Actualizar estado de empleado  | PUT   | `/admin/employment-statuses/{id}`   |
| BYT-12      | Listar estados de empleado     | GET   | `/admin/employment-statuses`        |
| BYT-10      | Crear estado de empleado       | POST  | `/admin/employment-statuses`        |
| BYT-26      | Eliminar estado de empleado    | DELETE| `/admin/employment-statuses`        |

### 3. Categorías de Trabajo

| Jira Código | Funcionalidad                  | Verbo | Endpoint                          |
|-------------|--------------------------------|-------|-----------------------------------|
| BYT-3       | Obtener categoría de trabajo  | GET   | `/admin/job-categories/{id}`     |
| BYT-27      | Actualizar categoría trabajo  | PUT   | `/admin/job-categories/{id}`     |
| BYT-4       | Listar categorías de trabajo  | GET   | `/admin/job-categories`          |
| BYT-2       | Crear categoría de trabajo    | POST  | `/admin/job-categories`          |
| BYT-24      | Eliminar categoría de trabajo | DELETE| `/admin/job-categories`          |

---

## 👤 Roles de Usuario
       Administrador: Puede acceder a todas las funcionalidades.

---

## 🔍 Tipos de Pruebas Realizadas

| Tipo de Prueba         | Descripción |
|------------------------|-------------|
| Exploratory Testing    | Pruebas manuales con Postman para inputs límite, errores inesperados, comparación con documentación. |
| Functional Testing     | Validación de casos positivos/negativos, estructura JSON, status codes. |
| Smoke Testing          | Validación rápida de endpoints críticos. |
| Regression Testing     | Verificación de funcionalidades existentes tras cambios. |
| Security Testing       | Validación de tokens, control de acceso y manejo de errores no autenticados. |
| Performance Testing    | Tiempo de respuesta bajo carga (GET <1s, POST/PUT <2s). |
| Boundary Value Testing | Entradas máximas/mínimas, campos vacíos, inputs inválidos. |

---

## ⚙️ Instalación y Ejecución

### Requisitos
- Python 3.11+
- Postman
- pytest, requests, pytest-html

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/Byte-Girls/api-testing.git
cd byte-girls-api-testing

# Crear entorno virtual


# Instalar dependencias



---

## 👥 Equipo de Trabajo

| Nombre                         | Rol              | Responsabilidades                        |
|-------------------------------|------------------|-----------------------------------------|
| Carolina Melendez             | QA Lead          | Coordinación, asignación, revisión      |
| Maria Calani Uvaldez          | Tester Developer | Diseño y ejecución de pruebas           |
| Jhesabel Cespedes             | Tester Developer | Diseño y ejecución de pruebas           |
| Katerine Isabel Rojas Calle   | Tester Developer | Diseño y ejecución de pruebas           |

                                                      
                                                      #  Anexos

## 🔍 Exploratory Testing
Durante las pruebas exploratorias se utilizó Postman para realizar peticiones manuales a los endpoints de la API de OrangeHRM, con los siguientes objetivos:

-Identificar comportamientos no documentados o inconsistencias en las respuestas.
-Explorar inputs límite o no válidos en tiempo real.
-Validar la robustez y mensajes de error generados por el sistema ante entradas inesperadas.
-Comparar la documentación pública de la API con la respuesta real.

## 📁 Exploratory Testing - Evidencia
La carpeta Exploratory Testing contiene la colección de Postman utilizada para realizar pruebas exploratorias sobre la API de OrangeHRM.

## Archivo	Descripción
Orange HRM API.postman_collection.json	Colección Postman con peticiones manuales y escenarios exploratorios. Incluye pruebas con entradas límite, inputs inválidos y respuestas de error.

##📄 Uso del archivo
Puedes importar el archivo JSON en Postman desde la opción:
File → Import → Upload File → Seleccionar Orange HRM API.postman_collection.json

