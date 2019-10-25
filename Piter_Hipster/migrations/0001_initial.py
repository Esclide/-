# Generated by Django 2.2.6 on 2019-10-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_delivery', models.CharField(choices=[('Почта России', 'Почта России'), ('CDEK', 'CDEK'), ('Самовывоз', 'Самовывоз')], max_length=30)),
                ('Address', models.TextField(blank=True, max_length=200, null=True)),
                ('Price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=100)),
                ('Description', models.TextField(blank=True, max_length=500, null=True)),
                ('Price', models.FloatField()),
                ('Left_in_stock', models.IntegerField()),
                ('Prime_cost', models.FloatField()),
                ('id_category', models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', to='Piter_Hipster.Categories', verbose_name='Код')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=100)),
                ('Type_sale', models.CharField(choices=[('Фиксированная', 'Фиксированная'), ('Процент', 'Процент')], max_length=30)),
                ('Size', models.FloatField()),
                ('Min_price', models.FloatField(blank=True, null=True)),
                ('Lim_start_date', models.DateField(blank=True, null=True)),
                ('Lim_end_date', models.DateField(blank=True, null=True)),
                ('Lim_cat', models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', to='Piter_Hipster.Categories')),
                ('Lim_goods', models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', to='Piter_Hipster.Goods')),
                ('Lim_mark', models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', to='Piter_Hipster.Marks')),
            ],
        ),
        migrations.CreateModel(
            name='Promocodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(max_length=100)),
                ('id_sale', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='Piter_Hipster.Sale')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Direction', models.TextField(max_length=500)),
                ('id_goods', models.ForeignKey(on_delete='CASCADE', to='Piter_Hipster.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lastname', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
                ('Middlename', models.TextField(blank=True, max_length=100, null=True)),
                ('Phone', models.TextField(max_length=20)),
                ('email', models.TextField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('В корзине', 'В корзине'), ('Создан', 'Создан'), ('Согласован', 'Согласован'), ('Оплачен', 'Оплачен'), ('В пути', 'В пути'), ('Завершен', 'Завершен')], max_length=30)),
                ('Address', models.TextField(max_length=200)),
                ('Index', models.TextField(max_length=6)),
                ('Date_of_payment', models.DateTimeField(blank=True, null=True)),
                ('Date_of_create', models.DateTimeField(auto_now_add=True)),
                ('Date_of_order', models.DateTimeField(blank=True, null=True)),
                ('Comment', models.TextField(max_length=500)),
                ('id_delivery', models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', to='Piter_Hipster.Delivery')),
                ('id_promocode', models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', to='Piter_Hipster.Promocodes')),
            ],
        ),
        migrations.CreateModel(
            name='MarkGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_goods', models.ForeignKey(on_delete='CASCADE', to='Piter_Hipster.Goods')),
                ('id_mark', models.ForeignKey(on_delete='CASCADE', to='Piter_Hipster.Marks')),
            ],
        ),
    ]
