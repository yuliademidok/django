from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Menu(models.Model):
    menu_label = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.pk}: {self.menu_label}"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, blank=False, null=False, on_delete=models.CASCADE, related_name="links")
    title = models.CharField(max_length=32, null=False, blank=False)
    url = models.CharField(max_length=2048, null=False, blank=False)
    icon = models.ImageField(null=True, blank=True, upload_to="menu_images")
    priority = models.SmallIntegerField(validators=[MinValueValidator(-100), MaxValueValidator(100)], default=0)

    class Meta:
        indexes = [
            models.Index(fields=["url", "menu"]),
            models.Index(fields=["menu"]),
        ]
        unique_together = [("menu", "title"), ]

    def __str__(self):
        return f"{self.pk}: {self.title}"
