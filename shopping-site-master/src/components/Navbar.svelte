<script lang="ts">
    import cartStore from "../stores/cart";
    import currentUser from "../stores/user";

    let cartItems = 0;

    cartStore.subscribe((items) => {
        let total = 0;
        items.forEach((item) => {
            total += item.quantity;
        });
        cartItems = total;
    });

    let user = "";
    currentUser.subscribe((username) => {
        user = username;
    });
</script>

<div class="navbar bg-base-100">
    <div class="navbar-start">
        <div class="dropdown">
            <button tabindex="0" class="btn btn-ghost lg:hidden">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    ><path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M4 6h16M4 12h8m-8 6h16"
                    /></svg
                >
            </button>
            <ul
                class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-44"
            >
                <li class="dropdown dropdown-right">
                    <button tabindex="0" class="btn btn-ghost gap-2">
                        Categories
                        <svg
                            class="fill-current"
                            xmlns="http://www.w3.org/2000/svg"
                            width="24"
                            height="24"
                            viewBox="0 0 24 24"
                            ><path
                                d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"
                            />
                        </svg>
                    </button>
                    <ul
                        class="menu dropdown-content p-2 shadow bg-base-200 rounded-box"
                    >
                        <li><a href="/category/men">Men</a></li>
                        <li><a href="/category/women">Women</a></li>
                        <li><a href="/category/kids">Kids</a></li>
                    </ul>
                </li>
                <li><a href="/cart">Cart</a></li>
                <li><a href="/login">Login</a></li>
                <li><a href="/statistics">Statistics</a></li>
                <li><a href="/about">About Us</a></li>
            </ul>
        </div>
        <a class="btn btn-ghost normal-case text-xl" href="/">Home</a>
    </div>
    <div class="navbar-end">
        <div class="dropdown mr-2 hidden lg:block">
            <button tabindex="0" class="btn gap-2">
                Categories
                <svg
                    class="fill-current"
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                    ><path
                        d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"
                    />
                </svg>
            </button>
            <ul
                class="dropdown-content menu p-2 shadow bg-base-200 rounded-box w-52 mt-2"
            >
                <li><a href="/category/men">Men</a></li>
                <li><a href="/category/women">Women</a></li>
                <li><a href="/category/kids">Kids</a></li>
            </ul>
        </div>
        <ul class="menu menu-horizontal hidden lg:flex">
            <li>
                {#if user.length > 0}
                    <button
                        class="btn btn-ghost"
                        on:click={() => {
                            currentUser.set("");
                        }}
                    >
                        Logout
                    </button>
                {:else}
                    <a class="btn btn-ghost" href="/login">Login</a>
                {/if}
            </li>
            <li><a href="/statistics">Statistics</a></li>
            <li><a href="/about">About Us</a></li>
        </ul>
        <a class="btn btn-ghost btn-circle" href="/cart">
            <div class="indicator">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    ><path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
                    /></svg
                >
                {#if cartItems > 0}
                    <span
                        class="badge bg-orange-600 border-orange-600 badge-sm indicator-item"
                    >
                        {cartItems}
                    </span>
                {/if}
            </div>
        </a>
    </div>
</div>
