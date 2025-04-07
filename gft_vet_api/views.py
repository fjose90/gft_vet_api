from django.http import JsonResponse


def home(request):
    return JsonResponse({'msg': 'Bem vindo a API da Clínica Veterinária'})
