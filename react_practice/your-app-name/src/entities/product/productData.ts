export interface Product {
  id: number;
  name: string;
  price: number;
}

export const products: Product[] = [
  { id: 1, name: "iPhone", price: 80000 },
  { id: 2, name: "Laptop", price: 60000 },
  { id: 3, name: "Wireless Headphones", price: 12000 },
  { id: 4, name: "Smartwatch", price: 15000 },
  { id: 5, name: "Tablet", price: 30000 },
  { id: 6, name: "Gaming Mouse", price: 4500 },
];