import imp
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Postes
from .serializers import PostSerializers
from rest_framework.decorators import api_view
from datetime import datetime
import json

today = datetime.now()

@api_view(['DELETE'])
def delete_post(request,id):
        isFound = False
        body = json.loads(json.dumps(request.data))
        singleposte = Postes.objects.all()
        singleposte = PostSerializers(singleposte,many=True)

        for data in singleposte.data:
            if data['id']==id:
                    isFound = True
        if isFound:
            s=Postes.objects.get(id=id)
            s.delete()
            return Response({'status':True , 'msg':'Ce post a été supprimé avec succès....'})


        else:
            return Response({'status':True , 'msg':'Ce post n\'existe pas....'})