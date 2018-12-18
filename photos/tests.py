from django.test import TestCase
from .models import Image

# Create your tests here.

class ImageTestCase(TestCase):
    """
    This is the class I will use to test the images
    """
    def setUp(self):
        """
        This will create a new imae before each test
        """
        self.new_image = Image(name = 'Hey')

    def tearDown(self):
        """  
        This will clear the db after each test
        """
        Image.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the new image created is an instance of the Image class
        """
        self.assertTrue(isinstance(self.new_image, Image))

    def test_init(self):
        """
        This will test whether the new image is instantiated correctly
        """

        self.assertTrue(self.new_image.name == "Hey")

    def test_save_image(self):
        """
        This will test whether the new image is added to the db
        """
        self.new_image.save_image()    
        self.assertTrue(len(Image.objects.all()) > 0)