// pages/home/HomePage.tsx
import { useCart } from "../../features/cart/useCart";
import { ProductList } from "../../widgets/product-list/ProductList";

interface HomePageProps {
  onShowCart: () => void;
}

export const HomePage = ({ onShowCart }: HomePageProps) => {
  const { totalItems } = useCart();

  return (
    <div className="page-shell">
      <div className="store-header">
        <div>
          <h1>My Store</h1>
          <p>Browse products and add items to your cart.</p>
        </div>
        <button className="primary-button" onClick={onShowCart}>
          View Cart ({totalItems})
        </button>
      </div>
      <ProductList />
    </div>
  );
};