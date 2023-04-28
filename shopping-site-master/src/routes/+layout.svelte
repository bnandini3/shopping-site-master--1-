<script>
    import "../app.css";
    import CopyRight from "../components/CopyRight.svelte";
    import Navbar from "../components/Navbar.svelte";
    import { itemsData } from "../stores/data";
    import itemsStore from "../stores/items";

    itemsStore.set(itemsData);
</script>

<div class="min-h-screen">
    <Navbar />
    <slot />
</div>
<CopyRight />
