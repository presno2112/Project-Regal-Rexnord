from django.db import models


class Game(models.Model):
    game_number = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=75, null=True)
    number = models.IntegerField(default=0)


    @property
    def leaderboard(self):
        results = self.results.order_by("-time").all()
        return results

# score, time, nombre usuario, booleano
