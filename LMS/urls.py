from django.conf.urls import url
from django.contrib import admin
from core import views
#from django.urls import path << usar no windows

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', views.index, name ='index'),
    url('cadastro-disciplina/', views.cadastro_disciplina, name = "cadastro_disciplina"),
    url('cursos/', views.cursos, name="cursos"),
    url('novo-curso/', views.novocurso, name = "novocurso"),
    url('cadastro-aluno/', views.cadastro_aluno, name ="cadastro_aluno"),
    url('cursos/grade-ads/', views.grade_ads, name="grade_ads"),
    url('cursos/grade-redes/',views.grade_redes, name="grade_redes"),
    url('cursos/grade-bd/', views.grade_bd, name = "grade_bd"),
    url('cursos/desc-ads/', views.desc_ads, name = "cursos/desc_ads"),
    url('cursos/desc-bd/', views.desc_bd, name= "cursos/desc_bd"),
    url('cursos/desc-redes/', views.desc_redes, name = "cursos/desc_redes"),
    url('cursos/desc-bd-lp/', views.desc_bd_lp, name = "cursos/desc_bd_lp"),
    url('cursos/desc-bd-fbd/', views.desc_bd_fbd, name ="cursos/desc_bd_fbd"),
    url('cursos/desc-bd-dba/', views.desc_bd_dba, name ="desc_bd_dba"),
    url('cursos/desc-ads/grade-ads/', views.grade_ads, name="grade_ads"),
    url('cursos/desc-ads/grade-bd/', views.grade_bd, name="grade_bd"),
    url('cursos/desc-ads/grade-redes/', views.grade_redes, name="grade_redes"),
    url('login/', views.login, name = "login"),
    url('tabela-aluno/', views.tabela_aluno, name = "tabela_aluno"),  
    url('cadastro-disciplina', views.cadastro_disciplina, name="cadastro_disciplina"),
]