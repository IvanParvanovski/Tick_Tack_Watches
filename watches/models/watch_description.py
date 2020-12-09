from django.db import models

from watches.models.watch import Watch


class WatchDescription(models.Model):
    YES_NO_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    CASE_SHAPE_CHOICES = (
        ('circle', 'Circle'),
        ('square', 'Square'),
        ('rectangle', 'Rectangle'),
        ('triangle', 'Triangle'),
        ('other', 'Other'),
    )

    COLOUR_CHOICES = (
        ('black', 'Black'),
        ('white', 'White'),
        ('gray', 'Gray'),
        ('silver', 'Silver'),
        ('maroon', 'Maroon'),
        ('red', 'Red'),
        ('rose_gold', 'Rose Gold'),
        ('other', 'Other'),
    )

    ANALOGUE_OR_DIGITAL = (
        ('analogue', 'Analogue'),
        ('digital', 'Digital'),
    )

    case_shape = models.CharField(max_length=20, choices=CASE_SHAPE_CHOICES, default=CASE_SHAPE_CHOICES[-1])
    chronograph = models.CharField(max_length=20, blank=True, choices=YES_NO_CHOICES)
    dial_colour = models.CharField(max_length=20, choices=COLOUR_CHOICES, default=COLOUR_CHOICES[0])
    strap_colour = models.CharField(max_length=20, choices=COLOUR_CHOICES, default=COLOUR_CHOICES[0])
    water_resistance = models.PositiveIntegerField(default=0, blank=True)
    analogue_or_digital = models.CharField(max_length=20, choices=ANALOGUE_OR_DIGITAL, default=ANALOGUE_OR_DIGITAL)
    watch = models.OneToOneField(Watch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.watch.brand} {self.watch.model}'
