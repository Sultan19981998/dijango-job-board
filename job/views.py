from audioop import reverse
from sys import modules

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .filters import JobFilter





def job_list(request):
    job_list=Job.objects.all()

    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs


    paginator = Paginator(job_list, 4)# Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page( page_number )

    return render( request, 'job_list.html', context={'jobs': page_obj , 'myfilter':myfilter} )


def job_detail(request,slug):
    job_list = Job.objects.filter(slug=slug).first()

    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_list
            myform.save()
            messages.success( request, "✅ تم إرسال طلبك بنجاح!" )
            return redirect( request.path )
    else:
        form=ApplyForm()

    return render( request, 'job_details.html', context={'detail_job': job_list,'form':form,} )

@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm( request.POST, request.FILES )
        if form.is_valid():
            myform = form.save( commit=False )
            myform.owner = request.user
            myform.save()
            messages.success( request, "✅ تم إرسال طلبك بنجاح!" )
            return redirect(reverse('jobs:add_job'))

    else:
        form=JobForm()

    return render(request, 'add_job.html', {'form': form})


