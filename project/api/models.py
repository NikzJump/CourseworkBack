# Все модели приложения

from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    nik = models.CharField(max_length=99)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nik"]


class Processor(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    frequency = models.FloatField()
    frequency_turbo = models.FloatField()
    socket = models.CharField(max_length=19)
    memory_type = models.CharField(max_length=5)
    tdp = models.IntegerField()
    max_tdp = models.IntegerField()
    multiplier_block = models.BooleanField()
    architecture = models.CharField(max_length=99)
    hyper_trading = models.BooleanField()
    release_year = models.DateField()
    tech_process = models.IntegerField()
    num_core = models.IntegerField()
    max_memory_volume = models.IntegerField()
    max_temperature = models.IntegerField()
    graphic_core = models.BooleanField()
    graphic_core_name = models.CharField(max_length=99)
    pcie_version = models.FloatField()
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Processor")


class Motherboard(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    socket = models.CharField(max_length=19)
    chipset = models.CharField(max_length=19)
    memory_type = models.CharField(max_length=5)
    pcie_version = models.FloatField()
    usb_ports = models.IntegerField()
    power_phases = models.IntegerField()
    max_memory_volume = models.IntegerField()
    form_factor = models.CharField(max_length=19)
    wifi = models.BooleanField()
    pcie_lines = models.IntegerField()
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Motherboard")


class RAM(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    memory_type = models.CharField(max_length=5)
    frequency = models.FloatField()
    xmp = models.BooleanField()
    volume = models.IntegerField()
    supply_voltage = models.FloatField()
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="RAM")


class GraphicCard(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    chip_name = models.CharField(max_length=99)
    memory_type = models.CharField(max_length=5)
    architecture = models.CharField(max_length=99)
    maximum_resolution = models.CharField(max_length=19)
    core_frequency = models.FloatField()
    memory_frequency = models.FloatField()
    memory_volume = models.IntegerField()
    tech_process = models.IntegerField()
    tdp = models.IntegerField()
    pcie_version = models.FloatField()
    cuda_cores = models.IntegerField()
    memory_bus_capacity = models.IntegerField()
    add_power_connector = models.IntegerField(help_text="pin")
    num_lines_pcie = models.IntegerField()
    max_memory_bandwidth = models.FloatField(help_text="Gb/s")
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="GraphicCard")


class Disc(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    disc_type = models.CharField(max_length=3)
    interface = models.CharField(max_length=9)
    volume = models.IntegerField()
    read_speed = models.IntegerField()
    write_speed = models.IntegerField()
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Disc")


class Cooler(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    power_dissipation = models.IntegerField()
    diameter = models.FloatField()
    sockets = models.CharField(max_length=499)
    height = models.IntegerField()
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Cooler")


class Case(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    max_cooler_height = models.IntegerField()
    window_material = models.CharField(max_length=49)
    compatible_form_factors = models.CharField(max_length=99)
    form_factor = models.CharField(max_length=49)
    side_fan_support = models.CharField(max_length=99)
    front_panel_interfaces = models.CharField(max_length=199)
    possibility_install_LCS = models.BooleanField()
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Case")


class PowerUnit(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    form_factor = models.CharField(max_length=19)
    certificate_80plus = models.CharField(max_length=49)
    input_voltage_range = models.CharField(max_length=49, help_text="+ frequency of alternating current")
    total_power = models.IntegerField(help_text="W")
    power_12th_volt_line = models.IntegerField(help_text="W")
    current_12th_volt_line = models.IntegerField(help_text="А")
    num_processor_power_cables = models.IntegerField(help_text="4 pin or 4+4 pin")
    num_graphic_card_power_cables = models.IntegerField(help_text="6+2 pin")
    num_sata_connectors = models.IntegerField()
    num_molex_connectors = models.IntegerField()
    pcie_cable_length = models.IntegerField()
    sata_cable_length = models.IntegerField()
    molex_cable_length = models.IntegerField()
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="PowerUnit")


class Fan(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    size = models.CharField(max_length=19, help_text="00x00mm")
    power_connector_type = models.BooleanField(help_text="4 pin Male / 4 pin Female")
    max_rotation_speed = models.IntegerField(help_text="RPM")
    total_voltage = models.IntegerField()
    max_current = models.FloatField(help_text="mA")
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Fan")


class Monitor(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    aspect_ratio = models.CharField(max_length=19, help_text="16/9")
    screen_coverage = models.CharField(max_length=19, help_text="matte")
    resolution = models.CharField(max_length=19, help_text="1920x1080")
    contrast = models.CharField(max_length=19, help_text="1000:1")
    matrix_type = models.CharField(max_length=19)
    matrix_illumination_type = models.CharField(max_length=19)
    input_voltage_range = models.CharField(max_length=49, help_text="+ frequency of alternating current")
    hdr = models.BooleanField()
    vertical_viewing_angle = models.IntegerField(help_text="º")
    horizontal_viewing_angle = models.IntegerField(help_text="º")
    refresh_rate = models.IntegerField(help_text="Hz")
    size = models.FloatField(help_text="inch")
    ppi = models.IntegerField()
    hdmi_connector = models.BooleanField()
    displayport_connector = models.BooleanField()
    speakers = models.BooleanField()
    response_time = models.IntegerField()
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Monitor")


class Keyboard(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    origin_country = models.CharField(max_length=99)
    layout_language = models.CharField(max_length=99)
    type = models.CharField(max_length=19)
    body_material = models.CharField(max_length=19)
    connect_type = models.CharField(max_length=19)
    form_factor = models.CharField(max_length=19, help_text="70%")
    connect_interface = models.CharField(max_length=19)
    cable_length = models.IntegerField(help_text="m")
    total_num_keys = models.IntegerField()
    weight = models.IntegerField(help_text="mm")
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Keyboard")


class Mouse(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    connect_type = models.CharField(max_length=19)
    sensor_model = models.CharField(max_length=99)
    origin_country = models.CharField(max_length=99)
    num_keys = models.IntegerField()
    survey_frequency = models.IntegerField(help_text="Hz")
    speed = models.IntegerField(help_text="IPS")
    weight = models.IntegerField(help_text="mm")
    warranty_period = models.IntegerField(help_text="month")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Mouse")


class Headphones(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    connect_type = models.CharField(max_length=19)
    origin_country = models.CharField(max_length=99)
    microphone = models.BooleanField()
    max_reproducible_frequency = models.IntegerField(help_text="Hz")
    min_reproducible_frequency = models.IntegerField(help_text="Hz")
    warranty_period = models.IntegerField(help_text="month")
    connector = models.CharField(max_length=99)
    type = models.CharField(max_length=99, help_text="Headphones/speaker/microphone")
    price = models.IntegerField()
    category = models.CharField(max_length=99, default="Headphones")


# модельки на будущее
# после обязательно разделить модели вместе с вьюхами
# class Products(models.Model):
#     processors = models.ForeignKey(Processor, )
#     graphic_cards = models.ForeignKey(GraphicCard, on_delete=models.CASCADE)
#     motherboards = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
#     RAM = models.ForeignKey(RAM, on_delete=models.CASCADE)
#     discs = models.ForeignKey(Disc, on_delete=models.CASCADE)
#     coolers = models.ForeignKey(Cooler, on_delete=models.CASCADE)
#     cases = models.ForeignKey(Case, on_delete=models.CASCADE)
#     power_unit = models.ForeignKey(PowerUnit, on_delete=models.CASCADE)
#     fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
#     monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
#     keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
#     mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
#     headphones = models.ForeignKey(Headphones, on_delete=models.CASCADE)


# class SavedPreset(models.Model):
#     processor = models.ForeignKey(Processor, on_delete=models.CASCADE, default=None)
#     graphic_card = models.ForeignKey(GraphicCard, on_delete=models.CASCADE, default=None)
#     motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE, default=None)
#     disc = models.ForeignKey(Disc, on_delete=models.CASCADE, default=None)
#     fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
#     power_unit = models.ForeignKey(PowerUnit, on_delete=models.CASCADE, default=None)
#     case = models.ForeignKey(Case, on_delete=models.CASCADE, default=None)
#     cooler = models.ForeignKey(Cooler, on_delete=models.CASCADE, default=None)
#     category = models.CharField(max_length=99)


class Cart(models.Model):
    processors = models.ManyToManyField(Processor, null=True)
    graphic_cards = models.ManyToManyField(GraphicCard, null=True)
    motherboards = models.ManyToManyField(Motherboard, null=True)
    RAM = models.ManyToManyField(RAM, null=True)
    discs = models.ManyToManyField(Disc, null=True)
    coolers = models.ManyToManyField(Cooler, null=True)
    cases = models.ManyToManyField(Case, null=True)
    power_unit = models.ManyToManyField(PowerUnit, null=True)
    fan = models.ManyToManyField(Fan, null=True)
    monitor = models.ManyToManyField(Monitor, null=True)
    keyboard = models.ManyToManyField(Keyboard, null=True)
    mouse = models.ManyToManyField(Mouse, null=True)
    headphones = models.ManyToManyField(Headphones, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    processors = models.ManyToManyField(Processor, null=True)
    graphic_cards = models.ManyToManyField(GraphicCard, null=True)
    motherboards = models.ManyToManyField(Motherboard, null=True)
    RAM = models.ManyToManyField(RAM, null=True)
    discs = models.ManyToManyField(Disc, null=True)
    coolers = models.ManyToManyField(Cooler, null=True)
    cases = models.ManyToManyField(Case, null=True)
    power_unit = models.ManyToManyField(PowerUnit, null=True)
    fan = models.ManyToManyField(Fan, null=True)
    monitor = models.ManyToManyField(Monitor, null=True)
    keyboard = models.ManyToManyField(Keyboard, null=True)
    mouse = models.ManyToManyField(Mouse, null=True)
    headphones = models.ManyToManyField(Headphones, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_price = models.IntegerField(default=0)
