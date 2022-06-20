import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Jaime
# Create your views here.


class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            users = list(Jaime.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
                datos = {'message': "Succes", 'user': user}
            else:
                datos = {'message': "user not found..."}
            return JsonResponse(datos)
        else:
            users = list(Jaime.objects.values())
            if len(users) > 0:
                datos = {'message': "Succes", 'user': user}
            else:
                datos = {'message': "user not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Jaime.objects.create(
            nombre=jd['nombre'],
            apellido=jd['apellido'],
            edad=jd['edad'],
            sexo=jd['sexo'],
            telefono=jd['telefono'],
            direccion=jd['direccion'],)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(Jaime.objects.filter(id=id).values())
        if len(users) > 0:
            user = Jaime.objects.get(id=id)
            user.nombre = jd['nombre']
            user.apellido = jd['apellido']
            user.edad = jd['edad']
            user.sexo = jd['sexo']
            user.telefono = jd['telefono']
            user.direccion = jd['direccion']
            user.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "user not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        users = list(Jaime.objects.filter(id=id).values())
        if len(users) > 0:
            Jaime.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "user not found..."}
        return JsonResponse(datos)
