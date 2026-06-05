// widgets/product-list/ProductList.tsx
import { products } from "../../entities/product/productData";
import { ProductCard } from "../../entities/product/productCard";

export const ProductList = () => {
  return (
    <div className="product-grid">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};