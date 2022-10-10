from app.core.services import climate_fieldview_get, climate_fieldview_post, climate_fieldview_put

_farms_url = 'fields/api/'


def get_all_farms(params):
    """[Gets a paged list of all farms. It is possible to pass some query parameters.
      Retorna uma lista de todas as fazendas. É possível passar alguns parâmetros de consulta.]
    Args:
        params ([dict]): [parametros de consulta.
        Podem ser os seguintes:
        - provider (string) - apenas fazendas do provedor especificado.
        - leafUserId (string[UUID]) - apenas fazendas do usuário especificado.
        - page (int) - um inteiro especificando a página sendo requisitada.
        - size (int) - um inteiro especificando o tamanho da página (padrão é 20).
        ]
    Returns:
        [list]: [returns a list of all farms.
          Exemplo da Response:
          [
            {
              "id": 1538766,
              "name": "name",
              "providerId": 2,
              "providerName": "JohnDeere",
              "providerFarmId": "00000000-0000-0000-0000-000000000000",
              "leafUserId": "00000000-0000-0000-0000-000000000000",
              "fieldIds": ["00000000-0000-0000-0000-000000000000"],
              "growerId": 12345
            }
          ]
        ]
    """
    all_farms_endpoint = _farms_url + 'farms'
    farms = climate_fieldview_get(f'{all_farms_endpoint}', params)

    return farms


def get_farm(user_id, farm_id):
    """[Retorna uma fazenda específica pelo seu id e do usuário.
    ]

    Args:
        user_id ([string]): [deve conter o id do usuário requisitado.]
        farm_id ([string]): [deve conter o id da fazenda requisitada.]

    Returns:
        [dict]: [ retorna as informações da fazenda.
          Exemplo da response:
          {
            "id": 1551010,
            "name": "name",
            "providerName": "JohnDeere",
            "providerFarmId": "00000000-0000-0000-0000-000000000000",
            "leafUserId": "00000000-0000-0000-0000-000000000000",
            "fieldIds": ["00000000-0000-0000-0000-000000000000"],
            "growerId": 123
          }
        ]
    """

    farm_endpoint = _farms_url + f'users/{user_id}/farms/{farm_id}'
    farm = climate_fieldview_get(f'{farm_endpoint}')
    return farm


def new_farm(user_id, grower_id, farm_name=''):
    """[
    Cria uma fazenda para o usuário user_id. É possível passar tanto o nome da fazenda quanto o id do ganhador no corpo da requisição.]

    Args:
        user_id ([string]): [ deve conter o id do usuário requisitado.]
        farm_name ([string]): [ deve conter o nome da fazenda.]
        grower_id ([int]): [ deve conter o id do produtor.]

    Returns:
        [dict]: [O JSON da nova fazendo]
    """
    create_farm_endpoint = _farms_url + f'users/{user_id}/farms'
    payload = {
        "name": farm_name,
        "growerId": grower_id
    }
    new_farm = climate_fieldview_post(payload, f'{create_farm_endpoint}')
    return new_farm


def update_farm(user_id, farm_id, grower_id, farm_name=''):
    """[
    Atualiza a fazenda com id id para o usuário user_id. É possível passar tanto o nome da fazenda quanto o id do produtor no corpo da requisição.]

    Args:
        user_id ([string]): [ deve conter o id do usuário requisitado.]
        farm_id ([string]): [ deve conter o id da fazenda.]
        farm_name ([string]): [ deve conter o nome da fazenda.]
        grower_id ([int]): [ deve conter o id do produtor.]
    Returns:
        [dict]: [ O JSON da fazenda atualizada]
    """
    update_farm_endpoint = _farms_url + f'users/{user_id}/farms/{farm_id}'
    payload = {
        "name": farm_name,
        "growerId": grower_id
    }
    update_farm = climate_fieldview_put(payload, f'{update_farm_endpoint}')

    return update_farm
