from django.test import SimpleTestCase
from apps.movies.forms import ReviewForm

class TestForms(SimpleTestCase):

    def test_revew_form_valid_data(self):
        form = ReviewForm(data={
            'name': 'AAA',
            'email': 'aaa@aaa.aa',
            'text': 'AAAAA!'
        })

        self.assertTrue(form.is_valid())