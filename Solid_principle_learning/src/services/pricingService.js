const PRODUCT_PRICES = {
  laptop: 1000,
  phone: 500,
  headset: 50,
  misc: 20
};

export function calculateTotal(item, qty, user) {
  let total = PRODUCT_PRICES[item] * qty;

  if (user === "vip") {
    total *= 0.7;
  } else if (qty > 10) {
    total *= 0.85;
  }

  return total;
}