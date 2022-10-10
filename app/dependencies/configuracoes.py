from app.core.services import climate_fieldview_get, climate_fieldview_post, climate_fieldview_patch,  climate_fieldview_delete

_configs_url = 'config/api/configs/'


async def get_owner_configs():
    """[Retorna as configs do proprietário da API.
    Returns:
      [dict]: [retorna a configuração do proprietário da API]
    """

    owner_configs = await climate_fieldview_get(f'{_configs_url}')

    return owner_configs


async def get_user_configs(user_id):
    """[Retorna as configs de um usuario.]
    Args:
      user_id ([string]): [deve conter o id do usuário requisitado.]
    Returns:
      [dict]: [retorna as configs do usuário]
    """

    user_configs = await climate_fieldview_get(f'{_configs_url}{user_id}')

    return user_configs


def new_user_config(payload):
    """[Cria a config para um usuário. Um payload deve ser enviado contendo as configs a serem setadas. Todas as entradas são opcionais, qualquer config que não seja setada será herdada da config do proprietário da API.
    geoimagesColorRamp é uma dict de listas com as cores da rampa de cores.
    Exemplo: 
        "geoimagesColorRamp": {
        "0%"  : [200,   0, 0],
        "35%" : [255,  40, 0],
        "45%" : [255, 150, 0],
        "55%" : [255, 240, 0],
        "65%" : [  0, 230, 0],
        "75%" : [  0, 190, 0],
        "100%": [  0, 130, 0],
        "nv"  : [  0,   0, 0, 0]
      }
    ]
    Args:
      payload ([dict]): [deve conter todas as configs a serem setadas.]

    Returns:
      [dict]: [retorna a configuração atualizada]
  """
    payload = {
        "apiOwnerUsername": payload.api_owner_username,
        "operationsImageCreation": payload.operations_image_creation,
        "geoimagesResolution": payload.geoimages_resolution,
        "geoimagesShape": payload.geoimages_shape,
        "geoimagesProjection": payload.geoimages_projection,
        "geoimagesColorRamp": payload.geoimages_color_ramp,
        "fieldsAutoSync": payload.fields_auto_sync,
        "fieldsMergeIntersection": payload.fields_merge_intersection,
        "fieldsAttachIntersection": payload.fields_attach_intersection
    }

    return climate_fieldview_post(payload, '{_configs_url}')


def update_owner_config(payload):
    """[Atualiza os campos especificados de Configuração para o Proprietário da API. Um payload deve ser enviado contendo as configurações a serem setadas. Todas as entradas são opcionais.
    geoimagesColorRamp é uma dict de listas com as cores da rampa de cores.
    Exemplo: 
        "geoimagesColorRamp": {
        "0%"  : [200,   0, 0],
        "35%" : [255,  40, 0],
        "45%" : [255, 150, 0],
        "55%" : [255, 240, 0],
        "65%" : [  0, 230, 0],
        "75%" : [  0, 190, 0],
        "100%": [  0, 130, 0],
        "nv"  : [  0,   0, 0, 0]
      }
    ]
    ]

    Args:
        payload ([dict]): [deve conter todas as configs a serem setadas.]

    Returns:
        [dict]: [retorna a configuração atualizada]
    """
    payload = {
        "apiOwnerUsername": payload.api_owner_username,
        "operationsImageCreation": payload.operations_image_creation,
        "geoimagesResolution": payload.geoimages_resolution,
        "geoimagesShape": payload.geoimages_shape,
        "geoimagesProjection": payload.geoimages_projection,
        "geoimagesColorRamp": payload.geoimages_color_ramp,
        "fieldsAutoSync": payload.fields_auto_sync,
        "fieldsMergeIntersection": payload.fields_merge_intersection,
        "fieldsAttachIntersection": payload.fields_attach_intersection
    }
    return climate_fieldview_patch(payload, '{_configs_url}')


def update_user_config(payload, user_id):
    """[Atualiza os campos especificados de Configuração para o Usuário da API. Um payload deve ser enviado contendo as configurações a serem setadas. Todas as entradas são opcionais.
    geoimagesColorRamp é uma dict de listas com as cores da rampa de cores.
    Exemplo: 
        "geoimagesColorRamp": {
        "0%"  : [200,   0, 0],
        "35%" : [255,  40, 0],
        "45%" : [255, 150, 0],
        "55%" : [255, 240, 0],
        "65%" : [  0, 230, 0],
        "75%" : [  0, 190, 0],
        "100%": [  0, 130, 0],
        "nv"  : [  0,   0, 0, 0]
      }
    ]

    Args:
        payload ([dict]): [deve conter todas as configs a serem setadas.]
        user_id ([string]): [deve conter o id do usuário requisitado.]
    Returns:
        [dict]: [retorna a configuração atualizada]
    """
    payload = {
        "apiOwnerUsername": payload.api_owner_username,
        "operationsImageCreation": payload.operations_image_creation,
        "geoimagesResolution": payload.geoimages_resolution,
        "geoimagesShape": payload.geoimages_shape,
        "geoimagesProjection": payload.geoimages_projection,
        "geoimagesColorRamp": payload.geoimages_color_ramp,
        "fieldsAutoSync": payload.fields_auto_sync,
        "fieldsMergeIntersection": payload.fields_merge_intersection,
        "fieldsAttachIntersection": payload.fields_attach_intersection
    }

    return climate_fieldview_patch(payload, '{_configs_url}', user_id)


def delete_usuario(id):
    """[Deleta a configuração do usuário. Até que uma nova configuração seja criada, o usuário será herdado todas as configurações do proprietário da API.]

    Args:
        id ([string]): [id do usuário a ser deletado]
    """
    return climate_fieldview_delete(f'{_configs_url}', id)
