from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, DecimalValidator
from django.core.exceptions import ValidationError


def validate_number(value):
    try:
        value = int(value)
    except ValueError:
        raise ValidationError("This field requires a number.")
    if value < 0 or value > 900000:
        raise ValidationError("Number should be in range 0-900000")
    



# Create your models here.
class User(AbstractUser):

    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
       return self.name
    
    
# class Attacks(models.Model):
#     attack_name = models.CharField(max_length=20)
#     attack_category = models.CharField(max_length=20)

#     def __str__(self):
#         return self.attack_name


class Attack(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    recommended_actions = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    severity_level = models.TextField(null=True, blank=True)
    #historical_context = 

    def __str__(self):
        return str(self.name)
    

# class Label(models.Model):
#     name = models.CharField(max_length=255, unique=True, help_text='Give this connection a name to identify it e.g Connection_01')
#     def __str__(self):
#         return self.name

class FormOne(models.Model):
    PROTOCOLTYPE_CHOICES = [
        ('udp', 'UDP'),
        ('tcp', 'TCP'),
        ('icmp', 'ICMP'),
    ]
    PROTOCOLSERVICE_CHOICES = [
        ('private', 'Private'),
        ('domain_u', 'Domain_U'),
        ('http', 'HTTP'),
        ('smtp', 'SMTP'),
        ('ftp_data', 'FTP_Data'),
        ('ftp', 'FTP'),
        ('eco_i', 'ECO_I'),
        ('other', 'Other'),
        ('auth', 'Auth'),
        ('ecr_i', 'ECR_I'),
        ('irc', 'IRC'),
        ('x11', 'X11'),
        ('finger', 'Finger'),
        ('time', 'Time'),
        ('domain', 'Domain'),
        ('telnet', 'Telnet'),
        ('pop_3', 'POP_3'),
        ('idap', 'Idap'),
        ('login', 'Login'),
        ('name', 'Name'),
        ('ntp_u', 'NTP_U'),
        ('http_443', 'HTTP_443'),
        ('sunrpc', 'Sunrpc'),
        ('printer', 'Printer'),
        ('systat', 'Systat'),
        ('tim_i', 'Tim_I'),
        ('netstat', 'Netstat'),
        ('remote_job', 'Remote_Job'),
        ('link', 'Link'),
        ('urp_i', 'URP_I'),
        ('sql_net', 'SQL_Net'),
        ('bgp', 'BGP'),
        ('pop_2', 'POP_2'),
        ('tftp_u', 'TFTP_U'),
        ('uucp', 'UUCP'),
        ('imap4', 'IMAP4'),
        ('pm_dump', 'PM_Dump'),
        ('nnsp', 'NNSP'),
        ('courier', 'Courier'),
        ('daytime', 'Daytime'),
        ('iso_tsap', 'ISO_TSAP'),
        ('echo', 'Echo'),
        ('discard', 'Discard'),
        ('ssh', 'SSH'),
        ('whois', 'Whois'),
        ('mtp', 'MTP'),
        ('gopher', 'Gopher'),
        ('rje', 'RJE'),
        ('ctf', 'CTF'),
        ('supdup', 'Supdup'),
        ('hostname', 'Hostname'),
        ('csnet_ns', 'Csnet_Ns'),
        ('uucp_path', 'UUCP_Path'),
        ('nntp', 'NNTP'),
        ('netbios_ns', 'Netbios_NS'),
        ('netbios_dgm', 'Netbios_DGM'),
        ('netbios_ssn', 'Netbios_SSN'),
        ('vmnet', 'VMnet'),
        ('z39_50', 'Z39_50'),
        ('exec', 'Exec'),
        ('shell', 'Shell'),
        ('efs', 'EFS'),
        ('klogin', 'Klogin'),
        ('kshell', 'Kshell'),
        ('icmp', 'ICMP')  
    ]

    DOS_CHOICES = [
    (0, 'Not a DOS attack'),
    (1, 'DOS attack'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=255, unique=True, help_text='Give this connection a name to identify it e.g Connection_01')
    protocol_type = models.CharField(max_length=5, choices=PROTOCOLTYPE_CHOICES, help_text='Type of the protocol, e.g. tcp, udp, etc.')
    protocol_service = models.CharField(max_length=20, choices=PROTOCOLSERVICE_CHOICES, help_text='Network service on the destination, e.g., http, telnet, etc.')
    src_bytes = models.CharField(max_length=6, validators=[validate_number], help_text='Number of data bytes from source to destination.')
    dst_bytes = models.CharField(max_length=6, validators=[validate_number], help_text='Number of data bytes from destination to source.')
    the_count = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], help_text='Number of connections to the same host as the current connection in the past two seconds.')
    srv_count = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], help_text='Number of connections to the same service as the current connection in the past two seconds.')
    dst_host_diff_srv_rate = models.DecimalField(max_digits=5, decimal_places=2, validators=[DecimalValidator(max_digits=5, decimal_places=2)], help_text='Percentage of connections to different services, among the connections to the same destination host in the past two seconds.')
    dst_host_same_src_port_rate = models.DecimalField(max_digits=5, decimal_places=2, validators=[DecimalValidator(max_digits=5, decimal_places=2)], help_text='Percentage of connections from the same source port, among the connections from the same source IP in the past two seconds.')
    is_DOS = models.IntegerField(choices=DOS_CHOICES, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.label

    # def save(self, *args, **kwargs):
    # # First, let's check if the user has provided a label in the form
    #     if hasattr(self, 'label_name') and self.label_name:
    #         self.label, created = Label.objects.get_or_create(name=self.label_name)
    #     elif not self.label_id:  # If no user label, and no auto-generated label, then generate one
    #         last_form = FormOne.objects.filter(user=self.user).order_by('-id').first()
    #         new_number = 1

    #         if last_form and 'Connection_' in last_form.label.name:  # Assuming Label model has a field named 'name'
    #             last_number = int(last_form.label.name.split('_')[-1])
    #             new_number = last_number + 1

    #         label_name = f"Connection_{new_number:02d}"
            
    #         # Ensure the label is unique for the user
    #         while FormOne.objects.filter(user=self.user, label__name=label_name).exists():
    #             new_number += 1
    #             label_name = f"Connection_{new_number:02d}"

    #         # Create or fetch the Label instance
    #         self.label, created = Label.objects.get_or_create(name=label_name)

    #     super(FormOne, self).save(*args, **kwargs)







class Message(models.Model):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    label = models.ForeignKey(FormOne, on_delete=models.CASCADE)
    attack_name = models.ForeignKey(Attack, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200, null=True)



    # message_instance = Message.objects.get(pk=1)
    # recommended_actions = message_instance.attack_name.recommended_actions
    # attack_severity_level = message_instance.attack_name.attack_severity_level
    # body = message_instance.attack_name.attack_description
    # attack_category = message_instance.attack_name.attack_category
    # updated = message_instance.label.updated
    # created = message_instance.label.created


    # class Meta:
    #     ordering = ['-updated', '-created']

    # def __str__(self):
    #     return self.body[0:50]

    # RESULTS =[
    #     ('normal', 'Normal'),
    #     ('snmpgetattack', 'SNMPGetAttack'),
    #     ('named', 'Named'),
    #     ('xlock', 'Xlock'),
    #     ('smurf', 'Smurf'),
    #     ('ipsweep', 'IPsweep'),
    #     ('multihop', 'Multihop'),
    #     ('xsnoop', 'Xsnoop'),
    #     ('sendmail', 'Sendmail'),
    #     ('guess_passwd', 'Guess_Password'),
    #     ('saint', 'Saint'),
    #     ('buffer_overflow', 'Buffer_Overflow'),
    #     ('portsweep', 'Portsweep'),
    #     ('pod', 'Pod'), 
    #     ('apache2', 'Apache2'),
    #     ('phf', 'PHF'),
    #     ('udpstorm', 'UDPstorm'),
    #     ('warezmaster', 'Warezmaster'),
    #     ('perl', 'Perl'),
    #     ('satan', 'Satan'),
    #     ('xterm', 'Xterm'),
    #     ('mscan', 'Mscan'),
    #     ('processtable', 'Processtable'),
    #     ('ps', 'PS'),
    #     ('nmap', 'Nmap'),
    #     ('rootkit', 'Rootkit'),
    #     ('back', 'Back'),
    #     ('ftp_write', 'FTP_Write'),
    #     ('imap', 'Imap'),
    #     ('land', 'Land'),
    #     ('loadmodule', 'Loadmodule'),
    #     ('neptune', 'Neptune'),
    #     ('spy', 'Spy'),
    #     ('teardrop', 'Teardrop'),
    #     ('warezclient', 'Warezclient'),
    #     ('snmpguess', 'SNMPguess'),
    #     ('httptunnel', 'HTTPtunnel'),
    #     ('mailbomb', 'Mailbomb')
    # ]

