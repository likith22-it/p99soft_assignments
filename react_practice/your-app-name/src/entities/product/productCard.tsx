// entities/product/ProductCard.tsx
import { AddToCartButton } from "../../features/add-to-cart/AddToCartButton";
import type { Product } from "./productData";

interface ProductCardProps {
  product: Product;
}

export const ProductCard = ({ product }: ProductCardProps) => {
  return (
    <article className="product-card">
      <div>
        <h3>{product.name}</h3>
        <p>₹{product.price}</p>
      </div>
      <AddToCartButton product={product} />
    </article>
  );
};