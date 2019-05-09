from django.utils.translation import get_language_info,get_language


def locale(request):
    return {'LOCALE_LANG': get_language_info(get_language())['name_local']}

def locale(request):
    return {'LOCALE_LANG': get_language_info(get_language())['name_local']}
