import type { Product } from "../../entities/product/productData";
import { useCart } from "../cart/useCart";

interface AddToCartButtonProps {
  product: Product;
}

export const AddToCartButton = ({ product }: AddToCartButtonProps) => {
  const { addProduct } = useCart();

  const handleClick = () => {
    addProduct(product);
  };

  return (
    <button className="primary-button" onClick={handleClick}>
      Add to Cart
    </button>
  );
};