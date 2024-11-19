# Proyecto-de-Licitaciones-y-TDRs
Este repositorio contiene el desarrollo de una aplicación web diseñada para gestionar procesos de licitación y evaluación técnica/económica. El proyecto está basado en **Django** para el backend y se conecta con una base de datos MySQL para manejar datos relacionados con usuarios, licitaciones y términos de referencia (TDRs). 

## Funcionalidades Principales

- **Autenticación de Usuarios**:
  - Login y registro de usuarios con roles definidos (admin, licitador, evaluador).
  - Gestión de sesiones seguras con autenticación basada en tokens (JWT).
  
- **Gestión de Licitaciones**:
  - Creación, consulta, edición y eliminación de licitaciones.
  - Consulta de Términos de Referencia (TDRs) asociados a licitaciones.

- **Interfaz de Usuario**:
  - Diseño responsivo para una experiencia óptima en diferentes dispositivos.
  - Formulario de login, dashboard de licitaciones y vistas de detalle.

- **Base de Datos Externa**:
  - Conexión a una base de datos MySQL para almacenar información de usuarios, licitaciones y TDRs.

---

## Tecnologías Utilizadas

- **Backend**:
  - Django 4.2
  - Django REST Framework (DRF) para la API RESTful
  - MySQL para almacenamiento de datos
- **Frontend**:
  - HTML5, CSS3
  - Framework CSS: Bootstrap
- **Herramientas**:
  - Git y GitHub para control de versiones
  - Postman para pruebas de API
  - MySQL Workbench para diseño y gestión de la base de datos

---

## Instalación y Configuración

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clonar el Repositorio
`bash
git clone https://github.com/usuario/repo-licitaciones.git
cd repo-licitaciones

###  1. Configurar un Entorno Virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
