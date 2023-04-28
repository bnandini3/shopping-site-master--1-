<script lang="ts">
    import type { Item } from "../types/items";
    import CartQuantityButton from "./CartQuantityButton.svelte";

    export let item: Item;
</script>

<div class="product-card">
    <img src={"/images/" + item.image} alt={item.name} />
    <h2>{item.name}</h2>
    <p>{item.description}</p>
    <span class="price">${item.price}</span>
    <div class="mt-4">
        <CartQuantityButton {item} />
    </div>
</div>

<style>
    .product-card {
        margin-bottom: 40px;
        text-align: center;
        border: 1px solid #ccc;
        padding: 20px;
    }

    .product-card img {
        width: 100%;
    }

    .product-card h2 {
        margin-top: 10px;
        margin-bottom: 5px;
        font-size: 20px;
        font-weight: bold;
    }

    .product-card p {
        margin-bottom: 10px;
    }

    .product-card .price {
        font-size: 18px;
        font-weight: bold;
        color: rgb(255, 88, 0);
    }
</style>
