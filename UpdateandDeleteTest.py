def test_update_item(self):
    # Create a sample item
    item = Item.objects.create(name='Old Item', quantity=5, price=10.0)

    # Data for updating the item
    updated_item_data = {
        'name': 'Updated Item',
        'quantity': 8,
        'price': 12.0,
    }

    # Make a PUT request to update the item
    response = self.client.put(reverse('item-retrieve-update-destroy', args=[item.id]), updated_item_data, format='json')

    # Check if the response status code is 200 (OK)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Check if the item is updated in the database
    updated_item = Item.objects.get(id=item.id)
    self.assertEqual(updated_item.name, updated_item_data['name'])
    self.assertEqual(updated_item.quantity, updated_item_data['quantity'])
    self.assertEqual(updated_item.price, updated_item_data['price'])

def test_delete_item(self):
    # Create a sample item
    item = Item.objects.create(name='Item to Delete', quantity=3, price=8.0)

    # Make a DELETE request to delete the item
    response = self.client.delete(reverse('item-retrieve-update-destroy', args=[item.id]))

    # Check if the response status code is 204 (No Content)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Check if the item is deleted from the database
    with self.assertRaises(Item.DoesNotExist):
        Item.objects.get(id=item.id)
