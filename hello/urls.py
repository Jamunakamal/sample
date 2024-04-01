from django.urls import path
from . import views

urlpatterns = [
    path("hello/",views.avgsamp1, name="samp1"),
    path("index/",views.index, name="samp2"),
    path("index.html",views.index, name="samp2"),
    path("index",views.index, name="samp2"),
    path("sample3/",views.square, name="samp17"),
    path("login/",views.login, name="samp16"),
    path("signup/",views.register, name="samp18"),
    path("index1/",views.index_1, name="samp3"),
    path("member/",views.member, name="samp4"),
    path("add/",views.add_member, name="samp5"),
    path("event/",views.event, name="samp6"),
    path("left/",views.left, name="samp7"),
    path("noside/",views.no_side, name="samp8"),
    path("report/",views.report, name="samp9"),
    path("right/",views.right, name="samp10"),
    path("two/",views.two, name="samp11"),
    path("jinja/",views.jinja, name="samp13"),
    path("square/",views.square2, name="samp14"),
    path("image/",views.image, name="samp15"),

    
   
]