from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse

from cars_universe.forms import CreatePartForm, EditPartForm, DeletePartForm, OrderForm
from cars_universe.web.models.models import CarPart, Order, Tool


class ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.part = CarPart.objects.create(name='Test Part', price=10)
        self.tool = Tool.objects.create(name='Test Tool', price=20)
        self.order = Order.objects.create(user=self.user, address='Test Address')

    def test_create_part_view(self):
        url = reverse('create_part')
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'part_create.html')
        self.assertContains(response, 'Create Part')
        self.assertIsInstance(response.context['form'], CreatePartForm)

    def test_edit_part_view(self):
        url = reverse('edit_part', args=[self.part.pk])
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'part_edit.html')
        self.assertContains(response, 'Edit Part')
        self.assertIsInstance(response.context['form'], EditPartForm)
        self.assertEqual(response.context['part'], self.part)

    def test_delete_part_view(self):
        url = reverse('delete_part', args=[self.part.pk])
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'part_delete.html')
        self.assertContains(response, 'Delete Part')
        self.assertIsInstance(response.context['form'], DeletePartForm)
        self.assertEqual(response.context['part'], self.part)

    def test_add_to_cart_view(self):
        url = reverse('add_to_cart', args=[self.tool.pk, 'tool'])
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tools'))
        self.assertIn('cart', request.session)
        self.assertEqual(request.session['cart'][30]['id'], self.tool.id)

    def test_remove_from_cart_view(self):
        request = self.factory.get(reverse('remove_from_cart', args=[self.tool.id]))
        request.user = self.user
        request.session['cart'] = {30: {'id': self.tool.id}}
        response = self.client.get(reverse('remove_from_cart', args=[self.tool.id]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('cart'))
        self.assertNotIn(30, request.session['cart'])

    def test_clear_cart_view(self):
        request = self.factory.get(reverse('clear_cart'))
        request.user = self.user
        request.session['cart'] = {30: {'id': self.tool.id}}
        response = self.client.get(reverse('clear_cart'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('cart'))
        self.assertNotIn('cart', request.session)

    def test_cart_page_view(self):
        request = self.factory.get(reverse('cart'))
        request.user = self.user
        request.session['cart'] = {30: {'id': self.tool.id, 'type': 'tool'}}
        response = self.client.get(reverse('cart'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
        self.assertEqual(len(response.context['cart_items']), 1)
        self.assertEqual(response.context['cart_total'], self.tool.price)
        self.assertIsInstance(response.context['order_form'], OrderForm)

    def test_view_orders_view(self):
        url = reverse('view_orders')
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders.html')
        self.assertEqual(len(response.context['orders']), 1)
        self.assertIn(self.order.id, response.context['items_dict'])
        self.assertIsInstance(response.context['items_dict'][self.order.id][0][0], Tool)

    def test_place_order_view(self):
        url = reverse('place_order')
        data = {
            'address': 'Test Address'
        }
        request = self.factory.post(url, data)
        request.user = self.user
        request.session['cart'] = {30: {'id': self.tool.id, 'type': 'tool'}}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        self.assertFalse('cart' in request.session)
        self.assertEqual(Order.objects.count(), 2)


