// app/App.tsx
import { useState } from "react";
import { CartProvider } from "../features/cart/CartContext";
import { CartPage } from "../pages/cart/CartPage";
import { HomePage } from "../pages/home/HomePage";

function App() {
  const [page, setPage] = useState<"home" | "cart">("home");

  return (
    <CartProvider>
      {page === "home" ? (
        <HomePage onShowCart={() => setPage("cart")} />
      ) : (
        <CartPage onBack={() => setPage("home")} />
      )}
    </CartProvider>
  );
}

export default App;