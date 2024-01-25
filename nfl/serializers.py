# © Kyle Olson/Future Trick 2023
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from nfl.models import (Agent, Contract, ContractYear, Timeframe, Team, Stadium, Score, Schedule, TeamGame, 
                        TeamSeason, Standing, PlayerDetail, Injury, PlayerGame, PlayerSeason, ScoringPlay, ScoringDetail, 
                        Quarter, Play, PlayStat, DepthChart, TeamDepthChart, NFLTeamContactInfo, NCAAFTeamContactInfo,
                        TestTable, Contact, SubContact, Address, OtherDetail, PhoneNumber, NCAAFPlayer, NCAAFTeam,
                        PlayerPersonalContact, PlayerWorkContact, PlayerRespresentativeContact, PlayerMerchDesigner, PlayerCompanyContact, PlayerFamilyContact,
                        PlayerMerchDesigner, PlayerClubContact
                        )

from django.db import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

#Data Model Fields

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class ContractYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractYear
        fields = '__all__'

class TimeframeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeframe
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

        
class TeamHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['Key', 'TeamID', 'PlayerID', 'City', 'Name', 'FullName', 'Conference', 'Division', 'WikipediaLogoUrl', 'WikipediaWordMarkUrl']

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['GameKey', 'SeasonType', 'Season', 'Week', 'Date', 'AwayTeam', 'HomeTeam', 'Channel', 'PointSpread', 
                  'OverUnder', 'StadiumID', 'Canceled', 'GeoLat', 'GeoLong', 'ForecastTempLow', 'ForecastTempHigh', 
                  'ForecastDescription', 'ForecastWindChill', 'ForecastWindSpeed', 'AwayTeamMoneyLine', 'HomeTeamMoneyLine', 
                  'Day', 'DateTime', 'GlobalGameID', 'GlobalAwayTeamID', 'GlobalHomeTeamID', 'ScoreID', 'StadiumDetails', 
                  'Status', 'IsClosed']

class TeamGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamGame
        fields = '__all__'
class TeamSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSeason
        fields = '__all__'
class StandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standing
        fields = '__all__'
class PlayerHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerDetail
        fields = ['Name', 'PlayerID', 'Team', 'Number', 'Position', 'FirstName', 'LastName', 'Status', 'PhotoUrl']
        

class PlayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerDetail
        fields = '__all__'

class InjurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Injury
        fields = '__all__'

class PlayerGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerGame
        fields = '__all__'

class PlayerSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSeason
        fields = '__all__'
        
class ScoringPlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringPlay
        fields = '__all__'
        
class ScoringDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringDetail
        fields = '__all__'
        
class QuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarter
        fields = '__all__'
        
class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ['PlayID', 'QuarterID', 'QuarterName', 'Sequence', 'TimeRemainingMinutes', 'TimeRemainingSeconds', 'PlayTime', 'Updated', 'Created', 'Team', 'Opponent', 'Down', 'Distance', 'YardLine', 'YardLineTerritory', 'YardsToEndZone', 'Type', 'YardsGained', 'Description', 'IsScoringPlay', 'ScoringPlay']

class PlayStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayStat
        fields = '__all__'
        
class DepthChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepthChart
        fields = '__all__'
        
class TeamDepthChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamDepthChart
        fields = '__all__'
        
class NFLTeamContactInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = NFLTeamContactInfo
        fields = '__all__'
        
class NCAAFTeamContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NCAAFTeamContactInfo
        fields = '__all__'

class TestTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTable
        fields = '__all__'



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'

class OtherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDetail
        fields = '__all__'


class SubContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContact
        fields = '__all__'

class SubContactTreeSerializer(serializers.ModelSerializer):
    Addresses  = AddressSerializer(many=True, read_only=True)
    PhoneNumbers  = PhoneNumberSerializer(many=True, read_only=True)
    OtherDetails  = OtherDetailSerializer(many=True, read_only=True)
    class Meta:
        model = SubContact
        fields = ['id', 'Contact', 'Primary', 'Name', 'Description', 'Addresses', 'PhoneNumbers', 'OtherDetails']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactTreeSerializer(serializers.ModelSerializer):
    SubContacts  = SubContactTreeSerializer(many=True, read_only=True)
    class Meta:
        model = Contact
        fields = ['id', 'Name', 'Description', 'Private', 'DataID', 'Owner', 'SubContacts']

class NCAAFPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NCAAFPlayer
        fields = '__all__'

class NCAAFTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
class PlayerPersonalContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPersonalContact
        fields = '__all__'

class PlayerWorkContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerWorkContact
        fields = '__all__'

class PlayerCompanyContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerCompanyContact
        fields = '__all__'
        
class PlayerRespresentativeContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerRespresentativeContact
        fields = '__all__'
        
class PlayerClubContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerClubContact
        fields = '__all__'
        
class PlayerFamilyContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerFamilyContact
        fields = '__all__'
        
class PlayerMerchDesignerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayerMerchDesigner
        fields = '__all__'
        
# class PlayerMerchDesignerSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = PlayerPersonalContact
#         fields = '__all__'

class PlayerInfoSerializer(serializers.ModelSerializer):
   
    TeamName = serializers.SerializerMethodField()
    Stadium = serializers.SerializerMethodField(method_name='get_Stadium')
    PFF = serializers.FloatField(default=67.2)
    class Meta:
        model = PlayerDetail
        fields = ['PlayerID', 'Name', 'TeamName', 'Number', 'Position', 'PFF','CurrentStatus', 'Height', 'Weight', 'Experience', 'PhotoUrl', 'BirthDate', 'CurrentStatus', 'College', 'CollegeDraftYear', 'IsUndraftedFreeAgent', 'Stadium']

    def get_TeamName(self, obj):
        # Get the team abbreviation from the player detail object
        team_abbr = obj.Team
        # Get the full name of the team from the Team model
        try:
            team = Team.objects.get(Key=team_abbr)
            return team.FullName
        except Team.DoesNotExist:
            return None
        
    def get_Stadium(self, obj):
        team_abbr = obj.Team
        try:
            team = Team.objects.get(Key=team_abbr)
            stadium_id = team.StadiumID
            
            stadium = Stadium.objects.get(StadiumID=stadium_id)
            stadium_serializer = StadiumSerializer(stadium)
            return {'Name': stadium.Name, 'City': stadium.City, 'State' : stadium.State, 'Country' : stadium.Country, 'Phone' : '6351728452'}
        except (Team.DoesNotExist, Stadium.DoesNotExist):
            return None

class NFLPlayersListSerializer(serializers.ModelSerializer):
    # Add new fields to include the full name of the team, the league, and contract date
    Team = serializers.SerializerMethodField()
    State = serializers.SerializerMethodField()
    League = serializers.CharField(default='NFL')
    # State = serializers.SerializerMethodField()
    Agency = serializers.CharField(default='')
    Agent = serializers.CharField(default='')
    ContractDate = serializers.SerializerMethodField()

    class Meta:
        model = PlayerDetail
        fields = ['FirstName', 'LastName', 'Status', 'Position', 'Team','League','State','Agency','Agent','ContractDate']

    def get_Team(self, obj):
        # Get the team abbreviation from the player detail object
        team_abbr = obj.Team

        # Get the full name of the team from the Team model
        try:
            team = NFLTeamContactInfo.objects.get(Key=team_abbr)
            return team.Name 
        except NFLTeamContactInfo.DoesNotExist:
            return None
        
    def get_State(self, obj):
        # Get the team abbreviation from the player detail object
        team_abbr = obj.Team

        # Get the full name of the team from the Team model
        try:
            team = NFLTeamContactInfo.objects.get(Key=team_abbr)
            return team.State
        except NFLTeamContactInfo.DoesNotExist:
            return None

    def get_ContractDate(self, obj):
        contracts = Contract.objects.filter(PlayerId=obj.PlayerID).order_by('-ContractDate')

        if contracts.exists():
            # Return the contract date of the latest contract
            return contracts.first().ContractDate
        else:
            return None

    def to_representation(self, instance):
        # Call the parent to_representation method
        data = super().to_representation(instance)

        # Add the 'league' field with the value 'NFL'
        data['League'] = 'NFL'

        return data

class TeamListSerializer(serializers.ModelSerializer):

     League = serializers.CharField(default='NFL')
     class Meta:
        model = NFLTeamContactInfo
        fields = ['Name','Mascot','League','State']

        