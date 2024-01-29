# © Kyle Olson/Future Trick 2023
from django.urls import include, path

from . import views
from rest_framework import routers
"""from nfl.views import (AgentViewSet, ContractViewSet, ContractYearViewSet, TimeframeViewSet, TeamViewSet, StadiumViewSet, 
                       ScoreViewSet, ScheduleViewSet, TeamGameViewSet, TeamSeasonViewSet, StandingViewSet, PlayerDetailViewSet, 
                       InjuryViewSet, PlayerGameViewSet, PlayerSeasonViewSet, ScoringPlayViewSet, ScoringDetailViewSet, 
                       QuarterViewSet, PlayViewSet, PlayStatViewSet, DepthChartViewSet, TeamDepthChartViewSet,
                       PlayerSearchViewSet, NFLTeamContactInfoViewSet, NCAAFTeamContactInfoViewSet, 
                       NCAAFPlayerViewSet, NCAAFTeamViewSet, NCAAFPlayersViewSet, NCAAFTeamsViewSet,
                       ContactViewSet, SubContactViewSet, ContactTreeViewSet, SubContactTreeViewSet,
                       AddressViewSet, PhoneNumberViewSet, OtherDetailViewSet)
"""

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'agent', views.AgentViewSet)
# router.register(r'Contract', views.ContractViewSet)
# router.register(r'ContractYear', views.ContractYearViewSet)
# router.register(r'Timeframe', views.TimeframeViewSet)
# router.register(r'Team', views.TeamViewSet)
# router.register(r'Teams', views.TeamsViewSet)
# router.register(r'TeamHeader', views.TeamHeaderViewSet)
# router.register(r'NFLTeamContactInfo', views.NFLTeamContactInfoViewSet)
# router.register(r'NCAAFTeamContactInfo', views.NCAAFTeamContactInfoViewSet)
# router.register(r'NFLTeamContactInfos', views.NFLTeamContactInfosViewSet)
# router.register(r'NCAAFTeamContactInfos', views.NCAAFTeamContactInfosViewSet)
# router.register(r'Stadium', views.StadiumViewSet)
# router.register(r'Score', views.ScoreViewSet)
# router.register(r'Schedule', views.ScheduleViewSet)
# router.register(r'TeamGame', views.TeamGameViewSet)
# router.register(r'TeamSeason', views.TeamSeasonViewSet)
# router.register(r'Standing', views.StandingViewSet)
# router.register(r'PlayerDetail', views.PlayerDetailViewSet)
# router.register(r'PlayerHeader', views.PlayerHeaderViewSet)
# router.register(r'Injury', views.InjuryViewSet)
# router.register(r'PlayerGame', views.PlayerGameViewSet)
# router.register(r'PlayerSeason', views.PlayerSeasonViewSet)
# router.register(r'PlayerSeasons', views.PlayerSeasonsViewSet)
# router.register(r'ScoringPlay', views.ScoringPlayViewSet)
# router.register(r'ScoringDetail', views.ScoringDetailViewSet)
# router.register(r'Quarter', views.QuarterViewSet)
# router.register(r'Play', views.PlayViewSet)
# router.register(r'PlayStat', views.PlayStatViewSet)
# router.register(r'DepthChart', views.DepthChartViewSet)
# router.register(r'TeamDepthChart', views.TeamDepthChartViewSet)


# router.register(r'NCAAFPlayer', views.NCAAFPlayerViewSet)
# router.register(r'NCAAFTeam', views.NCAAFTeamViewSet)
# router.register(r'NCAAFPlayers', views.NCAAFPlayersViewSet)
# # router.register(r'NCAAFTeams', views.NCAAFTeamsViewSet)

# router.register(r'Contact', views.ContactViewSet)
# router.register(r'SubContact', views.SubContactViewSet)
# router.register(r'ContactTree', views.ContactTreeViewSet)
# router.register(r'SubContactTree', views.SubContactTreeViewSet)
# router.register(r'Address', views.AddressViewSet) 
# router.register(r'PhoneNumber', views.PhoneNumberViewSet)
# router.register(r'OtherDetail', views.OtherDetailViewSet)


router.register(r'PlayerPersonalContact', views.PlayerPersonalContactViewSet)
router.register(r'PlayerWorkContact', views.PlayerWorkContactViewSet)
router.register(r'PlayerCompanyContact', views.PlayerCompanyContactViewSet)
router.register(r'PlayerRepContact', views.PlayerRepresentativeContactViewSet)
router.register(r'PlayerFamilyContact', views.PlayerFamilyContactViewSet)
router.register(r'PlayerMerchDesigner', views.PlayerMerchDesignerViewSet)


# router.register(r'PlayerSearch', views.PlayerSearchViewSet)

router.register(r'PlayerInfo', views.PlayerInfoViewSet, basename='player-info')
router.register(r'PlayersList', views.NFLPlayersListViewSet, basename='nfl-players-list')

router.register(r'TeamsList',views.TeamListViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("nfl/", include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

