from django.db import models



class Todo(models.Model):
    """Basic todo model"""
    title = models.CharField(max_length=80, blank=False, help_text="Todo title")
    body = models.TextField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

