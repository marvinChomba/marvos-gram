from django.test import TestCase
from .models import Image,Comments,Profile
from django.contrib.auth.models import User

# Create your tests here.

class ImageTestCase(TestCase):
    """
    This is the class I will use to test the images
    """
    def setUp(self):
        """
        This will create a new imae before each test
        """
        self.new_user = User(username = "Hey", email = "marvin.chomba24@gmaul.com",password = "heyjfbghjdnf")
        self.new_user.save()
        self.new_image = Image(name = 'Hey', user = self.new_user)
        self.new_image.save()

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

    def test_image_delete(self):
        """
        This will test whether the image is deleted from the db
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
        self.new_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_edit_caption(self):
        """
        This will test the edit caption function
        """
        self.new_image.save_image()
        image = Image.objects.get(id = 1)
        image.update_caption("Hey there")
        self.assertTrue(image.caption == "Hey there")


class CommentTestCases(TestCase):
    """
    This is the class I will use to test the comments
    """
    def setUp(self):
        """
        This will create a new comment before every test
        """
        self.new_user = User(username = "Hey")
        self.new_user.save()
        self.new_image = Image(name = 'hey', user = self.new_user)
        self.new_image.save_image()
        self.new_comment = Comments(comment = "Cool", image = self.new_image)

    def tearDown(self):
        """
        This will clear the dbs after each test
        """
        User.objects.all().delete()
        Image.objects.all().delete()
        Comments.objects.all().delete()

    def test_is_instance(self):
        """
        This will test whether the new comment created is an instance of the comment class
        """
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_init(self):
        """
        This will test whether the new comment is instantiated correctly
        """
        self.assertTrue(self.new_comment.comment = "Cool")

    def test_save_comment(self):
        """
        This will test whether the new comment is added to the db
        """
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.objects.all()) > 0)

    def test_delete_comment(self):
        """
        This will test whether the comment is deleted
        """
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.objects.all()) > 0)
        self.new_comment.delete_comment()
        self.assertTrue(len(Comments.objects.all()) == 0)

    def test_edit_comment(self):
        """
        This will test whether the new comment can be edited
        """
        self.new_comment.save_comment()
        comm = Comments.objects.get(id = 1)
        comm.update_comment("New one")
        self.assertTrue(self.objects.get(id =1).comment = "New one")

class ProfileTestCases(self):
    """
    This will test the profiles
    """
    def setUp(self):
        """
        This will add a new profile before each test
        """
        self.new_user = User(username = "Hey")
        self.new_user.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        
    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.new_user.profile, Profile))

    def test_init(self):
        """
        This will test whether the new profile is created coreectly
        """
        self.assertTrue(self.new_user.profile.bio == "Hi!")

    def test_search_users(self):
        """
        This will test whether the search function works
        """
        users = Profile.search_user("hey")
        self.assertTrue(len(users) == 1)
        

