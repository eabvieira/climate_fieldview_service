from app.core.services import climate_fieldview_get, climate_fieldview_post, climate_fieldview_put

_growers_url = 'fields/api/'


def get_all_growers(params):
    """
    [
    Retorna uma lista de todos os produtores. É possível passar alguns parâmetros de consulta.]

    Args:
        params ([dict]): [parametros de consulta.
        Podem ser os seguintes:
          provider (string) - apenas produtores do provedor especificado.
          leafUserId (string[UUID]) - apenas produtores do usuário especificado.
          page (int) - um inteiro especificando a página sendo requisitada.
          size (int) - um inteiro especificando o tamanho da página (padrão é 20).
        ]

    Returns:
    [list]: [returns a list of all growers.
    Exemplo da Response:
      [
        {
          "id": 2345,
          "leafUserId": "UUID",
          "providerName": "str",
          "providerOrganizationId": "str",
          "providerCompanyId": "str",
          "providerUserId": "str",
          "providerGrowerId": "str",
          "farmIds": [4534]
        }
      ]
    ]
    """
    all_growers_endpoint = _growers_url + 'growers'
    all_growers = climate_fieldview_get(f'{all_growers_endpoint}', params)

    return all_growers


def get_grower(user_id, grower_id):
    """[Retorna um produtor específico pelo seu id e do usuário.]

    Args:
        user_id ([string]): [ deve conter o id do usuário requisitado.]
        grower_id ([string]): [ deve conter o id do produtor requisitado.]

    Returns:
        [dict]: [ retorna as informações do produtor.
          Exemplo da response:
          {
            "id": 2345,
            "name": "str",
            "leafUserId": "UUID",
            "providerName": "str",
            "providerOrganizationId": "str",
            "providerCompanyId": "str",
            "providerUserId": "str",
            "providerGrowerId": "str",
            "farmIds": [4534]
          }
        ]
    """

    grower_endpoint = _growers_url + f'users/{user_id}/growers/{grower_id}'
    grower = climate_fieldview_get(f'{grower_endpoint}')
    return grower


def new_grower(user_id, grower_name):
    """[Creates a grower for the user leafUserId. It's possible to pass name on the body of the request.
     Cria um produtor para o usuário user_id. É possível passar tanto o nome do produtor quanto o id do ganhador no corpo da requisição.]

    Args:
        user_id ([string]): [ deve conter o id do usuário requisitado.]
        grower_name ([string]): [ deve conter o nome do produtor.]

    Returns:
        [dict]: [ retorna as informações do produtor.]
    """

    new_grower_endpoint = _growers_url + f'users/{user_id}/growers'
    payload = {
        "name": grower_name
    }
    grower = climate_fieldview_post(f'{new_grower_endpoint}', payload)
    return grower


def update_grower(user_id, grower_id, grower_name):
    """[
     Atualiza um produtor para o usuário user_id. É possível passar tanto o nome do produtor quanto o id do ganhador no corpo da requisição.]

    Args:
        user_id ([string]): [ deve conter o id do usuário requisitado.]
        grower_id ([string]): [ deve conter o id do produtor a ser atualizado.]
        grower_name ([string]): [ deve conter o nome do produtor.]

    Returns:
        [dict]: [ retorna as informações do produtor.]
    """

    update_grower_endpoint = _growers_url + \
        f'users/{user_id}/growers/{grower_id}'
    payload = {
        "name": grower_name
    }
    grower = climate_fieldview_put(f'{update_grower_endpoint}', payload)
    return grower
