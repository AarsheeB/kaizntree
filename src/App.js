// index.js
import React from 'react';
import AccountForm from './components/AccountForm';
import Login from './components/Login';
import ItemList from './components/ItemList';

const App = () => {
  return (
    <div>
      {/*the login form */}
      <Login />

      {/*the item dashboard */}
      <ItemList />

      {}
      <AccountForm />
    </div>
  );
};

export default App;