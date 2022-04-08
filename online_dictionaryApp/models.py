from django.db import models


class DictionaryDB(models.Model):
    alphabet=models.CharField(max_length=1)
    word=models.CharField(max_length=30)
    definition=models.CharField(max_length=300)
    example=models.CharField(max_length=300)


    def __str__(self):
        return "{} {} {} {}".format(self.alphabet,self.word, self.definition, self.example)
