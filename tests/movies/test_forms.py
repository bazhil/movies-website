from django.test import SimpleTestCase
from apps.movies.forms import ReviewForm

class TestForms(SimpleTestCase):

    # def test_revew_form_valid_data(self):
    # #TODO: найти способ тестировать формы с капчей
    #     form = ReviewForm(data={
    #         'name': 'AAA',
    #         'email': 'aaa@aaa.aa',
    #         'text': 'AAAAA!'
    #     })
    #
    #     self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = ReviewForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
