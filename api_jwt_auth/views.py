from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.models import TokenUser
import os

# Create your views here.
class CreateDocument(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):
        nome = request.data.get('nome', None)
        data = request.data.get('data', None)
        cpf = request.data.get('cpf', None)
        rg = request.data.get('rg', None)
        ip = request.META.get('REMOTE_ADDR')
        username = str(request.user)

        if nome == None or data == None or cpf == None or rg == None:
            error_message = "Invalid parameters"
            print(error_message)
            return Response(data=error_message, status=status.HTTP_400_BAD_REQUEST)
        
        print('Nome: ' + nome + ', Data Nascimento: ' + data + ', CPF: ' + cpf + ' e RG: '+ rg)
        response_message = "Document writed: " + writeFile(nome,data,cpf,rg,username,ip)

        return Response(data=response_message,status=status.HTTP_200_OK)

def writeFile(nome,data,cpf,rg,username,ip):
    fileName = 'cadastro.txt'
    f = open(fileName, "w")
    f.write('Nome Completo: ' + nome)
    f.write('\n')
    f.write('Data de Nascimento: ' + data)
    f.write('\n')
    f.write('CPF: ' + cpf)
    f.write('\n')
    f.write('RG: ' + rg)
    f.write('\n\n')
    f.write('Usuario Autenticado\n')
    f.write('Login: ' + str(username))
    f.write('\n')
    f.write('IP: ' + ip)
    f.write('\n')
    f.close()
    return os.getcwd() + '/' + fileName