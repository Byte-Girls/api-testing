

                                                   # OrangeHRM API Test Automation

![Logo de Python](https://opensource-demo.orangehrmlive.com/web/images/ohrm_branding.png?v=1721393199309)

## Índice

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Objetivos](#objetivos)
- [Módulos Probados](#módulos-probados)
- [Limitaciones](#limitaciones)
- [Herramientas](#herramienetas)
- [Funcionalidades y Endpoints](#funcionalidades-y-endpoints)
  - [1. Administración de usuarios](#1-administración-de-usuarios)
  - [2. Estado de Empleado](#2-estado-de-empleado)
  - [3. Categorías de Trabajo](#3-categorías-de-trabajo)
- [Roles de Usuario](#roles-de-usuario)
- [Tipos de Pruebas Realizadas](#tipos-de-pruebas-realizadas)
- [Instalación y Ejecución](#instalación-y-ejecución)
  - [Requisitos](#requisitos)
  - [Clonación del Repositorio](#clonación-del-repositorio)
  - [Instalar dependencias](#instalar-dependencias)
  - [Obtener/Actualizar el token](#obteneractualizar-el-token)
  - [Ejecutar Test Cases](#-ejecutar-test-cases)
  - [Generar reporte HTML](#-generar-reporte-html)
  - [Ejecutar tests específicos](#ejecutar-tests-específicos)
    - [Por submódulo](#por-submódulo)
    - [Por archivo específico](#por-archivo-específico)
    - [Por etiqueta (mark)](#-por-etiqueta-mark)
- [Equipo de Trabajo](#equipo-de-trabajo)
- [Anexos](#anexos)
  - [Pruebas de exploracion](#pruebas-de-exploracion)
  - [Evidencia](#evidencia)
  - [Uso del archivo](#uso-del-archivo)

## Descripción del Proyecto
Este repositorio contiene las pruebas automatizadas de la API REST del sistema **OrangeHRM**, enfocado en el módulo de **Administración** especificamente en los submodulos (Estado de Empleado,Categorías de Trabajo y Administración de usuarios).

OrangeHRM es un sistema de gestión de recursos humanos (HRM) que permite administrar empleados, asistencia, licencias, reclutamiento y desempeño desde una plataforma centralizada.

---

## Objetivos
- Validar las funcionalidades del módulo Administración mediante pruebas automatizadas.
- Garantizar que los endpoints REST de la API cumplan con los requisitos funcionales.
- Documentar y automatizar casos de prueba positivos y negativos.
- Ejecutar pruebas exploratorias, funcionales, de humo (smoke) y regresión

---

## Módulos Probados
El presente plan de pruebas se enfocará exclusivamente en las funcionalidades del módulo Administración, cubriendo 
los siguientes submódulos a nivel de API:
- Administración de usuarios
- Estado de empleado
- Categorías de trabajo

---

## Limitaciones
* **Token de autenticación:**
No se prueba el flujo de login. En su lugar, se utiliza un token obtenido desde la [documentación](https://api-starter-orangehrm.readme.io/reference/try-it-yourself) pública de la API de OrangeHRM.
Este token se actualiza automáticamente mediante el script en python `src/utils/update_token_config.py`, el cual se ejecuta como parte del pipeline para correr los test cases con pytest.

---
## Herramienetas 
- **Postman**  para la ejecución y documentación sobre  la API REST de OrangeHRM. Estas estarán organizadas por colecciones
- **Python + Pytest**, utilizados para la creación de pruebas automatizadas y la integración con librerías que permitan validaciones sobre la API.

---
## Funcionalidades y Endpoints

### 1. Administración de usuarios

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

## Roles de Usuario
       Administrador: Puede acceder a todas las funcionalidades.

---

## Tipos de Pruebas Realizadas

| Tipo de Prueba         | Descripción |
|------------------------|-------------|
| Pruebas exploratorias  | Pruebas manuales con Postman para inputs límite, errores inesperados, comparación con documentación. |
| Pruebas funcionales    | Validación de casos positivos/negativos, estructura JSON, status codes. |
| Pruebas de humo (smoke)| Validación rápida de endpoints críticos. |
| Pruebas de regression  | Verificación de funcionalidades existentes tras cambios. |
| Pruebas de seguridad   | Validación de tokens y manejo de errores no autenticados. |
| Pruebas de rendimiento | Tiempo de respuesta bajo carga (GET <1s, POST/PUT <2s). |
| Pruebas valor limite   | Entradas máximas/mínimas, campos vacíos, inputs inválidos. |

---

## Instalación y Ejecución

### Requisitos
El sistema debe tener instalado los siguiete:
- Python 3.11 o superior
- Postman (opcional, para pruebas manuales)
- Git (para clonar el repositorio)
- pip (administrador de paquetes de Python)

### Clonación del Repositorio
```bash
git clone https://github.com/Byte-Girls/api-testing.git
cd api-testing
```

### Instalar dependencias
Se puede instalar todas las dependencias utilizando el archivo de requerimientos. Ejecuta el siguiente comando:
```
pip install -r requirements.txt
```

### Obtener/Actualizar el token
Ejecuta el siguiente comando para obtener el token desde la página web y actualizarlo en config.py:
```
python .\src\utils\update_token_config.py
```
Este comando extrae el token automáticamente y lo guarda en la variable TOKEN del archivo config.json

Como alternativa, puedes acceder al [enlace de esta página](https://api-starter-orangehrm.readme.io/reference/try-it-yourself) y copiar manualmente el token en el archivo config.json.

### Ejecutar Test Cases

Para ejecutar todos los test cases del proyecto, abre una terminal en la raíz del repositorio (`api-testing`) con Python y las dependencias instaladas. Luego ejecuta:

```bash
python -m pytest
```

---

### Generar reporte HTML

Para generar un reporte HTML después de ejecutar los tests:

```bash
python -m pytest --html=report.html
```

---

### Ejecutar tests específicos

#### Por submódulo
Ejecutar todos los test cases de un submódulo (por ejemplo, `employment_statuses`):

```bash
python -m pytest tests\opensource_demo_orangehrmlive\admin\employment_statuses
```

Otros ejemplos:

```bash
python -m pytest tests\opensource_demo_orangehrmlive\admin\job-categories
python -m pytest tests\opensource_demo_orangehrmlive\admin\users
```

#### Por archivo específico
Ejecutar un archivo de pruebas concreto o en otras palabras un test suite:

```bash
python -m pytest tests\opensource_demo_orangehrmlive\admin\employment_statuses\test_get_employment_status.py
```

#### Por etiqueta (mark)
Puedes ejecutar un grupo de pruebas usando una etiqueta (mark/tag):

```bash
python -m pytest -m <tag-name>
```

**Etiquetas disponibles:**

```ini
markers =
    smoke: tests de humo (verifican funciones básicas)
    regression: tests de regresión
    funcional: tests funcionales
    negativo: tests de escenarios negativos
    positivo: tests de escenarios positivos
    seguridad: tests para validar manejo de tokens inválidos o ausentes
    rendimiento: tests para medir tiempos de respuesta
    valor_limite: tests con entradas mínimas/máximas o inválidas
```

## Equipo de Trabajo

| Nombre                        | Rol              | Responsabilidades                       |
|-------------------------------|------------------|-----------------------------------------|
| Carolina Melendez             | QA Lead          | Coordinación, asignación, revisión +Diseño e implentación |
| Maria Calani Uvaldez          | Tester Developer | Diseño e implentación de pruebas automatizadas  |
| Jhesabel Cespedes             | Tester Developer | Diseño e implentación de pruebas automatizadas  |
| Katerine Isabel Rojas Calle   | Tester Developer | Diseño e implentación de pruebas automatizadas  |

                                                      
                                                      #  Anexos

## Pruebas de exploracion
Durante las pruebas exploratorias se utilizó Postman para realizar peticiones manuales a los endpoints de la API de OrangeHRM, con los siguientes objetivos:

- Identificar comportamientos no documentados o inconsistencias en las respuestas.
- Explorar inputs límite o no válidos en tiempo real.
- Validar la robustez y mensajes de error generados por el sistema ante entradas inesperadas.
- Comparar la documentación pública de la API con la respuesta real.

### Evidencia
La carpeta Exploratory Testing contiene la colección de Postman utilizada para realizar pruebas exploratorias sobre la API de OrangeHRM.

- **Orange HRM API.postman_collection.json**

### Uso del archivo
Puedes importar el archivo JSON en Postman desde la opción:
File → Import → Upload File → Seleccionar Orange HRM API.postman_collection.json

