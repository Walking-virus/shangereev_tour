from django.db import models

class ContactUs(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	tel = models.IntegerField()
	message = models.TextField()

	def __str__ (self):
		return self.name


class AboutUs(models.Model):
	image_aboutUs = models.ImageField(upload_to='images_aboutUs/')
	description_aboutUs = models.TextField()

	def __str__(self):
		return self.description_aboutUs


class Command(models.Model):	
	photo_employee = models.ImageField(upload_to='images_command/')
	name_employee = models.CharField(max_length=50)
	description_employee = models.TextField()

	def __str__ (self):
		return self.name_employee	


class Trips(models.Model):
	trips_name = models.CharField(max_length = 50)
	url = models.SlugField(max_length=160, unique=True)

	def __str__ (self):
		return self.trips_name


class Travel(models.Model):	
	photo_main = models.ImageField(upload_to='images_travel/')
	video_travel = models.FileField(upload_to='videos_travel/')
	name_travel = models.CharField(max_length=50)
	price_travel = models.IntegerField()
	description_travel = models.TextField()
	url = models.SlugField(max_length=160, unique=True)
	trips = models.ForeignKey(Trips, on_delete = models.CASCADE)

	def __str__ (self):
		return self.name_travel				
	
	class Meta:
		ordering = ('name_travel',)



class Timetable(models.Model):
	sending_date = models.DateField()
	departure_date = models.DateField(blank='True')
	name_trips = models.ManyToManyField(Travel)

	def __str__(self):
		return 'Расписание'

	class Meta:
		ordering = ('-sending_date',)
			


class Images(models.Model):	
	images_travel = models.ImageField(upload_to='images_carusel/', blank=True)
	travel = models.ForeignKey(Travel, on_delete = models.CASCADE, related_name='travel')

	def __str__ (self):
		return 'Изображения на карусели'


class Comment(models.Model):
    comment_travel = models.ForeignKey(Travel, on_delete = models.CASCADE, related_name='comment')
    release_date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField("Ваше имя:", max_length=50)
    user_comment = models.TextField("Текст:")	
	
    def __str__(self):
        return self.user_name