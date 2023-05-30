from django.db import models

# Create your models here.
import os
# CRIANDO O  MODELO PARA O RECICLAQUI

class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class RECICLAQUIapp(Base):
    título = models.CharField(max_length=255)
    url = models.URLField(unique=True)


    class Meta:
        verbose_name = 'RECICLAQUI'
        verbose_name_plural = 'RECICLAQUI'


    def __str__(self):
        return self.título

# Criando a parte de avaliacao
class Avaliacao(Base):
    RECICLAQUI = models.ForeignKey(RECICLAQUIapp,
                               related_name='avaliacoes',
                               on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email','RECICLAQUI']

        def __str__(self):
            return f'{self.nome} avaliou o RECICLAQUI {self.RECICLAQUI} com a nota {self.avaliacao}'

class todo(models.Model):
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)

class teste(models.Model):
    ID = models.PositiveIntegerField()
    NOME = models.CharField(max_length=200)
    Endereco = models.CharField(max_length=200)
    Observacao= models.CharField(max_length=200)
    Subpref = models.CharField(max_length=200)
    Situacao = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()





'''     ecopontos = pd.read_csv("data/ecopontos.csv")

    for i, r in ecopontos.iterrows():
        # setting for the popup
        popup = folium.Popup(r['NOME'], max_width=1000)
        # Plotting the Marker for each stationsト
        folium.map.Marker(
            location=[r['latitude'], r['longitude']],
            popup=popup,
            icon=folium.Icon(color="green", icon="fa-solid fa-recycle", prefix='fa')
        ).add_to(map)'''