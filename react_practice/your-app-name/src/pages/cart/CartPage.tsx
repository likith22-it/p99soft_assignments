import { CartSummary } from "../../features/cart/CartSummary";

interface CartPageProps {
  onBack: () => void;
}

export const CartPage = ({ onBack }: CartPageProps) => {
  return (
    <div className="page-shell">
      <button className="primary-button" onClick={onBack}>
        ← Back to Store
      </button>
      <h1>Your Cart</h1>
      <CartSummary />
    </div>
  );
};