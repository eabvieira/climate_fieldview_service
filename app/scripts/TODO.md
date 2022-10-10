# TODO:

carga de tipo solo - OK
```json
[{
    "dominio": "tipos_solo",
    "internal_id": 0,
    "integration_id": 1,
    "slug": "tipo-1",
    "label": "Tipo 1"
},
{
    "dominio": "tipos_solo",
    "internal_id": 0,
    "integration_id": 2,
    "slug": "tipo-2",
    "label": "Tipo 2"
},
{
    "dominio": "tipos_solo",
    "internal_id": 0,
    "integration_id": 3,
    "slug": "tipo-3",
    "label": "Tipo 3"
}
]
```

carga de coberturas (com codigo climate_fieldview e labels) - OK
exemplo:
```json
[
{
    "dominio": "coberturas",
    "internal_id": 1,
    "integration_id": 2030,
    "slug": "geada-e-temperaturas-baixas",
    "label": "Geada e temperaturas baixas",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 2,
    "integration_id": 2006,
    "slug": "granizo",
    "label": "Granizo",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 3,
    "integration_id": 2009,
    "slug": "incendio-e-raio",
    "label": "Incendio E Raio",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 4,
    "integration_id": 2018,
    "slug": "replantio",
    "label": "Replantio",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 5,
    "integration_id": 2021,
    "slug": "tratamento-fitossanitario",
    "label": "Tratamento Fitossanitario",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 6,
    "integration_id": 2002,
    "slug": "chuvas-excessivas",
    "label": "Chuvas Excessivas",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 7,
    "integration_id": 2005,
    "slug": "geada",
    "label": "Geada",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 8,
    "integration_id": 2010,
    "slug": "incendio-e-raio",
    "label": "Incendio E Raio",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 9,
    "integration_id": 2011,
    "slug": "inundacao",
    "label": "Inundacao",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 10,
    "integration_id": 2011,
    "slug": "nao-germinacaonao-emergencia-replantio",
    "label": "Nao Germinacaonao Emergencia Replantio",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 11,
    "integration_id": 2019,
    "slug": "seca",
    "label": "Seca",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 12,
    "integration_id": 2022,
    "slug": "tromba-d-agua",
    "label": "Tromba d'agua",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 13,
    "integration_id": 2024,
    "slug": "variacao-excessiva-de-temperatura",
    "label": "Variacao Excessiva de temperatura",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 14,
    "integration_id": 2025,
    "slug": "ventos-fortes",
    "label": "Ventos Fortes",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 15,
    "integration_id": 2026,
    "slug": "ventos-frios",
    "label": "Ventos Frios",
    "cultura_slug": "soja"
},
{
    "dominio": "coberturas",
    "internal_id": 16,
    "integration_id": 2031,
    "slug": "perda-de-qualidade",
    "label": "Perda de qualidade",
    "cultura_slug": "soja"
}
]
```

carga de previsao de colheita default para culturas  - OK
```json
{
    "dominio": "data_prevista_fim_default",
    "internal_id": 0,
    "integration_id": 1,
    "slug": "soja",
    "label": "Soja",
    "default": "30/04/2022"
}
```


carga de formas pagamento - OK
```json
[
{
    "dominio": "formas_pagamento",
    "internal_id": 0,
    "integration_id": 1,
    "slug": "boleto",
    "label": "Boleto"
},
{
    "dominio": "formas_pagamento",
    "internal_id": 0,
    "integration_id": 6,
    "slug": "debito-em-conta",
    "label": "Débito em conta"
}    
]
```

carga de Regulacao de Sinistro - OK
```json
[
{
    "dominio": "regulacao_sinistro",
    "internal_id": 0,
    "integration_id": 0,
    "slug": "nao-informado",
    "label": "Não informado"
},
{
    "dominio": "regulacao_sinistro",
    "internal_id": 0,
    "integration_id": 1,
    "slug": "media-geral",
    "label": "Média Geral"
},
{
    "dominio": "regulacao_sinistro",
    "internal_id": 0,
    "integration_id": 2,
    "slug": "talhonado",
    "label": "Talhonado"
}
]
```

• 0 – Não informado;
• 1 – Média geral;
• 2 – Por talhão;
