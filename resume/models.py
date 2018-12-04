from django.db import models


class Resume(models.Model):

    SFL_BUREAUX=(
        ('M','Montréal'),
        ('Q','Québec')
    )

    title=models.CharField(
        max_length=50,
        verbose_name="Titre du CV"
    )
    description=models.TextField(
        verbose_name="Description du CV"
    )
    prenom_consultant=models.CharField(
        max_length=50,
        verbose_name="Prénom du consultant"
    )
    nom_consultant=models.CharField(
        max_length=50,
        verbose_name="Nom du consultant"
    )
    titre_consultant=models.CharField(
        max_length=50,
        verbose_name="Titre du consultant"
    )

    date_de_naissance=models.DateField(
        verbose_name="Date de naissance"
    )
    courriel=models.EmailField(
        verbose_name="Courriel"
    )
    bureau=models.CharField(
        max_length=2,
        choices=SFL_BUREAUX,
        verbose_name='Bureau',
        default="M"
    )
