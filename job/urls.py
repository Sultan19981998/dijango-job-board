from django.urls import path, include

from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path( '', views.job_list, name='job_list' ),
    path( 'add', views.add_job, name='add_job' ),
    path( '<str:slug>', views.job_detail, name='job_details' ),
    path( 'api/list', api.job_list_api, name='job_list_api' ),
    path( 'api/list/<int:id>', api.job_details_api, name='job_details_api' ),


    path( 'api/v2/list/', api.JobListapi.as_view(), name='Job_List_api' ),
    path( 'api/v2/list/<int:id>', api.JobDetails.as_view(), name='JobDetails' ),


]
