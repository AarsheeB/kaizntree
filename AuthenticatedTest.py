def test_authenticated_access(self):
    # Create a user and obtain a token
    user = User.objects.create_user(username='testuser', password='testpassword')
    token = Token.objects.create(user=user)

    # Authenticate the client using the obtained token
    self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    # Make requests to protected endpoints with authentication
    response = self.client.get(reverse('item-list-create'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more cases for other HTTP methods and endpoints as needed
