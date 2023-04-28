<script lang="ts">
    import cartStore from "../stores/cart";
    import type { Item } from "../types/items";

    export let item: Item;

    let quantity = 0;

    cartStore.subscribe((cart) => {
        const itemInCart = cart.get(item.id);
        if (itemInCart) {
            quantity = itemInCart.quantity;
        } else {
            quantity = 0;
        }
    });

    const addToCart = () => {
        cartStore.update((cart) => {
            const itemInCart = cart.get(item.id);
            if (itemInCart) {
                itemInCart.quantity++;
            } else {
                cart.set(item.id, {
                    id: item.id,
                    name: item.name,
                    description: item.description,
                    category: item.category,
                    price: item.price,
                    image: item.image,
                    quantity: 1,
                });
            }
            return cart;
        });
    };

    const removeFromCart = () => {
        cartStore.update((cart) => {
            const itemInCart = cart.get(item.id);
            if (itemInCart) {
                itemInCart.quantity--;
                if (itemInCart.quantity === 0) {
                    cart.delete(item.id);
                }
            }
            return cart;
        });
    };
</script>

{#if quantity > 0}
    <div
        class="grid grid-cols-3 h-10 w-24 rounded-lg bg-orange-600 text-white font-bold mx-auto"
    >
        <button on:click={() => removeFromCart()} class="rounded-r">-</button>
        <div class="flex items-center justify-around">
            {quantity}
        </div>
        <button on:click={() => addToCart()} class="rounded-l">+</button>
    </div>
{:else}
    <div>
        <button
            class="add-to-cart"
            on:click={() => {
                addToCart();
            }}
        >
            Add to Cart
        </button>
    </div>
{/if}

<style>
    .add-to-cart {
        padding: 10px 20px;
        background-color: rgb(255, 88, 0);
        color: #fff;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
    }

    .add-to-cart:hover {
        background-color: #fff;
        color: rgb(255, 88, 0);
        border: 1px solid rgb(255, 88, 0);
    }
</style>
