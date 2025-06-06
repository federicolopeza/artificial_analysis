# Artificial Analysis API Documentation

## Visión general y acceso
Artificial Analysis proporciona APIs para apoyar el análisis de modelos de IA y tomar decisiones informadas sobre cuáles usar.

Ofrecemos:
- **Free API**: centrada en benchmarks de modelos.
- **Commercial API**: datos más completos.

Para acceder a la Free API, crea una cuenta en la plataforma Artificial Analysis Insights y genera una clave de API.

Cuando integres nuestra API, incluye tu clave en el header `x-api-key`. Recomendamos usar IDs de modelo y creador como identificadores primarios, ya que son estables (los slugs y nombres pueden cambiar).

---

## Atribución y uso de datos
Es obligatoria la atribución para todo uso de la Free API. Por favor, menciona:

https://artificialanalysis.ai/

Si deseas incluir nuestro logo, descarga nuestro brand kit aquí: [Artificial Analysis Brand Kit](Artificial Analysis Brand Kit).

---

## Metodología
Para detalles sobre cómo se realizan los benchmarks, consulta nuestra documentación de metodología.

---

## Autenticación
- **Header requerido**: `x-api-key: tu_api_key_aquí`
- **Códigos de error**:
  - **401**: API key inválida o faltante
  - **429**: Límite de solicitudes excedido
  - **500**: Error interno del servidor

---

## Seguridad y uso
Las claves de API son sensibles. Nunca las compartas en repositorios públicos ni las expongas en código cliente.

Las claves de API se usan para autenticar solicitudes a la Artificial Analysis API. Incluye tu clave en el header `x-api-key` en cada petición.

---

## Commercial API
Además de la Free API enfocada en benchmarks de modelos, ofrecemos una Commercial API con **datos más completos y capacidades ampliadas**. Incluye:
- Modalidades no lingüísticas (Speech-to-Text, Text-to-Speech, Speech-to-Speech, Text-to-Image, Text-to-Video)
- Benchmarks de diferentes longitudes de prompt (por ejemplo, 10k, 100k tokens)
- Benchmarks por proveedor (Azure, Amazon Bedrock, Together.ai, etc.)
- Y más.

Si estás interesado en acceder a nuestra Commercial API, contáctanos para hablar de tus necesidades.

---

## Free API
La Free API comparte métricas primarias de nuestros benchmarks de modelos, incluyendo evaluaciones de inteligencia, velocidad y precios.

- Límite de **1,000 requests/día**. No expongas tu API key en código cliente; cachea las respuestas.

### Endpoint: Modelos

`GET https://artificialanalysis.ai/api/v2/data/llms/models`

#### Campos de la respuesta

| Campo                                 | Tipo    | Descripción                                                                                          |
|---------------------------------------|---------|------------------------------------------------------------------------------------------------------|
| `id`                                  | string  | Identificador único (estable)                                                                        |
| `name`                                | string  | Nombre completo (puede cambiar)                                                                      |
| `slug`                                | string  | Identificador amigable para URLs (rara vez cambia)                                                   |
| `model_creator`                       | object  | Información del creador (`id`, `name`, `slug`)                                                       |
| `evaluations`                         | object  | Puntuaciones de benchmark                                                                             |
| `pricing`                             | object  | Precio por millón de tokens (USD)                                                                    |
| `median_output_tokens_per_second`     | number  | Velocidad de generación de tokens (tokens/segundo)                                                   |
| `median_time_to_first_token_seconds`  | number  | Tiempo hasta el primer token (segundos)                                                              |
| `median_time_to_first_answer_token`   | number  | Tiempo hasta el primer token de respuesta (segundos; diferente del primero para modelos de razonamiento) |

#### Ejemplo de solicitud

```bash
curl -X GET "https://artificialanalysis.ai/api/v2/data/llms/models" \
  -H "x-api-key: tu_api_key_aquí"
```

#### Ejemplo de respuesta

```json
{
  "status": 200,
  "prompt_options": {
    "parallel_queries": 1,
    "prompt_length": "medium"
  },
  "data": [
    {
      "id": "2dad8957-4c16-4e74-bf2d-8b21514e0ae9",
      "name": "o3-mini",
      "slug": "o3-mini",
      "release_date": "2025-01-31",
      "model_creator": {
        "id": "e67e56e3-15cd-43db-b679-da4660a69f41",
        "name": "OpenAI",
        "slug": "openai"
      },
      "evaluations": {
        "artificial_analysis_intelligence_index": 62.9,
        "artificial_analysis_coding_index": 55.8,
        "artificial_analysis_math_index": 87.2,
        "mmlu_pro": 0.791,
        "gpqa": 0.748,
        "hle": 0.087,
        "livecodebench": 0.717,
        "scicode": 0.399,
        "math_500": 0.973,
        "aime": 0.77
      },
      "pricing": {
        "price_1m_blended_3_to_1": 1.925,
        "price_1m_input_tokens": 1.1,
        "price_1m_output_tokens": 4.4
      },
      "median_output_tokens_per_second": 153.831,
      "median_time_to_first_token_seconds": 14.939,
      "median_time_to_first_answer_token": 14.939
    }
    // Otros modelos...
  ]
}
```