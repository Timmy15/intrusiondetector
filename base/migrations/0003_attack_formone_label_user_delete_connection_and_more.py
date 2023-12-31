# Generated by Django 4.2.3 on 2023-07-18 15:30

import base.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_connection_created_alter_connection_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack_name', models.CharField(max_length=20)),
                ('attack_description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('recommended_actions', models.TextField(blank=True, null=True)),
                ('attack_category', models.TextField(blank=True, null=True)),
                ('attack_severity_level', models.TextField(blank=True, null=True)),
                ('the_result', models.CharField(max_length=20)),
                ('feedback', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.SmallIntegerField(help_text='Length (number of seconds) of the connection.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('protocol_type', models.CharField(choices=[('udp', 'UDP'), ('tcp', 'TCP'), ('icmp', 'ICMP')], help_text='Type of the protocol, e.g. tcp, udp, etc.', max_length=5)),
                ('protocol_service', models.CharField(choices=[('private', 'Private'), ('domain_u', 'Domain_U'), ('http', 'HTTP'), ('smtp', 'SMTP'), ('ftp_data', 'FTP_Data'), ('ftp', 'FTP'), ('eco_i', 'ECO_I'), ('other', 'Other'), ('auth', 'Auth'), ('ecr_i', 'ECR_I'), ('irc', 'IRC'), ('x11', 'X11'), ('finger', 'Finger'), ('time', 'Time'), ('domain', 'Domain'), ('telnet', 'Telnet'), ('pop_3', 'POP_3'), ('idap', 'Idap'), ('login', 'Login'), ('name', 'Name'), ('ntp_u', 'NTP_U'), ('http_443', 'HTTP_443'), ('sunrpc', 'Sunrpc'), ('printer', 'Printer'), ('systat', 'Systat'), ('tim_i', 'Tim_I'), ('netstat', 'Netstat'), ('remote_job', 'Remote_Job'), ('link', 'Link'), ('urp_i', 'URP_I'), ('sql_net', 'SQL_Net'), ('bgp', 'BGP'), ('pop_2', 'POP_2'), ('tftp_u', 'TFTP_U'), ('uucp', 'UUCP'), ('imap4', 'IMAP4'), ('pm_dump', 'PM_Dump'), ('nnsp', 'NNSP'), ('courier', 'Courier'), ('daytime', 'Daytime'), ('iso_tsap', 'ISO_TSAP'), ('echo', 'Echo'), ('discard', 'Discard'), ('ssh', 'SSH'), ('whois', 'Whois'), ('mtp', 'MTP'), ('gopher', 'Gopher'), ('rje', 'RJE'), ('ctf', 'CTF'), ('supdup', 'Supdup'), ('hostname', 'Hostname'), ('csnet_ns', 'Csnet_Ns'), ('uucp_path', 'UUCP_Path'), ('nntp', 'NNTP'), ('netbios_ns', 'Netbios_NS'), ('netbios_dgm', 'Netbios_DGM'), ('netbios_ssn', 'Netbios_SSN'), ('vmnet', 'VMnet'), ('z39_50', 'Z39_50'), ('exec', 'Exec'), ('shell', 'Shell'), ('efs', 'EFS'), ('klogin', 'Klogin'), ('kshell', 'Kshell'), ('icmp', 'ICMP')], help_text='Network service on the destination, e.g., http, telnet, etc.', max_length=20)),
                ('the_flag', models.CharField(choices=[('sf', 'SF'), ('rstr', 'RSTR'), ('s1', 'S1'), ('rej', 'REJ'), ('s3', 'S3'), ('rsto', 'RSTO'), ('s0', 'S0'), ('s2', 'S2'), ('rstos0', 'RSTOS0'), ('sh', 'SH'), ('oth', 'OTH')], help_text='Normal or error status of the connection', max_length=10)),
                ('src_bytes', models.CharField(help_text='Number of data bytes from source to destination.', max_length=6, validators=[base.models.validate_number])),
                ('dst_bytes', models.CharField(help_text='Number of data bytes from destination to source.', max_length=6, validators=[base.models.validate_number])),
                ('land', models.CharField(choices=[('0', '0'), ('1', '1')], help_text='1 if connection is from/to the same host/port; 0 otherwise.', max_length=1)),
                ('wrong_fragment', models.SmallIntegerField(help_text='Number of "wrong" fragments.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('urgent', models.SmallIntegerField(help_text='Number of urgent packets.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('hot', models.SmallIntegerField(help_text='Number of "hot" indicators.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('num_failed_logins', models.SmallIntegerField(help_text='Number of failed login attempts.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('logged_in', models.CharField(choices=[('0', '0'), ('1', '1')], help_text='1 if successfully logged in; 0 otherwise.', max_length=1)),
                ('num_compromised', models.SmallIntegerField(help_text='Number of "compromised" conditions.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('root_shell', models.CharField(choices=[('0', '0'), ('1', '1')], help_text='1 if root shell is obtained; 0 otherwise.', max_length=1)),
                ('su_attempted', models.CharField(choices=[('0', '0'), ('1', '1')], help_text='1 if "su root" command attempted; 0 otherwise.', max_length=1)),
                ('num_root', models.SmallIntegerField(help_text='Number of "root" accesses.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('num_file_creations', models.SmallIntegerField(help_text='Number of file creation operations.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('num_shells', models.SmallIntegerField(help_text='Number of shell prompts.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('num_access_files', models.SmallIntegerField(help_text='Number of operations on access control files.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('num_outbound_cmds', models.SmallIntegerField(help_text='Number of outbound commands in an ftp session.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('is_host_login', models.CharField(choices=[('0', '0'), ('1', '1')], help_text='1 if the login belongs to the "host" list; 0 otherwise.', max_length=1)),
                ('is_guest_login', models.CharField(choices=[('0', '0'), ('1', '1')], help_text='1 if the login is a "guest" login; 0 otherwise.', max_length=1)),
                ('the_count', models.SmallIntegerField(help_text='Number of connections to the same host as the current connection in the past two seconds.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('srv_count', models.SmallIntegerField(help_text='Number of connections to the same service as the current connection in the past two seconds.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('serror_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections that have "SYN" errors.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('srv_serror_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections that have "SYN" errors.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('rerror_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections that have "REJ" errors.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('srv_rerror_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections that have "REJ" errors.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('same_srv_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections to the same service.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('diff_srv_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections to different services.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('srv_diff_host_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections to different hosts.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('dst_host_count', models.SmallIntegerField(help_text='Number of connections having the same destination host in the past two seconds.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('dst_host_srv_count', models.SmallIntegerField(help_text='Number of connections having the same destination host and using the same service in the past two seconds.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('dst_host_same_srv_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections to the same service, among the connections to the same destination host in the past two seconds.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('dst_host_diff_srv_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections to different services, among the connections to the same destination host in the past two seconds.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('dst_host_same_src_port_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections from the same source port, among the connections from the same source IP in the past two seconds.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('dst_host_srv_diff_host_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections to different destination hosts, among the connections to the same destination host and the same service in the past two seconds.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('dst_host_serror_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections that have activated the flag (s0, s1, s2 or s3) among the connections to the same destination host, in the past two seconds.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('dst_host_srv_serror_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections that have activated the flag (s0, s1, s2 or s3) among the connections to the same destination host and the same service, in the past two seconds.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('dst_host_rerror_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections that have activated the flag (REJ) among the connections to the same destination host, in the past two seconds.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
                ('dst_host_srv_rerror_rate', models.DecimalField(decimal_places=2, help_text='Percentage of connections that have activated the flag (REJ) among the connections to the same destination host and the same service, in the past two seconds.', max_digits=5, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=5)])),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Connection',
        ),
        migrations.AddField(
            model_name='attack',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.user'),
        ),
        migrations.AddField(
            model_name='attack',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.label'),
        ),
    ]
