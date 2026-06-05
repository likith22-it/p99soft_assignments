import { createContext, useContext, useMemo, useState, type ReactNode } from "react";
import type { Product } from "../../entities/product/productData";

export type CartItem = Product & { quantity: number };

interface CartContextValue {
  items: CartItem[];
  totalItems: number;
  totalPrice: number;
  addProduct: (product: Product) => void;
  removeProduct: (productId: number) => void;
  clearCart: () => void;
}

const CartContext = createContext<CartContextValue | null>(null);

interface CartProviderProps {
  children: ReactNode;
}

export const CartProvider = ({ children }: CartProviderProps) => {
  const [items, setItems] = useState<CartItem[]>([]);

  const addProduct = (product: Product) => {
    setItems((current) => {
      const existing = current.find((item) => item.id === product.id);
      if (existing) {
        return current.map((item) =>
          item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item,
        );
      }

      return [...current, { ...product, quantity: 1 }];
    });
  };

  const removeProduct = (productId: number) => {
    setItems((current) => current.filter((item) => item.id !== productId));
  };

  const clearCart = () => setItems([]);

  const totals = useMemo(
    () => ({
      totalItems: items.reduce((sum, item) => sum + item.quantity, 0),
      totalPrice: items.reduce((sum, item) => sum + item.price * item.quantity, 0),
    }),
    [items],
  );

  return (
    <CartContext.Provider
      value={{
        items,
        totalItems: totals.totalItems,
        totalPrice: totals.totalPrice,
        addProduct,
        removeProduct,
        clearCart,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};

export const useCartContext = () => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error("useCartContext must be used inside CartProvider");
  }
  return context;
};
