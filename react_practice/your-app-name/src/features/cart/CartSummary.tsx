import { useCart } from "./useCart";

export const CartSummary = () => {
  const { items, totalItems, totalPrice, clearCart, removeProduct } = useCart();

  return (
    <section className="cart-summary">
      <h2>Cart</h2>
      {items.length === 0 ? (
        <p className="cart-empty">Your cart is empty.</p>
      ) : (
        <div>
          <p className="cart-total">
            {totalItems} item{totalItems === 1 ? "" : "s"} • ₹{totalPrice}
          </p>
          <ul className="cart-item-list">
            {items.map((item) => (
              <li key={item.id} className="cart-item">
                <span>
                  {item.name} x {item.quantity}
                </span>
                <button className="danger-button" onClick={() => removeProduct(item.id)}>
                  Remove
                </button>
              </li>
            ))}
          </ul>
          <button className="primary-button" onClick={clearCart}>
            Clear cart
          </button>
        </div>
      )}
    </section>
  );
};
