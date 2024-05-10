from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, FileResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from documents.document_creater import DocumentMaker
from plans.models import Plan


class DownloadDocumentView(LoginRequiredMixin, View):

    def get_plan(self) -> Plan:
        plan = get_object_or_404(Plan, pk=self.kwargs.get('plan_id'))
        return plan

    def has_permission(self) -> bool:
        plan = self.get_plan()
        return plan.student.work_place.user == self.request.user

    def get(self, *args, **kwargs):
        plan = self.get_plan()
        if not self.has_permission():
            return HttpResponseForbidden("Нет прав")
        document_maker = DocumentMaker(plan=plan)
        stream = document_maker.get_document_stream()
        document_maker.document.save('test.docx')
        stream.seek(0)
        return FileResponse(
            stream,
            as_attachment=True,
            filename=plan.student.full_name + '.docx'
        )

