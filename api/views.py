# api/views.py

from rest_framework import generics, permissions, mixins
from .permissions import IsOwner
from .serializers import DocSerializer
from .models import docs
from rest_framework.response import Response
from django.db.models import Q
from django.db.models import Max,Aggregate
from rest_framework.permissions import IsAuthenticated

from api.Screening import get_docs_list




class DocView(generics.ListAPIView):

    """This class handles the GET and POSt requests of our rest api."""
    # permission_classes = (IsAuthenticated,)


    lookup_field            = 'id' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = DocSerializer

    def get_queryset(self):
        query = self.request.GET.get("id")
        qs = docs.objects.all()
        print (query)

        if query is not None:
            documents_scanned=get_docs_list(query)
            print (documents_scanned)

            for doc in documents_scanned:
                new_entry = docs(client_id=query,
                doc_name=doc[0],
                date_created=doc[1]
                
                )
                new_entry.save()

            qs = docs.objects.all().filter(
                    Q(client_id=query))
            # max_id = qs.aggregate(Max('id'))
            # qs = qs.filter(
            #     Q(id=max_id['id__max']))

        return qs
