import React from "react";

export default function OrderForm({
  user,
  setUser,
  item,
  setItem,
  qty,
  setQty,
  payment,
  setPayment,
  onBuy,
  onExport
}) {
  return (
    <div className="card">
      <h2>Create Order</h2>

      <input value={user} onChange={(e) => setUser(e.target.value)} />

      <select value={item} onChange={(e) => setItem(e.target.value)}>
        <option value="laptop">laptop</option>
        <option value="phone">phone</option>
        <option value="headset">headset</option>
      </select>

      <input
        type="number"
        value={qty}
        onChange={(e) => setQty(Number(e.target.value))}
      />

      <select
        value={payment}
        onChange={(e) => setPayment(e.target.value)}
      >
        <option value="card">card</option>
        <option value="paypal">paypal</option>
        <option value="cod">cod</option>
      </select>

      <button onClick={onBuy}>Buy</button>
      <button onClick={onExport}>Export</button>
    </div>
  );
}