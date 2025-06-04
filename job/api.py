from rest_framework import generics
from rest_framework.response import Response
from .models import Job
from .serializer import JobSerializer
from rest_framework.decorators import api_view



@api_view(['GET'])
def job_list_api(request):
    all_jobs=Job.objects.all()
    data=JobSerializer(all_jobs, many=True).data

    return Response({'data':data})

@api_view(['GET', 'POST'])
def job_details_api(request,id):
    job_details = Job.objects.get(id=id)
    data = JobSerializer( job_details ).data
    return Response( {'data': data} )



class JobListapi(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer



class JobDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class=JobSerializer
    lookup_field='id'





