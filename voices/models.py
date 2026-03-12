from django.db import models

# Create your models here.

class Voice(models.Model):
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='voices/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    transcribe_status = models.CharField(
        max_length=20,
        default="pending" # pending/running/done/failed
        )
    def __str__(self):
        return self.title


class Segment(models.Model):
    voice = models.ForeignKey(Voice, on_delete=models.CASCADE, related_name='segments')
    start_time = models.FloatField()
    end_time = models.FloatField()
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.voice.title} [{self.start_time:.2f} - {self.end_time:.2f}]"