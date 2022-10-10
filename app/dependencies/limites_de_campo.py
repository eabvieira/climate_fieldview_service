from app.core.services import climate_fieldview_get, climate_fieldview_post, climate_fieldview_put, climate_fieldview_delete

_field_boundaries_url = 'fields/api/'


def get_all_fields(params={}):
    """
    [Retorna uma lista de campos com páginas de resultados. É possível filtrar os resultados passando alguns parâmetros de consulta.]
    Params:
      - type, retorna somente campos com este tipo (string).
      - provider, retorna somente campos com este provider (string).
      - leafUserId, retorna somente campos deste usuário (string).
      - page, um número inteiro que especifica a página sendo buscada.
      - size, inteiro que especifica o tamanho da página (padrão é 20).


    Returns:
        [list]: [retorna uma lista de todos os campos]
    """
    fields = climate_fieldview_get(f'{_field_boundaries_url}fields', params)

    return fields


def get_field(user_id, field_id):
    """
    [
      Retorna um campo específico de um usuário com base no id de ambos .
    ]
    Args:
      user_id ([string]): [deve conter o id do usuário associado ao campo]
      field_id ([string]): [deve conter o id do campo requisitado]

    Returns:
        [dict]: [retorna as informações do campo]
    """
    get_field_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/{field_id}'
    field = climate_fieldview_get(get_field_endpoint)

    return field


def new_field(user_id, coordinates):
    """
    [Cria um Campo para o usuario user_id. O payload deve ser enviado contendo a chave "geometry", que representa os limites do Campo a ser criado com o formato GeoJSON (deve ser um "MultiPolygon").
    O id é opcional. Se ele não for informado, um UUID será gerado. O campo NÃO PODE ser alterado.
    Exemplo de payload:
      {
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
            [
              [
                [-93.48821327980518, 41.77137549568163],
                [-93.48817333680519, 41.77143534378164],
                [-93.48821327390516, 41.76068857977987],
                [-93.48821327980518, 41.77137549568163]
              ]
            ]
          ]
        }
      }]
    Args:
        user_id ([string]): [usuario ao qual o campo pertence]
        payload ([dict]): [deve conter as informações do da geometria do campo]
    Returns:
        [dict]: [retorna um campo como um objeto JSON]
    """
    create_field_endpoint = _field_boundaries_url + f'users/{user_id}/fields'
    payload = {
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": coordinates
        }
    }

    new_field = climate_fieldview_post(payload, create_field_endpoint)

    return new_field


def get_all_field_operations(user_id, field_id, params={}):
    """
   [ Retorna uma lista de todos os arquivos de operação de um campo específico.
    É possivel filtrar os resultados passando alguns parâmetros de consulta. Eles estão listados abaixo.

  Params:
    - operationType	  ([String]):                       "harvested", "planted", "applied" ou "other" retorna as operações de um destes tipos.
    - provider	      ([String]):                       "ClimateFieldView"	retorna as operações deste provider.
    - origin	        ([String]):                       "provider", "automerged", "merged" or "uploaded"	retorna as operações desta origem.
    - crop          	([String]):                       nome da cultura, como "corn" ou "soybeans". A lista completa de culturas está disponível aqui. Um nome da cultura é case sentitive.
    - page          	([Integer]):                      um número inteiro que especifica a página sendo buscada.
    - size          	([Integer]):                      inteiro que especifica o tamanho da página (padrão é 20).
    - startTime	      ([ISO 8601 datetime format]):	    retorna as operações que começaram após esta data.
    - endTime	        ([ISO 8601 datetime format]):	    retorna as operações que terminaram antes desta data.
    - page            ([int])                           especifica qual página a ser buscada (default is 0)
    - size            ([int])                           especifica o tamanho da página (default is 20, max is 100)
]
    Args:
        user_id ([string]): [id do usuario associado a este campo]
        field_id ([string]): [id do campo requisitado]

    Returns:
    [list]: [A JSON array of Files. Uma lista JSON de arquivos.]
    """

    get_all_field_operations_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/{field_id}/operations'

    all_field_operations = climate_fieldview_get(
        get_all_field_operations_endpoint, params)

    return all_field_operations


def get_operation_of_field(user_id, field_id, operation_id):
    """
   [Retorna um arquivo de operação específico de um campo pelo seu id.]
    Args:
        user_id ([string]): [id do usuario associado a este campo]
        field_id ([string]): [id do campo requisitado]
        operation_id ([string]): [id da operação requisitada]

    Returns:
      [dict] :Um arquivo único da operação.
    """

    get_operation_of_field_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/{field_id}/operations/{operation_id}'

    operation_of_field = climate_fieldview_get(
        get_operation_of_field_endpoint)

    return operation_of_field


def get_fields_by_geometry(user_id, coordinates, threshold=0.01):
    """
    [Retorna uma lista de campos que intersectam com o MultiPolygon enviado no corpo da requisição. O percentual de interseção mínimo é dado por intersectionThreshold, o valor padrão é 0.01%.

    Exemplo de resposta JSON:
    [
      {
        "id": "id",
        "leafUserId": "uuid",
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
            [
              [
                [-89.84388470649719,39.71943436012731],
                [-89.84392762184143,39.72439389620628],
                [-89.83936786651611,39.725392361998416],
                [-89.83928203582764,39.71951688444436],
                [-89.84388470649719,39.71943436012731]
              ]
            ]
          ]
        },
        "type": "MERGED",
        "sources": []
      }
    ]]
    Args:
        user_id ([string]): [id do usuario associado a este campo]
        coordinates ([list]): [lista das coordenadas GeoJSON do MultiPolygon]
        threshold (float, optional): [limite de intersecção entre campos. Padrão é  0.01]

    Returns:
        [list]: [uma lista JSON dos campos]
    """

    get_fields_by_geometry_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/intersects'

    payload = {
        'geometry': {
            'type': "MultiPolygon",
            'coordinates': coordinates
        },
        'intersectionThreshold': threshold
    }

    get_fields_by_geometry = climate_fieldview_post(
        payload, get_fields_by_geometry_endpoint)

    return get_fields_by_geometry


def get_intersection_of_fields(user_id, fields_ids):
    """
     [ Retorna um GeoJSON MultiPolygon correspondente à intersecção dos campos especificados pelos id's fornecidos. Os id's dos campos vão estar em uma lista, no corpo da requisição.
      Exemplo de resposta JSON:
        {
            "type": "MultiPolygon",
            "coordinates": [
                [
                    [
                        [-89.84388470649719,39.71943436012731],
                        [-89.84392762184143,39.72439389620628],
                        [-89.83936786651611,39.725392361998416],
                        [-89.83928203582764,39.71951688444436],
                        [-89.84388470649719,39.71943436012731]
                    ]
                ]
            ]
        }]
      Args:
          user_id ([string]): [id do usuario associado a este campo]
          fields_ids ([list]): [lista de id's dos campos]
      Returns:
          [dict]: [GeoJSON MultiPolygon]
    """

    get_intersection_of_fields_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/intersect'
    payload = fields_ids

    intersection_of_fields = climate_fieldview_post(
        payload, get_intersection_of_fields_endpoint)

    return intersection_of_fields


def delete_field(user_id, field_id):
    """
    [Deleta um campo específico.]

    Args:
        user_id ([string]): [id do usuario associado a este campo]
        field_id ([string]): [id do campo requisitado]

    Returns:
        [dict]: [Resposta JSON de remoção de campo]]
    """
    delete_field_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/{field_id}'
    delete_field = climate_fieldview_delete(delete_field_endpoint)

    return delete_field


def get_all_boundaries_from_field(user_id, field_id):
    """
    [Retorna a lista de todos os limites de um campo]

    Args:
        user_id ([string]): [id de um usuário especpifico]
        field_id ([string]): [id de um campo requisitado]

    Returns:
      [list]: [lista de limites de um campo]
    """
    get_all_boundaries_from_field_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/{field_id}/boundaries'
    all_boundaries_from_field = climate_fieldview_get(
        get_all_boundaries_from_field_endpoint)

    return all_boundaries_from_field


def get_boundary_from_field(user_id, field_id, boundary_id):
    """
    [Retorna um limite específico de um campo]

    Args:
        user_id ([string]): [id de um usuário especpifico]
        field_id ([string]): [id de um campo requisitado]
        boundary_id ([string]): [id de um limite requisitado]

    Returns:
      [dict]: [limite de um campo como JSON]
    """
    get_boundary_from_field_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/{field_id}/boundaries/{boundary_id}'
    boundary_from_field = climate_fieldview_get(
        get_boundary_from_field_endpoint)

    return boundary_from_field


def get_active_boundary_from_field(user_id, field_id):
    """
    [Retorna um limite ativo de um campo]

    Args:
        user_id ([string]): [id de um usuário especpifico]
        field_id ([string]): [id de um campo requisitado]

    Returns:
      [dict]: [limite de um campo como JSON]
    """
    get_active_boundary_from_field_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/{field_id}/boundary'
    active_boundary_from_field = climate_fieldview_get(
        get_active_boundary_from_field_endpoint)

    return active_boundary_from_field


def udpate_active_boundary_from_field(user_id, field_id, coordinates):
    """
    [Atualiza o limite ativo de um campo. O limite anterior não é deletado, mas é definido como inativo.]

    Args:
        user_id ([string]): [id de um usuário especpifico]
        field_id ([string]): [id de um campo requisitado]
        coordinates ([list]): [lista de coordenadas GeoJSON]

    Returns:
        [dict]: [um campo como JSON]
    """
    update_active_boundary_from_field_endpoint = _field_boundaries_url + \
        f'users/{user_id}/fields/{field_id}/boundary'
    payload = {
        'geometry': {
            'type': "MultiPolygon",
            'coordinates': coordinates
        }
    }
    active_boundary_from_field = climate_fieldview_put(
        payload, update_active_boundary_from_field_endpoint)

    return active_boundary_from_field
