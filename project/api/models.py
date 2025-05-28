from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=99)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]


class Processor(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
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


class Motherboard(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
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


class RAM(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    memory_type = models.CharField(max_length=5)
    frequency = models.FloatField()
    xmp = models.BooleanField()
    volume = models.IntegerField()
    supply_voltage = models.FloatField()


class VideoCard(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
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


class Disc(models.Model):
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=4999)
    disc_type = models.CharField(max_length=3)
    interface = models.CharField(max_length=9)
    volume = models.IntegerField()
    read_speed = models.IntegerField()
    write_speed = models.IntegerField()


class Cooler(models):
    power_dissipation = models.IntegerField()
    diameter = models.FloatField()
    sockets = models.CharField(499)
    height = models.IntegerField()
