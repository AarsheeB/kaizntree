def test_retrieve_item(self):
    # Create a sample item
    item = Item.objects.create(name='Test Item', quantity=10, price=15.0)

    # Make a GET request to retrieve the item
    response = self.client.get(reverse('item-retrieve-update-destroy', args=[item.id]))

    # Check if the response status code is 200 (OK)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Check if the response data matches the created item
    self.assertEqual(response.data['name'], item.name)
    self.assertEqual(response.data['quantity'], item.quantity)
    self.assertEqual(response.data['price'], item.price)
