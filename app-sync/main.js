import { Amplify } from 'aws-amplify';
import config from './aws-exports.js';
import { generateClient } from 'aws-amplify/api'

Amplify.configure(config);

const client = generateClient()

const listFruits = `
query listFruits {
  listFruits {
    items {
      FruitID
      Fruit
      Rating
    }
  }
}
`

// Simple query
const fruits = await client.graphql({ query: listFruits })
console.log(fruits.data.listFruits.items)