# Generated by Django 5.0 on 2024-02-09 09:46

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('street', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(max_length=100, null=True)),
                ('city', models.IntegerField()),
                ('pincode', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'address',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AlertTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'alert_types',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ConnectivityTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'connectivity_type',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceProviderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'device_provider',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('external_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('organization_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'disease',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='EnumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'enum',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MonitoringModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('spent_time', models.IntegerField()),
                ('max_addon_timing', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('organization_id', models.IntegerField()),
            ],
            options={
                'db_table': 'monitoring',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RequestResponseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('comment', models.TextField(null=True)),
                ('request_status', models.CharField(choices=[('APPROVED', 'Approved'), ('CANCELLED', 'Cancelled'), ('PENDING', 'Pending')], max_length=20)),
            ],
            options={
                'db_table': 'request_response',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('external_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('feature_description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('manufactured_by', models.CharField(max_length=100)),
                ('uuid', models.CharField(blank=True, max_length=255, null=True)),
                ('organization_id', models.IntegerField(blank=True, null=True)),
                ('rental_cost', models.FloatField(blank=True, null=True)),
                ('buy_cost', models.FloatField(blank=True, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
                ('connectivity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.connectivitytypemodel')),
                ('device_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.deviceprovidermodel')),
            ],
            options={
                'db_table': 'device',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceImeiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('imei', models.CharField(max_length=100)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.devicemodel')),
            ],
            options={
                'db_table': 'device_imei',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceAssignmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('patient_id', models.IntegerField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('assigned_by', models.IntegerField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.devicemodel')),
            ],
            options={
                'db_table': 'device_assignment',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseDeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.devicemodel')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.diseasemodel')),
            ],
            options={
                'db_table': 'disease_device',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PackageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('period', models.IntegerField()),
                ('enrollment_cost', models.FloatField(null=True)),
                ('monitoring_cost', models.FloatField(null=True)),
                ('addon_cost', models.FloatField(null=True)),
                ('discount', models.FloatField(null=True)),
                ('offer', models.FloatField(null=True)),
                ('organization_id', models.IntegerField()),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.enummodel')),
                ('rule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.monitoringmodel')),
            ],
            options={
                'db_table': 'package',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ResponseDeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.devicemodel')),
                ('request_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.requestresponsemodel')),
            ],
            options={
                'db_table': 'response_device',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RPMRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('external_id', models.CharField(max_length=255)),
                ('patient_id', models.IntegerField()),
                ('organization_id', models.IntegerField()),
                ('provider_id', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('self_monitoring', models.BooleanField(null=True)),
                ('imei', models.CharField(max_length=255, null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpm_service.addressmodel')),
                ('disease', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpm_service.diseasemodel')),
            ],
            options={
                'db_table': 'rpm_request',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RPMBillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('bill_id', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.rpmrequestmodel')),
            ],
            options={
                'db_table': 'rpm_bill',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='requestresponsemodel',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.rpmrequestmodel'),
        ),
        migrations.CreateModel(
            name='RequestProviderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_id', models.IntegerField()),
                ('primary', models.BooleanField(null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('provider_first_name', models.CharField(max_length=100, null=True)),
                ('provider_last_name', models.CharField(max_length=100, null=True)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.rpmrequestmodel')),
            ],
            options={
                'db_table': 'request_provider',
            },
        ),
        migrations.CreateModel(
            name='RequestPackageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.packagemodel')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.rpmrequestmodel')),
            ],
            options={
                'db_table': 'request_package',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RequestMonitoringStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=255, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.enummodel')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.rpmrequestmodel')),
            ],
            options={
                'db_table': 'request_monitoring_status',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RequestDeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('rent', models.BooleanField(null=True)),
                ('existing', models.BooleanField(null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.devicemodel')),
                ('device_imei', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rpm_service.deviceimeimodel')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.rpmrequestmodel')),
            ],
            options={
                'db_table': 'request_device',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='deviceimeimodel',
            name='owned_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpm_service.rpmrequestmodel'),
        ),
        migrations.CreateModel(
            name='VitalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('dual_value', models.BooleanField(default=False)),
                ('normal_range_up', models.FloatField()),
                ('normal_range_down', models.FloatField()),
                ('vital_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.enummodel')),
            ],
            options={
                'db_table': 'vital',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ThresholdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('value1', models.FloatField()),
                ('value2', models.FloatField(null=True)),
                ('alert_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.alerttypemodel')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.enummodel')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threshold_relation', to='rpm_service.enummodel')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpm_service.rpmrequestmodel')),
                ('taken_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='threshold_taken_state', to='rpm_service.enummodel')),
                ('vital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.vitalmodel')),
            ],
            options={
                'db_table': 'threshold',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceVitalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('high_value_string', models.CharField(max_length=255, null=True)),
                ('low_value_string', models.CharField(max_length=255, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.devicemodel')),
                ('vital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.vitalmodel')),
            ],
            options={
                'db_table': 'device_vital',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VitalReadingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('data_id', models.CharField(max_length=255, null=True)),
                ('high_value', models.FloatField(null=True)),
                ('low_value', models.FloatField(null=True)),
                ('vital_jsonb_data', models.JSONField(null=True)),
                ('collection_date', models.DateTimeField()),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpm_service.devicemodel')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpm_service.rpmrequestmodel')),
                ('vital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.vitalmodel')),
            ],
            options={
                'db_table': 'vital_reading',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VitalReadingAlertModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('alert_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.alerttypemodel')),
                ('threshold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.thresholdmodel')),
                ('vital_reading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.vitalreadingmodel')),
            ],
            options={
                'db_table': 'vital_reading_alert',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VitalRulesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('timing_periods', models.IntegerField(null=True)),
                ('day_periods', models.IntegerField(null=True)),
                ('taken_state_mins', models.IntegerField(null=True)),
                ('exact_time', models.TimeField(null=True)),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpm_service.rpmrequestmodel')),
                ('taken_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpm_service.enummodel')),
                ('vital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpm_service.vitalmodel')),
            ],
            options={
                'db_table': 'vital_rules',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
    ]
