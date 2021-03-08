from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import File
from .forms import FilesUploadForm


# Create your views here.
@login_required()
def index(request):
    files = File.objects.all().filter(user_id=request.user.id)
    return render(request, 'files/index.html', {'files': files})


@login_required()
def upload(request):
    if request.method == "POST":
        form = FilesUploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                file_instance = File(file=f, user_id=request.user.id)
                file_instance.save()
    else:
        form = FilesUploadForm()
    return render(request, 'files/upload.html', {'form': form})
