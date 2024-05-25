# Generated by Django 5.0.4 on 2024-05-01 13:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_product_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('An Giang', 'An Giang'), ('Ba Ria - Vung Tau', 'Bà Rịa – Vũng Tàu'), ('Bac Lieu', 'Bạc Liêu'), ('Bac Giang', 'Bắc Giang'), ('Bac Kan', 'Bắc Kạn'), ('Bac Ninh', 'Bắc Ninh'), ('Ben Tre', 'Bến Tre'), ('Binh Duong', 'Bình Dương'), ('Binh Dinh', 'Bình Định'), ('Binh Phuoc', 'Bình Phước'), ('Binh Thuan', 'Bình Thuận'), ('Ca Mau', 'Cà Mau'), ('Cao Bang', 'Cao Bằng'), ('Can Tho', 'Cần Thơ'), ('Da Nang', 'Đà Nẵng'), ('Dak Lak', 'Đắk Lắk'), ('Dak Nong', 'Đắk Nông'), ('Dien Bien', 'Điện Biên'), ('Dong Nai', 'Đồng Nai'), ('Dong Thap', 'Đồng Tháp'), ('Gia Lai', 'Gia Lai'), ('Ha Giang', 'Hà Giang'), ('Ha Nam', 'Hà Nam'), ('Ha Noi', 'Hà Nội'), ('Ha Tinh', 'Hà Tĩnh'), ('Hai Duong', 'Hải Dương'), ('Hai Phong', 'Hải Phòng'), ('Hau Giang', 'Hậu Giang'), ('Hoa Binh', 'Hòa Bình'), ('Ho Chi Minh City', 'Thành phố Hồ Chí Minh'), ('Hung Yen', 'Hưng Yên'), ('Khanh Hoa', 'Khánh Hòa'), ('Kien Giang', 'Kiên Giang'), ('Kon Tum', 'Kon Tum'), ('Lai Chau', 'Lai Châu'), ('Lang Son', 'Lạng Sơn'), ('Lao Cai', 'Lào Cai'), ('Lam Dong', 'Lâm Đồng'), ('Long An', 'Long An'), ('Nam Dinh', 'Nam Định'), ('Nghe An', 'Nghệ An'), ('Ninh Binh', 'Ninh Bình'), ('Ninh Thuan', 'Ninh Thuận'), ('Phu Tho', 'Phú Thọ'), ('Phu Yen', 'Phú Yên'), ('Quang Binh', 'Quảng Bình'), ('Quang Nam', 'Quảng Nam'), ('Quang Ngai', 'Quảng Ngãi'), ('Quang Ninh', 'Quảng Ninh'), ('Quang Tri', 'Quảng Trị'), ('Soc Trang', 'Sóc Trăng'), ('Son La', 'Sơn La'), ('Tay Ninh', 'Tây Ninh'), ('Thai Binh', 'Thái Bình'), ('Thai Nguyen', 'Thái Nguyên'), ('Thanh Hoa', 'Thanh Hóa'), ('Thua Thien Hue', 'Thừa Thiên Huế'), ('Tien Giang', 'Tiền Giang'), ('Tra Vinh', 'Trà Vinh'), ('Tuyen Quang', 'Tuyên Quang'), ('Vinh Long', 'Vĩnh Long'), ('Vinh Phuc', 'Vĩnh Phúc'), ('Yen Bai', 'Yên Bái')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
