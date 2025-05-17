# Prueba Tecnica BircleAI

---

Este proyecto es una simple API utilizando FastAPI y LlamaIndex para una prueba tecnica.

### Requisitos

---

- Python version >= 3.9

### Datos importantes

---

- Se debe crear un directorio `/data` en el cual pondremos los documentos a indexar.
- Lo mas conveniente seria utilizar el indexador de LlamaIndex con OpenAI, pero para los fines de este proyecto (y falta de fondos) se utilizara [Groq](https://groq.com/) como modelo llm.
- Ademas, utilizaremos modelo HuggingFace para el embedding de los documentos en el directorio `/data`.

### Configuracion y Ejecucion

1. Clonar el repositorio en local e ingresar al directorio root `/prueba-tecnica`.

2. Una vez en el directorio root, se debe crear un entorno virtual, para ellos utilizamos el modulo [venv](https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3) de python.

En Linux/Mac:

```bash
python3 -m venv env
```

En windows:

```bash
python -m venv env
```

##### Activamos el entorno virtual:

En Linux/Mac

```bash
source env/bin/activate
```

En Windows

```bash
env\bin\activate.bat
```

3. Instalamos las dependencias del proyecto:

```bash
pip3 install -r requirements.txt
```

4. Creamos un archivo .env en el root directory y añadimos nuestra api key de la siguiente manera:

```env
GROQ_API_KEY='API KEY'
```

La api key de Groq se puede conseguir facilmente desde su [web](https://groq.com/).

5. Por ultimo, entramos al directorio `/app` y ejecutamos el proyecto:

```bash
cd app
uvicorn main:app --reload --host localhost --port 8000
```

Esto iniciara la API en `http://localhost:8000`.
