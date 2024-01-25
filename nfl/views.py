# © Kyle Olson/Future Trick 2023
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, filters, permissions
from nfl.serializers import (UserSerializer, GroupSerializer, AgentSerializer, ContractSerializer, ContractYearSerializer,
                                TimeframeSerializer, TeamSerializer, StadiumSerializer, ScoreSerializer, ScheduleSerializer,
                                TeamGameSerializer, TeamSeasonSerializer, StandingSerializer, PlayerDetailSerializer,
                                InjurySerializer, PlayerGameSerializer, PlayerSeasonSerializer, ScoringPlaySerializer,
                                ScoringDetailSerializer, QuarterSerializer, PlaySerializer, PlayStatSerializer,
                                DepthChartSerializer, TeamDepthChartSerializer, PlayerHeaderSerializer,
                                NFLTeamContactInfoSerializer, NCAAFTeamContactInfoSerializer, TeamHeaderSerializer,
                                TestTableSerializer,
                                ContactSerializer, ContactTreeSerializer, SubContactSerializer, SubContactTreeSerializer,
                                AddressSerializer, PhoneNumberSerializer, OtherDetailSerializer, NCAAFPlayerSerializer,
                                NCAAFTeamSerializer,PlayerPersonalContactSerializer, PlayerInfoSerializer,PlayerWorkContactSerializer,PlayerCompanyContactSerializer,PlayerRespresentativeContactSerializer,
                                PlayerFamilyContactSerializer, PlayerMerchDesignerSerializer, PlayerClubContactSerializer, NFLPlayersListSerializer,TeamListSerializer
                                ) 

from django.contrib.auth.models import User, Group
from nfl.models import (Agent, Contract, ContractYear, Timeframe, Team, Stadium, Score, Schedule, 
                        TeamGame, TeamSeason, Standing, PlayerDetail, Injury, PlayerGame, PlayerSeason, 
                        ScoringPlay, ScoringDetail, Quarter, Play, PlayStat, DepthChart, TeamDepthChart,
                        NFLTeamContactInfo, NCAAFTeamContactInfo, NCAAFPlayer, NCAAFTeam,
                        TestTable,
                        Contact, SubContact, Address, PhoneNumber, OtherDetail,
                        PlayerPersonalContact, PlayerWorkContact,PlayerCompanyContact, PlayerRespresentativeContact,PlayerFamilyContact,
                        PlayerMerchDesigner, PlayerClubContact
                        )
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse("Dagger Concept")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Agent to be viewed or edited.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contract to be viewed or edited.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContractYearViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ContractYear to be viewed or edited.
    """
    queryset = ContractYear.objects.all()
    serializer_class = ContractYearSerializer

class TimeframeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Timeframe to be viewed or edited.
    """
    queryset = Timeframe.objects.all()
    serializer_class = TimeframeSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def create(self, request, *args, **kwargs):
         data = request.data
         serializer = TeamSerializer(data=data, many=isinstance(data, list))
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return HttpResponse(serializer.data)

    
class TeamHeaderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamHeaderSerializer
    ordering = ['-Key']

class NFLTeamContactInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows NFLTeamContactInfo to be viewed or edited.
    """
    queryset = NFLTeamContactInfo.objects.all()
    serializer_class = NFLTeamContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class NFLTeamContactInfosViewSet(viewsets.ModelViewSet):
    queryset = NFLTeamContactInfo.objects.all()
    serializer_class = NFLTeamContactInfoSerializer

    def create(self, request, *args, **kwargs):
         data = request.data
         serializer = NFLTeamContactInfoSerializer(data=data, many=isinstance(data, list))
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return HttpResponse()

class NCAAFTeamContactInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows NCAAFTeamContactInfo to be viewed or edited.
    """
    queryset = NCAAFTeamContactInfo.objects.all()
    serializer_class = NCAAFTeamContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    
class NCAAFTeamContactInfosViewSet(viewsets.ModelViewSet):
    queryset = NCAAFTeamContactInfo.objects.all()
    serializer_class = NCAAFTeamContactInfoSerializer

    def create(self, request, *args, **kwargs):
         data = request.data
         serializer = NCAAFTeamContactInfoSerializer(data=data, many=isinstance(data, list))
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return HttpResponse(serializer.data)

    

class StadiumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Stadium to be viewed or edited.
    """
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [permissions.IsAuthenticated]

class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Score to be viewed or edited.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Schedule to be viewed or edited.
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TeamGame to be viewed or edited.
    """
    queryset = TeamGame.objects.all()
    serializer_class = TeamGameSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamSeasonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TeamSeason to be viewed or edited.
    """
    queryset = TeamSeason.objects.all()
    serializer_class = TeamSeasonSerializer
    permission_classes = [permissions.IsAuthenticated]

class StandingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Standing to be viewed or edited.
    """
    queryset = Standing.objects.all()
    serializer_class = StandingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlayerHeaderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlayerDetail to be viewed or edited.
    """
    queryset = PlayerDetail.objects.all()
    serializer_class = PlayerHeaderSerializer

class PlayerDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlayerDetail to be viewed or edited.
    """
    queryset = PlayerDetail.objects.all()
    serializer_class = PlayerDetailSerializer

class InjuryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Injury to be viewed or edited.
    """
    queryset = Injury.objects.all()
    serializer_class = InjurySerializer
    permission_classes = [permissions.IsAuthenticated]

class PlayerGameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlayerGame to be viewed or edited.
    """
    queryset = PlayerGame.objects.all()
    serializer_class = PlayerGameSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlayerSeasonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlayerSeason to be viewed or edited.
    """
    queryset = PlayerSeason.objects.all()
    serializer_class = PlayerSeasonSerializer





class PlayerSeasonsViewSet(viewsets.ModelViewSet):
    queryset = PlayerSeason.objects.all()
    serializer_class = PlayerSeasonSerializer

    def create(self, request, *args, **kwargs):
         data = request.data
         serializer = PlayerSeasonSerializer(data=data, many=isinstance(data, list))
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return HttpResponse(serializer.data)



class ScoringPlayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ScoringPlay to be viewed or edited.
    """
    queryset = ScoringPlay.objects.all()
    serializer_class = ScoringPlaySerializer
    permission_classes = [permissions.IsAuthenticated]

class ScoringDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ScoringDetail to be viewed or edited.
    """
    queryset = ScoringDetail.objects.all()
    serializer_class = ScoringDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuarterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Quarter to be viewed or edited.
    """
    queryset = Quarter.objects.all()
    serializer_class = QuarterSerializer()
    permission_classes = [permissions.IsAuthenticated]

class PlayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Play to be viewed or edited.
    """
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
    permission_classes = [permissions.IsAuthenticated]

class PlayStatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlayStat to be viewed or edited.
    """
    queryset = PlayStat.objects.all()
    serializer_class = PlayStatSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepthChartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DepthChart to be viewed or edited.
    """
    queryset = DepthChart.objects.all()
    serializer_class = DepthChartSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamDepthChartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TeamDepthChart to be viewed or edited.
    """
    queryset = TeamDepthChart.objects.all()
    serializer_class = TeamDepthChartSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlayerSearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlayerDetail to be viewed or edited.
    """
    queryset = PlayerDetail.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['Name']

    serializer_class = PlayerHeaderSerializer

class TestTableViewSet(viewsets.ModelViewSet):
    """
    API endpoint for a test table.
    """
    queryset = TestTable.objects.all()
    serializer_class = TestTableSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contact to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Category', 'Owner']
    

class SubContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SubContact to be viewed or edited.
    """
    queryset = SubContact.objects.all()
    serializer_class = SubContactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Contact']

class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Address to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PhoneNumberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PhoneNumber to be viewed or edited.
    """
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer

class OtherDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OtherDetail to be viewed or edited.
    """
    queryset = OtherDetail.objects.all()
    serializer_class = OtherDetailSerializer

class ContactTreeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contact Objects to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactTreeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Category', 'Owner', 'DataID']

class SubContactTreeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SubContact Objects to be viewed or edited.
    """
    queryset = SubContact.objects.all()
    serializer_class = SubContactTreeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Contact']

class NCAAFPlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OtherDetail to be viewed or edited.
    """
    queryset = NCAAFPlayer.objects.all()
    serializer_class = NCAAFPlayerSerializer

class NCAAFPlayersViewSet(viewsets.ModelViewSet):
    queryset = NCAAFPlayer.objects.all()
    serializer_class = NCAAFPlayerSerializer

    def create(self, request, *args, **kwargs):
         data = request.data
         serializer = NCAAFPlayerSerializer(data=data, many=isinstance(data, list))
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return HttpResponse(serializer.data)


    
class NCAAFTeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OtherDetail to be viewed or edited.
    """
    queryset = NCAAFTeam.objects.all()
    serializer_class = NCAAFTeamSerializer
    
    
    
    
class PlayerPersonalContactViewSet(viewsets.ModelViewSet):
    
    http_method_names = ['get']
        
    queryset = PlayerPersonalContact.objects.all()
    serializer_class = PlayerPersonalContactSerializer
    
    permission_classes = [permissions.AllowAny]

    
class PlayerCompanyContactViewSet(viewsets.ModelViewSet):
    
    http_method_names = ['get', 'post', 'put', 'delete']

    queryset = PlayerCompanyContact.objects.all()
    serializer_class = PlayerCompanyContactSerializer
    
class PlayerRepresentativeContactViewSet(viewsets.ModelViewSet):
    
    http_method_names = ['get', 'post', 'put', 'delete']
    
    queryset = PlayerRespresentativeContact.objects.all()
    serializer_class = PlayerRespresentativeContactSerializer
class PlayerClubContactViewSet(viewsets.ModelViewSet):
    
    http_method_names = ['get', 'post', 'put', 'delete']
    
    queryset = PlayerClubContact.objects.all()
    serializer_class = PlayerClubContactSerializer
    
class PlayerMerchDesignerViewSet(viewsets.ModelViewSet):
    
    http_method_names = ['get', 'post', 'put', 'delete']
    
    queryset = PlayerMerchDesigner.objects.all()
    serializer_class = PlayerMerchDesignerSerializer
    
class PlayerFamilyContactViewSet(viewsets.ModelViewSet):
    
    http_method_names = ['get', 'post', 'put', 'delete']
    
    queryset = PlayerFamilyContact.objects.all()
    serializer_class = PlayerFamilyContactSerializer
    
class PlayerWorkContactViewSet(viewsets.ModelViewSet):
    
    http_method_names = ['get', 'post', 'put', 'delete']
    
    queryset = PlayerWorkContact.objects.all()
    serializer_class = PlayerWorkContactSerializer

    # def create(self, request, *args, **kwargs):
    #     player_id = request.data.get('PlayerID')

    #     # Check if a PlayerWorkContact already exists for the given PlayerID
    #     existing_contact = PlayerWorkContact.objects.filter(PlayerID=player_id).first()

    #     if existing_contact:
    #         return Response({"detail": "PlayerWorkContact for this PlayerID already exists."}, status=status.HTTP_400_BAD_REQUEST)

    #     return super().create(request, *args, **kwargs)

class PlayerInfoViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = PlayerDetail.objects.all()
    serializer_class = PlayerInfoSerializer
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Fetch TeamName
        team_name = self.get_serializer(instance).get_TeamName(instance)
        data['TeamName'] = team_name

        # Fetch Stadium details based on StadiumID associated with the Team
        stadium = self.get_serializer(instance).get_Stadium(instance)
        data['Stadium'] = stadium

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()



        personal_contact_queryset = PlayerPersonalContact.objects.filter(PlayerID=instance)
        work_contact_queryset = PlayerWorkContact.objects.filter(PlayerID=instance)
        company_contact_queryset = PlayerCompanyContact.objects.filter(PlayerID=instance)
        rep_contact_queryset = PlayerRespresentativeContact.objects.filter(PlayerID=instance)
        family_contact_queryset = PlayerFamilyContact.objects.filter(PlayerID=instance)
        merch_designer_queryset = PlayerMerchDesigner.objects.filter(PlayerID=instance)
        club_contact_queryset = PlayerClubContact.objects.filter(PlayerID=instance)

        serializer = self.get_serializer(instance)
        data = serializer.data

        if personal_contact_queryset.exists():
            personal_contact_serializer = PlayerPersonalContactSerializer(personal_contact_queryset, many=True)
            data[1] = personal_contact_serializer.data

        if work_contact_queryset.exists():
            work_contact_serializer = PlayerWorkContactSerializer(work_contact_queryset, many=True)
            data['PlayerWorkContact'] = work_contact_serializer.data

        if company_contact_queryset.exists():
            company_contact_serializer = PlayerCompanyContactSerializer(company_contact_queryset, many=True)
            data['PlayerCompanyContact'] = company_contact_serializer.data

        if rep_contact_queryset.exists():
            rep_contact_serializer = PlayerRespresentativeContactSerializer(rep_contact_queryset, many=True)
            data['playerRepContact'] = rep_contact_serializer.data

        if family_contact_queryset.exists():
            family_contact_serializer = PlayerFamilyContactSerializer(family_contact_queryset, many=True)
            data['playerFamilyContact'] = family_contact_serializer.data
            
        if merch_designer_queryset.exists():
            merch_designer_serializer = PlayerMerchDesignerSerializer(merch_designer_queryset, many=True)
            data['playerMerchDesigner'] = merch_designer_serializer.data
            
        if club_contact_queryset.exists():
            club_contact_serializer = PlayerClubContactSerializer(club_contact_queryset, many=True)
            data['playerClubContact'] = club_contact_serializer.data

       
        
        return Response(data)
    
class NCAAFTeamsViewSet(viewsets.ModelViewSet):
    queryset = NCAAFTeam.objects.all()
    serializer_class = NCAAFTeamSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = NCAAFTeamSerializer(data=data, many=isinstance(data, list))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(serializer.data)

class NFLPlayersListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PlayerDetail to be viewed.
    """
    queryset = PlayerDetail.objects.all()
    serializer_class = NFLPlayersListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        

        # Add the team_fullname to the response data
        response_data = {'Team': instance.get_TeamName(),'State':instance.get_State(),'ContractDate': instance.get_contract_date, **serializer.data}

        return Response(response_data)
    
class TeamListViewSet(viewsets.ModelViewSet):
    queryset=NFLTeamContactInfo.objects.all()
    serializer_class = TeamListSerializer