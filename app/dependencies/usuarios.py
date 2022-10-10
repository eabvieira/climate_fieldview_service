from app.core.services import climate_fieldview_get, climate_fieldview_post, climate_fieldview_put, climate_fieldview_delete

_user_management_url = 'usermanagement/api/users/'


async def users_list():
    """[retorna todos os usuários]

    Returns:
        [list]: [returns a list of all users]
    """
    users_list = await climate_fieldview_get(f'{_user_management_url}')

    return users_list


async def user(user_id):
    """[retorna um usuário específico]

    Args:
        user_id ([string]): [deve conter o id do usuário requisitado.]

    Returns:
        [dict]: [retorna as informações do usuário]
    """
    user = await climate_fieldview_get(f'{_user_management_url}{user_id}')

    return user


def new_user(payload):
    """[Cria um novo usuário. Um payload deve ser enviado contendo as informações a serem setadas.]

    Args:
        payload ([dict]): [deve conter todas as informações a serem setadas.]

    Returns:
        [dict]: [retorna um novo usuário]
    """
    payload = {
        "name": payload.name,
        "email": payload.email,
        "phone": payload.phone,
        "address": payload.address
    }
    return climate_fieldview_post(payload, '{_user_management_url}')


def update_user(payload, user_id):
    """[Atualiza as informações de um usuário. Um payload deve ser enviado contendo as informações a serem setadas.]

    Args:
        payload ([dict]): [deve conter todas as informações a serem setadas.]
        user_id ([String]): [deve conter o id do usuário requisitado.]

    Returns:
        [dict]: [retorna as informações do usuário]
    """
    payload = {
        "name": payload.name,
        "email": payload.email,
        "phone": payload.phone,
        "address": payload.address
    }
    return climate_fieldview_put(payload, '{_user_management_url}', user_id)


def delete_user(id):
    """[deleta um usuário específico]

    Args:
        id ([string]): [deve conter o id do usuário requisitado.]

    """
    return climate_fieldview_delete(f'{_user_management_url}', id)
