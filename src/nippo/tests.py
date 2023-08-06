from django.test import TestCase
from django.urls import reverse
from .models import NippoModel


class NippoTestCase(TestCase):
    # 初期設定
    def setUp(self):
        obj = NippoModel(title='testTitle', content='testContent')
        obj.save()

    # 日報が作成ができているか
    def test_saved_single_object(self):
        count = NippoModel.objects.count()
        self.assertEqual(count, 1)
        
    # queryが存在しないときに、404ページを返すか。
    def test_response_404(self):
        detail_url = reverse('nippo-detail', kwargs={'pk':100})
        detail_response = self.client.get(detail_url)
        self.assertEqual(detail_response.status_code, 404)

        update_url = reverse('nippo-update', kwargs={'pk':100})
        update_response = self.client.get(update_url)
        self.assertEqual(update_response.status_code, 404)

        delete_url = reverse('nippo-delete', kwargs={'pk':100})
        delete_response = self.client.get(delete_url)
        self.assertEqual(delete_response.status_code, 404)

    # createできちんとデータが保存されているか。
    def test_create_on_createView(self):
        create_url = reverse('nippo-create')
        create_data = {'title': 'title_from_test', 'content':'content_from_test'}
        response = self.client.post(create_url, create_data)
        count = NippoModel.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(count, 2)

