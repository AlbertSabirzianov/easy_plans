from django.urls import path

from documents import views

app_name = 'documents'


urlpatterns = [
    path('document/<int:plan_id>', views.DownloadDocumentView.as_view(), name='download'),
]
