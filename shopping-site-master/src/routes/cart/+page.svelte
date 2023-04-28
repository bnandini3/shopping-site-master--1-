<script lang="ts">
    import CartQuantityButton from "../../components/CartQuantityButton.svelte";
    import cartStore from "../../stores/cart";
    import type { CartItem } from "../../types/items";

    let cartItems = new Map<string, CartItem>();

    let cartTotal = 0;
    const updateCartTotal = () => {
        let total = 0;
        cartItems.forEach((item) => {
            total += item.price * item.quantity;
        });
        cartTotal = total;
    };

    cartStore.subscribe((cart) => {
        cartItems = cart;
        updateCartTotal();
    });
</script>

<main class="max-w-6xl mx-auto">
    <h1 class="font-bold">Your Shopping Cart</h1>
    <table>
        <tr>
            <th>Product</th>
            <th>Description</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
        </tr>
        {#each Array.from(cartItems.values()) as cartItem (cartItem.id)}
            <tr>
                <td>
                    <img
                        src={"/images/" + cartItem.image}
                        alt={cartItem.name}
                        width="100"
                        height="100"
                    />
                </td>
                <td>{cartItem.name}</td>
                <td>${cartItem.price}</td>
                <td><CartQuantityButton item={cartItem} /></td>
                <td>${cartItem.price * cartItem.quantity}</td>
            </tr>
        {/each}
        <tr>
            <td colspan="4">Total</td>
            <td>${cartTotal}</td>
        </tr>
    </table>
    <div class="checkout">
        <a href="/" class="btn">Continue Shopping</a>
        <a class="btn" href="/payment-page" class:btn-disabled={!cartTotal}
            >Checkout</a
        >
    </div>
</main>

<style>
    h1 {
        font-size: 44px;
        margin-bottom: 20px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }

    th,
    td {
        border: 1px solid #ccc;
        padding: 10px;
        text-align: left;
    }

    th {
        background-color: #333;
        color: #fff;
    }

    .checkout {
        display: flex;
        justify-content: flex-end;
        margin-top: 20px;
    }

    .checkout .btn {
        margin-left: 10px;
        background-color: rgb(255, 88, 0);
        color: #fff;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        text-decoration: none;
    }

    .checkout .btn-disabled {
        background-color: #ccc;
        cursor: not-allowed;
    }
</style>
