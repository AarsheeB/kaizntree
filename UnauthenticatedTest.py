def test_unauthenticated_access(self):
    # Make requests to protected endpoints without authentication
    response = self.client.get(reverse('item-list-create'))
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Add more cases for other HTTP methods and endpoints as needed
