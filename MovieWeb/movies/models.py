from django.db import models
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_img')
    rating = models.FloatField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    trailer = models.FileField(upload_to='movie_trailer')
    video = models.FileField(upload_to='movie_video')


    def get_video_duration(self):
        
        video_path = self.video.path

        try:
            
            video_clip = VideoFileClip(video_path)

            
            duration_seconds = video_clip.duration

            
            video_clip.close()

            
            duration_timedelta = timedelta(seconds=duration_seconds)

            
            hours, remainder = divmod(duration_timedelta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            return f"{hours} hours, {minutes} minutes, {seconds} Second"

        except Exception as e:
            
            print(f"Error in getting video duration: {str(e)}")
            return None



    def __str__(self):
        
        return f"{self.name}, time: {self.get_video_duration()}"

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    
    

    def __str__(self):
        return self.name
    