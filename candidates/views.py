from itertools import combinations
from rest_framework import viewsets
from candidates.models import Candidate
from candidates.serializers import CandidateSerializer

from django.db.models import Q, Value, F, Case, When, IntegerField, Sum, Count
from django.db.models.functions import Concat, Cast


class CandidateViewSet(viewsets.ModelViewSet):

    authentication_classes = []
    permission_classes = []

    serializer_class = CandidateSerializer

    def get_queryset(self):
        queryset = Candidate.objects.all()
        query = self.request.query_params.get('search', None)
        if query:
            search_terms = query.split()
            q_objects = Q()
            for term in search_terms:
                q_objects |= Q(name__icontains=term)
            # Filtering for search terms
            queryset = queryset.filter(q_objects)
            # Getting matching score for original search string
            queryset = queryset.annotate(
                sequence_match=Cast(Q(name__icontains=query), IntegerField())
            )
            # Getting matching score for each word in original search string
            queryset = queryset.annotate(
                total_relevancy=sum(
                    Cast(Q(name__icontains=term), IntegerField()) 
                    for term in search_terms
                )
            ).order_by('-sequence_match', '-total_relevancy', 'name')
        return queryset