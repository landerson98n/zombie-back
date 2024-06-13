from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from base.models import Survivor, Item
from .serializers import SurvivorSerializer
from django.db.models import Avg, Sum

class SurvivorViewSet(viewsets.ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

    @action(detail=False, methods=['get'])
    def infection_stats(self, request):
        total_survivors = Survivor.objects.count()
        infected_count = Survivor.objects.filter(is_infected=True).count()
        non_infected_count = total_survivors - infected_count

        if total_survivors == 0:
            infected_percentage = 0
            non_infected_percentage = 0
        else:
            infected_percentage = (infected_count / total_survivors) * 100
            non_infected_percentage = (non_infected_count / total_survivors) * 100

        return Response({
            'infected_percentage': infected_percentage,
            'non_infected_percentage': non_infected_percentage
        })




