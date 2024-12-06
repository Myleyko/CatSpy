from django.db import models

class SpyCat(models.Model):
    BREEDS = [
        ('Siberian', 'Siberian'),
        ('Bengal', 'Bengal'),
        ('Persian', 'Persian'),
        ('Maine Coon', 'Maine Coon'),
        ('Sphinx', 'Sphinx'),
    ]

    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=50, choices=BREEDS)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mission {self.id} (Complete: {self.complete})"

class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Target: {self.name} ({self.country})"


