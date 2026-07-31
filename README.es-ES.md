

# Custom Data GPT

[![label](https://img.shields.io/badge/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3-ZH-brightgreen)](https://github.com/aboutmydreams/custom_data_gpt/blob/main/README_ZH.md)
[![label](https://img.shields.io/badge/English-EN-brightgreen)](https://github.com/aboutmydreams/custom_data_gpt/blob/main/README.md)
[![label](https://img.shields.io/badge/aiis.life-AI%20is%20life-orange)](https://www.aiis.life)
[![label](https://img.shields.io/badge/NonceGeek-cool--oriented%20programming-orange)](https://noncegeek.com)



Este proyecto es un chatbot basado en OpenAI, adecuado para el ajuste fino de datos privados de empresas. Puede responder diversas preguntas relacionadas con productos empresariales planteadas por los usuarios. Utiliza la API de OpenAI para el entrenamiento y generación de modelos de lenguaje, y emplea Faiss para la búsqueda de texto y coincidencia de similitud. Admite la obtención de datos de entrenamiento desde archivos locales o URL. Este proyecto es una versión mejorada de [Custom-Company-Chatbot](https://replit.com/@DavidAtReplit/Custom-Company-Chatbot), inspirada en el proyecto original, extendiendo la adquisición de datos privados desde la red y de forma local (en principio, no se trata de un entrenamiento real, sino de encontrar contextos relevantes y luego indicárselos a GPT). Gracias a [@leeduckgo](https://github.com/leeduckgo) por el inspirador apoyo.

## Pasos para usarlo

1. Añade `API_SECRET=MySecret` y `OPENAI_API_KEY=<your-key>` al archivo `.env`, donde `<your-key>` es tu [Clave API de OpenAI](https://beta.openai.com/account/api-keys).
2. Instala las dependencias requeridas para el proyecto usando poetry:
   - `pip install poetry`
   - `poetry install`
   - `poetry shell`
3. Activa el entorno virtual y ejecuta `python3 main_api.py`.
4. Envía una solicitud de entrenamiento mediante una petición HTTP POST a [http://localhost:5000/train](http://localhost:5000/train), pasando la lista de archivos de datos de entrenamiento y el nombre del modelo.
5. Envía una solicitud de chat mediante una petición HTTP POST a [http://localhost:5000/chat](http://localhost:5000/chat), pasando el nombre del modelo, la pregunta y el historial.

## Documentación de la API

### /train

Esta interfaz se utiliza para el entrenamiento del modelo de lenguaje.

#### Solicitud

- Método: POST
- Cuerpo de la solicitud: formato JSON
- Parámetros del cuerpo de la solicitud:
  - `file_list`: Una lista de archivos para entrenar
  - `space_name`: El nombre del espacio vectorial
  - `file_tag`: `url` (datos de texto de red) o `path` (datos locales) para los datos

```json
{
    "file_list": ["https://cdn.vitae3.me/public-static/213113032213132120.1680148867987.txt"],
    "space_name": "train_space_name",
    "file_tag": "url",
}
```

#### Respuesta

- Código de estado: 200
- Cuerpo de la respuesta: formato JSON
- Parámetros del cuerpo de la respuesta:
  - `code`: mensaje de estado, 0 normal, 1 anormal
  - `data`: datos
  - `msg`: éxito

```json
{
  "code": 0,
  "data": {
    "index_space_size": 6.0439,
    "space_name": "train_space_name",
    "pkl_space_size": 2.4023,
    "size_type": "kb"
  },
  "msg": "success"
}
```

### /chat

Esta API se utiliza para las conversaciones del chatbot.

#### Solicitud de chat

- Método: POST
- Cuerpo de la solicitud: formato JSON
- Parámetros del cuerpo de la solicitud:
  - `space_name`: el nombre del espacio vectorial almacenado localmente
  - `question`: la pregunta que se realiza
  - `history`: el historial de la conversación
  - `model_name`: el nombre del modelo, ej: text-davinci-003, gpt-3.5-turbo, gpt-3.5-turbo-0301, puedes probar más modelos de generación de lenguaje en la [Lista de Modelos](https://platform.openai.com/docs/models) y consultar los precios de los diferentes modelos en la [Lista de Precios](https://openai.com/pricing).

```json
{
  "history": ["human: cómo estás", "Bot: bien"],
  "question": "Cómo construir un chatbot GPT3 para tu empresa",
  "space_name": "train_space_name",
  "model_name": "text-davinci-003",
}
```

#### Respuesta de chat

- Código de estado: 200
- Cuerpo de la respuesta: formato JSON
- Parámetros del cuerpo de la respuesta:
  - `code`: información de estado, 0 normal, 1 excepción
  - `data`: datos
  - `msg`: éxito

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "answer": " Construir un chatbot GPT3 para tu empresa requiere algunos pasos. Primero, necesitas obtener tu clave API de OpenAI y agregarla a Secrets como OPENAI_API_KEY. Luego, necesitas crear una API_KEY para la API JSON. Después, debes llenar la carpeta training/facts con tantos documentos de texto como sea posible que contengan información sobre la empresa en la que lo estás entrenando. Finalmente, necesitas editar el archivo prompt/master.txt para representar cómo quieres que se comporte el bot al interactuar con los usuarios.",
        "history": [
            "human: cómo estás",
            "Bot: bien",
            "Human: Cómo construir un chatbot GPT3 para tu empresa",
            "Bot:  Construir un chatbot GPT3 para tu empresa requiere algunos pasos. Primero, necesitas obtener tu clave API de OpenAI y agregarla a Secrets como OPENAI_API_KEY. Luego, necesitas crear una API_KEY para la API JSON. Después, debes llenar la carpeta training/facts con tantos documentos de texto como sea posible que contengan información sobre la empresa en la que lo estás entrenando. Finalmente, necesitas editar el archivo prompt/master.txt para representar cómo quieres que se comporte el bot al interactuar con los usuarios."
        ]
    }
}
```

## Notas

- Este proyecto está desarrollado con Python 3.10 y es únicamente con fines de aprendizaje e investigación. Por favor, no lo utilices para ningún propósito que pueda dañar el entorno social.
- Si tienes una gran cantidad de texto, el entrenamiento tardará mucho tiempo y requerirá muchos recursos de cómputo.
- Por favor, lee la documentación y el código detenidamente antes de usarlo, y asegúrate de que la clave API y los datos de entrenamiento estén configurados correctamente.

Bienvenido a unirte a la comunidad temprana de Custom AI en chino

<p>
  <img alt="QQ-Group" src="https://cdn.nlark.com/yuque/0/2023/png/164272/1680279312300-35636818-45ad-41ce-b0c7-d86aba020a2e.png?x-oss-process=image%2Fresize%2Cw_962%2Climit_0" width="300" style="border-radius: 10%;">
  <img alt="WX-Group" src="https://cdn.nlark.com/yuque/0/2023/png/164272/1680278249286-59ac3cbd-a27b-4c54-87a1-3dd6f9cd46e0.png" width="300" style="border-radius: 10%;">
</p>
