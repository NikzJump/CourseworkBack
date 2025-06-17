from django.contrib import admin
from .models import product_models


admin.site.register(product_models.Processor)
admin.site.register(product_models.SavedPreset)
admin.site.register(product_models.Mouse)
admin.site.register(product_models.Cooler)
admin.site.register(product_models.Headphones)
admin.site.register(product_models.Keyboard)
admin.site.register(product_models.PowerUnit)
admin.site.register(product_models.Motherboard)
admin.site.register(product_models.Disc)
admin.site.register(product_models.GraphicCard)
admin.site.register(product_models.RAM)
admin.site.register(product_models.Case)
admin.site.register(product_models.Fan)
