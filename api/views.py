# api/views.py

from rest_framework import generics, permissions, mixins
from .permissions import IsOwner
from .serializers import DocSerializer
from .models import docs
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import Max,Aggregate
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from api.Screening import get_docs_list


class DocView(generics.ListAPIView):

    """This class handles the GET and POSt requests of our rest api."""
    # permission_classes = (IsAuthenticated,)


    lookup_field            = 'id' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = DocSerializer

    def get_queryset(self):
        query = self.request.GET.get("id")
        qs = docs.objects.all()

        if query is not None:
            documents_scanned=get_docs_list(query)
            request_date=datetime.now().timestamp()
            print(request_date)
            print (documents_scanned)

            for doc in documents_scanned:
                new_entry = docs(
                client_id=query,
                doc_name=doc[0],
                date_created=doc[1],
                screen_vs=request_date
                )
                new_entry.save()

            qs = docs.objects.all().filter(
                    Q(client_id=query),
                    Q(screen_vs=request_date)
                    )
        return qs
