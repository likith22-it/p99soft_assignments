import React, { useEffect, useState } from "react";

import OrderForm from "./components/OrderForm";
import OrdersTable from "./components/OrdersTable";

import { loadOrders, saveOrders } from "./storage/orderStorage";

import { createOrder } from "./services/orderService";

import { sendOrderNotification } from "./services/notificationService";

import { exportCSV } from "./services/reportService";

export default function App() {
  const [user, setUser] = useState("vip");
  const [item, setItem] = useState("laptop");
  const [qty, setQty] = useState(1);
  const [payment, setPayment] = useState("card");
  const [orders, setOrders] = useState([]);
  const [message, setMessage] = useState("");

  useEffect(() => {
    setOrders(loadOrders());
  }, []);

  useEffect(() => {
    saveOrders(orders);
  }, [orders]);

  async function buyNow() {
    try {
      const order = createOrder(
        user,
        item,
        Number(qty),
        payment
      );

      setOrders([...orders, order]);

      await sendOrderNotification(user, order.id);

      setMessage(
        `Order ${order.id} placed. Total: ${order.total}`
      );
    } catch (err) {
      setMessage(err.message);
    }
  }

  function refund(orderId) {
    const updated = orders.map((o) =>
      o.id === orderId
        ? { ...o, status: "REFUNDED" }
        : o
    );

    setOrders(updated);
  }

  function handleExport() {
    const revenue = exportCSV(orders);

    setMessage(`Revenue: ${revenue}`);
  }

  return (
    <div className="page">
      <h1>Modular Commerce Admin</h1>

      <OrderForm
        user={user}
        setUser={setUser}
        item={item}
        setItem={setItem}
        qty={qty}
        setQty={setQty}
        payment={payment}
        setPayment={setPayment}
        onBuy={buyNow}
        onExport={handleExport}
      />

      <OrdersTable
        orders={orders}
        refund={refund}
      />

      <p>{message}</p>
    </div>
  );
}