# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('savereg/', views.save_registration, name='savereg'),
    path('comlog/', views.com_log, name='comlog'),
    
    path('profile/',views.profile_view, name='profile'),
    path('insert/', views.insert1, name= 'insert'),
    path('showall/', views.showall_view, name= 'showall'),
    path('search/', views.search_view, name= 'search'),
    path('showonetofive/searchdetail/<int:id>', views.searchdetails_view, name= 'searchdetail'),
    path('update/', views.update_view, name= 'update'),
    path('update/updateresult/<int:id>', views.update_result, name= 'updateresult'),
    path('delete/', views.delete_view, name= 'delete'),

    # path('savedata/',views.save_data, name = 'savedata'),
    
    path('onetofive/', views.onetofive_view, name= 'onetofive'),
    path('sixtoten/', views.sixtoten_view, name= 'sixtoten'),
    path('eleven_twelve/', views.eleven_twelve_view, name= 'eleven_twelve'),
    
    path('Mathscience/', views.Mathscience_view, name= 'Mathscience'),
    path('Biology/', views.Biology_view, name= 'Biology'),
    path('Commerce/', views.Commerce_view, name= 'Commerce'),
    path('Arts/', views.Arts_view, name= 'Arts'),
    path('Agriculture/', views.Agriculture_view, name= 'Agriculture'),


    path('Computerscience/', views.Computerscience_view, name= 'Computerscience'),
    path('Informationtechnology/', views.Informationtechnology_view, name= 'Informationtechnology'),
    path('Mechenical/', views.Mechenical_view, name= 'Mechenical'),
    path('Civil/', views.Civil_view, name= 'Civil'),
    path('Electronic/', views.Electronic_view, name= 'Electronic'),

    path('BCominAccountancy/', views.BCominAccountancy_view, name= 'BCominAccountancy'),
    path('BCominBankingandFinance/', views.BCominBankingandFinance_view, name= 'BCominBankingandFinance'),
    path('CominBusinessAdministration/', views.CominBusinessAdministration_view, name= 'CominBusinessAdministration'),
    path('BCominE_Commerce/', views.BCominE_Commerce_view, name= 'BCominE_Commerce'),
    path('BCominFinance/', views.BCominFinance_view, name= 'BCominFinance'),

    
    path('BScComputerscience/', views.BScComputerscience_view, name= 'BScComputerscience'),
    path('BScInformationtechnology/', views.BScInformationtechnology_view, name= 'BScInformationtechnology'),
    path('BScPhysics/', views.BScPhysics_view, name= 'BScPhysics'),
    path('BScNursing/', views.BScNursing_view, name= 'BScNursing'),
    path('BScAgriculture/', views.BScAgriculture_view, name= 'BScAgriculture'),
    

    path('showonetofive/', views.showonetofive_view, name= 'showonetofive'),
    path('showsixtoten/', views.showsixtoten_view, name= 'showsixtoten'),
]
