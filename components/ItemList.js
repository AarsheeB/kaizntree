// src/components/ItemList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ItemList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Fetch items from your Django API
    axios.get('http://localhost:8000/api/items/')
      .then(response => {
        setItems(response.data);
      })
      .catch(error => {
        console.error('Error fetching items:', error);
      });
  }, []); // Empty dependency array to run the effect only once on mount

  return (
    <div>
      <h1>Item Dashboard</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            <strong>{item.name}</strong> - SKU: {item.sku}, Category: {item.category}, Stock: {item.stock_status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ItemList;
